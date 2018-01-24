from django.shortcuts import render
from bokeh.embed import server_document 

from .models import Dashboard

def dashboard(request, dashboard_id):
    url = Dashboard.objects.get(id=dashboard_id).url
    script = server_document(url)
    return render(request, "weather_dashboards/dashboard.html", {"script": script})

