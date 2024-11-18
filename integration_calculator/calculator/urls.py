from django.urls import path
from . import views
from .views.trapesium_view import TrapesiumView

urlpatterns = [
    # path('', views.index, name='index'),
    path('trapesium', TrapesiumView.as_view())
]
