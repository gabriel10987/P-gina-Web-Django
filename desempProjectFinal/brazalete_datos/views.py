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
    ref_reminders = db.reference('/reminders')
    reminders = ref_reminders.get()

    ref_closest_reminder = db.reference('/closestReminders')
    closest_reminder = ref_closest_reminder.get()

    # Formatear la fecha
    if closest_reminder:
        reminder_time = closest_reminder.get('reminderTime')
        if reminder_time:
            # Convertir el timestamp a una fecha legible
            closest_reminder['reminderTime'] = datetime.fromtimestamp(reminder_time / 1000).strftime('%d/%m/%Y %H:%M:%S')

    for d, valor in reminders.items():
        if valor:
            reminder_time = valor["reminderTime"]
        if reminder_time:
            valor['reminderTime'] = datetime.fromtimestamp(reminder_time / 1000).strftime('%d/%m/%Y %H:%M:%S')
    context = {
        'reminders': reminders,
        'closest_reminder': closest_reminder
    }
    return render(request, 'closest_reminders.html', context)