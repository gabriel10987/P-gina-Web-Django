from django.shortcuts import render
from .firebase import db
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def help(request):
    return render(request, 'help.html')

def fetch_reminders(request):
    ref = db.reference('/reminders')
    
    data = ref.get()
    
    # Formatear la fecha
    print("imprimiendo datos")
    #print(data)
    for d, valor in data.items():
        #print("imprimiendo d")
        #print("clave: " + str(d))
        #print("valor: " + str(valor))
        if valor:
            reminder_time = valor["reminderTime"]
        if reminder_time:
            # Convertir el timestamp a una fecha legible
            valor['reminderTime'] = datetime.fromtimestamp(reminder_time / 1000).strftime('%d/%m/%Y %H:%M:%S')
    #print("datos formateados")
    #print(data)

    
    context = {
        'data': data
    }
    return render(request, 'closest_reminders.html', context)

