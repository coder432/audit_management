from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login,name = 'login'),
    path('SubmitResponse/<slug:s_id>',views.SubmitResponse,name = 'SubmitResponse'),
    path('details/<slug:emp_id>',views.details, name = 'details'),
    path('files/<slug:emp_id>/',views.show_files, name = 'show_files'),
    path('sheets/<slug:emp_id>/<slug:file_id>',views.sheets, name = 'sheets'),
    
    ]