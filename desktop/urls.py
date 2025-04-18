from django.urls import path
from .views import serial_page, start_reading, stop_reading, get_data, render_html

urlpatterns = [
    path("test/", render_html, name="home"),
    path("", serial_page, name="serial_page"),
    path("start/", start_reading, name="start_reading"),
    path("stop/", stop_reading, name="stop_reading"),
    path("data/", get_data, name="get_data"),
]
