from django.urls import path

from sessions import views

urlpatterns = [
    path(r'', views.sessions_list),
    path('<int:pk>/', views.session_detail)
]