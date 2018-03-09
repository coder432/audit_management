from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login,name = 'login'),
    path('register',views.register,name = 'register'),
    path('get_auditor',views.get_auditor,name = 'get_auditor)'),
    path('CreateAudit',views.CreateAudit,name = "CreateAudit"),
    path('AuditorList',views.AuditorList, name = "AuditorList"),
    path('get_audit',views.get_audit, name="get_audit"),
    path('AuditList',views.AuditList, name ="AuditList"),
    path('AuditSheets/<slug:audit_id>',views.AuditSheets,name = "AuditSheets"),
    path('EditAuditor/<slug:emp_id>',views.EditAuditor,name = "EditAuditor"),
    path('DeleteAuditor/<slug:emp_id>',views.DeleteAuditor,name = "DeleteAuditor"),
    path('CreateSheet/<slug:audit_id>',views.CreateSheet,name = "CreateSheet"),
    path('get_sheet/<slug:audit_id>',views.get_sheet,name = "get_sheet"),
    path('questions/<slug:s_id>',views.questions,name = "questions"),
    path('CreateQuestions/<slug:s_id>',views.CreateQuestions,name = "CreateQuestions"),
    path('get_questions/<slug:s_id>',views.get_questions,name = 'get_questions')
    ]
    