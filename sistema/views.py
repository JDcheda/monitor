from django.shortcuts import render
import psutil
import platform

def get_system_info():
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        system = platform.system()
        cores = psutil.cpu_count(logical=True)

        info = {
            'cpu_percent': cpu_percent,
            'memory_total': round(memory.total / (1024 ** 3), 2),  # GB
            'memory_used': round(memory.used / (1024 ** 3), 2),
            'memory_percent': memory.percent,
            'disk_total': round(disk.total / (1024 ** 3), 2),
            'disk_used': round(disk.used / (1024 ** 3), 2),
            'disk_free': round(disk.free / (1024 ** 3), 2),
            'disk_percent': disk.percent,
            'system': system,
            'cores': cores,
        }
    except Exception as e:
        info = {'error': str(e)}
    
    return info

def index(request):
    system_info = get_system_info()
    return render(request, 'sistema/index.html', {'info': system_info})

