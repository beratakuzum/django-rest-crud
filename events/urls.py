from django.urls import path

from events import views

urlpatterns = [
    path(r'', views.events_list),
    path('<int:pk>/', views.event_detail)
]