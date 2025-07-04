from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/machine1")
async def get_machine1():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "1d 2h 37m 6s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine2")
async def get_machine2():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "1d 16h 3m 16s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine3")
async def get_machine3():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "1d 12h 7m 21s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine4")
async def get_machine4():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "1d 1h 13m 59s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine5")
async def get_machine5():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "1d 21h 36m 1s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine6")
async def get_machine6():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "1d 22h 31m 19s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine7")
async def get_machine7():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "1d 5h 44m 15s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine8")
async def get_machine8():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "2d 12h 14m 38s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine9")
async def get_machine9():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "1d 23h 1m 33s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine10")
async def get_machine10():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "1d 19h 11m 38s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine11")
async def get_machine11():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "2d 21h 41m 14s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine12")
async def get_machine12():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "3d 12h 12m 6s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine13")
async def get_machine13():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "1d 19h 33m 44s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine14")
async def get_machine14():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "4d 2h 20m 10s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}

@app.get("/machine15")
async def get_machine15():
    cpu = random.randint(10, 99)
    mem = random.randint(10, 99)
    disk = random.randint(10, 99)
    uptime = "1d 22h 10m 44s"

    return {"cpu": cpu, "mem": str(mem)+"%", "disk": str(disk)+"%", "uptime": uptime}
