from django.template.loader import render_to_string
import serial
from serial.tools.list_ports import comports
from django.shortcuts import render
from django.http import JsonResponse
import threading


def list_com_ports():
    ports = comports()
    return [port.device for port in ports]


def render_html(request):
    print(list_com_ports())
    return render_to_string('home.html', {'message': 'Hello World!'})


serial_data = []
is_reading = False


def read_serial():
    global is_reading, serial_data
    ser = serial.Serial("COM5", baudrate=9600, timeout=1)

    while is_reading:
        data = ser.readline().decode().strip()
        if data:
            serial_data.append(data)  # Store received data
    ser.close()  # Close the port when stopping


def start_reading(request):
    global is_reading
    if not is_reading:
        is_reading = True
        threading.Thread(target=read_serial, daemon=True).start()
    return JsonResponse({"status": "reading started"})


def stop_reading(request):
    global is_reading
    is_reading = False  # Stop the loop
    return JsonResponse({"status": "reading stopped"})


def get_data(request):
    data = [serial_data[-1] if serial_data else None]
    return JsonResponse({"data": data})  # Return collected data


def serial_page(request):
    return render(request, "serial.html")
