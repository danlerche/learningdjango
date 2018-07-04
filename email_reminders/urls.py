from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:reminder_id>/', views.reminder_entry, name='reminder'),
]
