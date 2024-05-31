from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('logbook',views.logbook,name='logbook'),
    path('pdf_view', views.render_pdf_view,name='pdf_test'),
    path('new_entry',views.new_entry,name='new_entry'),
    path('time_calc',views.time_calc,name='time_calc')
]