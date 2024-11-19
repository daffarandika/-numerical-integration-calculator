from django.urls import path
from .views.trapesium_view import TrapesiumView
from .views.simpson_1_3_view import Simpson_1_3
from .views.simpson_3_8_view import Simpson_3_8
from .views.index_view import Index
from .views.gauss_kuadratur_view import GaussKuadratur

urlpatterns = [
    path('', Index.as_view()),
    path('trapesium', TrapesiumView.as_view()),
    path('simpson_1_3', Simpson_1_3.as_view()),
    path('simpson_3_8', Simpson_3_8.as_view()),
    path('gauss_kuadratur', GaussKuadratur.as_view()),
]
