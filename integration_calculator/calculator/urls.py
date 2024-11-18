from django.urls import path
from . import views
from .views.trapesium_view import TrapesiumView
from .views.simpson_1_3_view import Simpson_1_3

urlpatterns = [
    # path('', views.index, name='index'),
    path('trapesium', TrapesiumView.as_view()),
    path('simpson_1_3', Simpson_1_3.as_view())
]
