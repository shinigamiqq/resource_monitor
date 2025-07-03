from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=255, unique=True)
    endpoint = models.URLField(max_length=2000)

    def __str__(self):
        return self.name

class Metric(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    cpu_usage = models.IntegerField()
    mem_usage = models.IntegerField()
    disk_usage = models.IntegerField()
    uptime = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.machine.name} - CPU: {self.cpu_usage}% at {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']

class Incident(models.Model):
    INCIDENT_TYPES = [
        ('CPU', 'CPU Usage Exceeded'),
        ('MEM', 'Memory Usage Exceeded'),
        ('DISK', 'Disk Usage Exceeded'),
    ]

    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    incident_type = models.CharField(max_length=10, choices=INCIDENT_TYPES)
    threshold_value = models.CharField(max_length=255)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        status = "Active" if self.is_active else "Resolved"
        return f"{self.machine.name} - {self.get_incident_type_display()} ({status}) at {self.start_time}"

    class Meta:
        unique_together = ('machine', 'incident_type', 'is_active')
        ordering = ['-start_time']
