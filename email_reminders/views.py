from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import reminder

def index(request):
    latest_reminder_list = reminder.objects.order_by('reminder_date')[:10]
    context = {
        'latest_reminder_list': latest_reminder_list,
    }
    return render (request, 'email_reminders/index.html', context)

def reminder_entry(request, reminder_id):
    reminders = get_object_or_404(reminder, pk=reminder_id)
    return render(request, 'email_reminders/detail.html', {'reminders': reminders})

"""def reminder_entry(request, reminder_id):
    response = "You're looking at the results of reminder %s."
    return HttpResponse(response % reminder_id)"""
