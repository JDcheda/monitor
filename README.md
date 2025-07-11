# Monitor del Sistema con Django y Psutil

## 📄 Descripción
Aplicación web que muestra en tiempo real el estado del sistema (CPU, RAM, Disco, Sistema operativo y núcleos).

## ⚙️ Instalación

1️⃣ Clonar el repositorio:

```bash
git clone https://github.com/JDcheda/monitor.git
cd monitor
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

