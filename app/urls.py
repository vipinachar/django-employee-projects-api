from django.contrib import admin
from django.urls import path
from app.views import Employee
from app.views import get_projects
from app.views import whose_project

urlpatterns = [
    path('all', Employee.as_view()),
    path('projects/<int:emp_id>',get_projects.as_view()),
    path('get_employee/<int:project_id>', whose_project.as_view())
]
