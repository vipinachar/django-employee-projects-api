from http.client import responses
from django.shortcuts import render
from app.models import employee 
from app.serializers import employee_serializer 
from django.http import HttpResponse
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from app.models import projects

class Employee(APIView):
    def get(self, request):
        page = request.GET.get('page', None)
        page_size = request.GET.get('page_size', None)
        order_by = request.GET.get('order_by', None)
        search = request.GET.get('search', None)
        if order_by:
            e = employee.objects.order_by(order_by)
        else:
            e = employee.objects.all()
        employees = e[int(page)*int(page_size):int(page)*int(page_size)+int(page_size)] 
        response = []
        for emp in employees:
            output = { "firstname" : emp.firstname,
                        "lastname":emp.lastname,
                        "emp_id":emp.emp_id
                    }
            response.append(output)
        d=dict()
        d["total"]=employee.objects.count()
        d["page"]=page 
        d["page_size"]=page_size 
        d["users"]=response
        return Response(d, status=status.HTTP_200_OK)

class get_projects(APIView):
    def get(self, request, emp_id):
        project = employee.objects.get(emp_id=emp_id).projects_set.all()
        response=list()
        for p in project:
            d=dict()
            d["project_id"]=p.project_id
            d["project_name"]=p.project_name 
            response.append(d)
        return Response(response, status=status.HTTP_200_OK)
        
class whose_project(APIView):
    def get(self, request, project_id):
        emp = employee.objects.filter(projects__project_id=project_id)[0]
        response=dict()
        response["emp_id"]=emp.emp_id 
        response["firstname"]=emp.firstname
        response["lastname"]=emp.lastname
        return Response(response, status=status.HTTP_200_OK)







