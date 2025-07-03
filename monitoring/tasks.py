import requests
from celery import shared_task
from .models import Machine, Metric
from datetime import timedelta
from django.utils import timezone
from django.db.models import Avg


@shared_task
def poll_machine(machine_id):
    try:
        machine = Machine.objects.get(id=machine_id)
        response = requests.get(machine.endpoint, timeout=10)
        response.raise_for_status()
        data = response.json()

        mem_usage_int = int(data["mem"].replace('%', ''))
        disk_usage_int = int(data["disk"].replace('%', ''))

        Metric.objects.create(
            machine=machine,
            cpu_usage=data["cpu"],
            mem_usage=mem_usage_int,
            disk_usage=disk_usage_int,
            uptime=data["uptime"]
        )
        print(f"Data collected for {machine.name}: {data}")
    except Machine.DoesNotExist:
        print(f"Machine with ID {machine_id} does not exist.")
    except requests.exceptions.RequestException as e:
        print(f"Error polling {machine.endpoint}: {e}")
    except ValueError as e:
        print(f"Error parsing data from {machine.endpoint}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {machine.endpoint}: {e}")


@shared_task
def poll_all_machines():
    machines = Machine.objects.all()
    for machine in machines:
        poll_machine.delay(machine.id)
    print("Scheduled polling for all machines.")


@shared_task
def check_for_incidents():
    print("Checking for incidents...")
    machines = Machine.objects.all()
    for machine in machines:
        last_metric = Metric.objects.filter(machine=machine).order_by('-timestamp').first()
        if last_metric and last_metric.cpu_usage > 85:
            active_incident = Incident.objects.filter(
                machine=machine,
                incident_type='CPU',
                is_active=True
            ).exists()
            if not active_incident:
                Incident.objects.create(
                    machine=machine,
                    incident_type='CPU',
                    threshold_value='85%',
                    is_active=True
                )
                print(f"Incident created: CPU > 85% for {machine.name}")

        time_30_mins_ago = timezone.now() - timedelta(minutes=30)
        recent_mem_metrics = Metric.objects.filter(
            machine=machine,
            timestamp__gte=time_30_mins_ago
        )
        if recent_mem_metrics.count() >= 2:
            avg_mem_usage = recent_mem_metrics.aggregate(Avg('mem_usage'))['mem_usage__avg']
            if avg_mem_usage and avg_mem_usage > 90:
                active_incident = Incident.objects.filter(
                    machine=machine,
                    incident_type='MEM',
                    is_active=True
                ).exists()
                if not active_incident:
                    Incident.objects.create(
                        machine=machine,
                        incident_type='MEM',
                        threshold_value='90% for 30 mins',
                        is_active=True
                    )
                    print(f"Incident created: MEM > 90% for 30 mins for {machine.name}")
        elif recent_mem_metrics.count() == 1 and recent_mem_metrics.first().mem_usage > 90:
            active_incident = Incident.objects.filter(
                machine=machine,
                incident_type='MEM',
                is_active=True
            ).exists()
            if not active_incident:
                Incident.objects.create(
                    machine=machine,
                    incident_type='MEM',
                    threshold_value='90%',
                    is_active=True
                )
                print(f"Incident created: MEM > 90% (single reading) for {machine.name}")


        time_2_hours_ago = timezone.now() - timedelta(hours=2)
        recent_disk_metrics = Metric.objects.filter(
            machine=machine,
            timestamp__gte=time_2_hours_ago
        )
        if recent_disk_metrics.count() >= 2:
            avg_disk_usage = recent_disk_metrics.aggregate(Avg('disk_usage'))['disk_usage__avg']
            if avg_disk_usage and avg_disk_usage > 95:
                active_incident = Incident.objects.filter(
                    machine=machine,
                    incident_type='DISK',
                    is_active=True
                ).exists()
                if not active_incident:
                    Incident.objects.create(
                        machine=machine,
                        incident_type='DISK',
                        threshold_value='95% for 2 hours',
                        is_active=True
                    )
                    print(f"Incident created: DISK > 95% for 2 hours for {machine.name}")
        elif recent_disk_metrics.count() == 1 and recent_disk_metrics.first().disk_usage > 95:
            active_incident = Incident.objects.filter(
                machine=machine,
                incident_type='DISK',
                is_active=True
            ).exists()
            if not active_incident:
                Incident.objects.create(
                    machine=machine,
                    incident_type='DISK',
                    threshold_value='95%',
                    is_active=True
                )
                print(f"Incident created: DISK > 95% (single reading) for {machine.name}")

    print("Incident check complete.")
