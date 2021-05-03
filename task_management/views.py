from django.shortcuts import render
from django.shortcuts import render_to_response
from . import serializers
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.
def home(request):
    queryset = Project.objects.all()
    serializeobj = serializers.ProjectSerializer(queryset,many=True)
    context = { 
        "items":serializeobj.data
    }
    return render(request, 'homepage.html',context)

class projecttable(APIView):
    def post(self,request):
        serializeobj = serializers.ProjectSerializer(data = request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return_object = {
                "message":"success"
            }
            return JsonResponse(return_object ,safe= False)

    
    def get(self, request):
        queryset = Project.objects.all()
        serializeobj = serializers.ProjectSerializer(queryset,many=True)
        return JsonResponse(serializeobj.data ,safe= False)


class projectupdatetable(APIView):
    def get(self,request,project_id):
        try:
            queryset = Project.objects.filter(pk=project_id)
            serializeobj = serializers.ProjectSerializer(queryset,many=True)
            return JsonResponse(serializeobj.data ,safe= False)
        except Task.DoesNotExist:
            return_object = {
                "message":"No Task Found"
            }
        return JsonResponse(return_object ,safe= False)


class tasktable(APIView):
    def post(self,request,project_id):
        print("1",request.data,project_id)
        serializeobj = serializers.TaskSerializer(data = request.data)
        print("2",serializeobj)
        if serializeobj.is_valid():
            print("3")
            serializeobj.save()
            return_object = {
                "message":"Success"
            }
            return JsonResponse(return_object ,safe= False)
        else:
            print("not valid")
            return_object = {
                "message":"Fail"
            }
            return JsonResponse(return_object ,safe= False)

    
    def get(self,request,project_id):
        try:
            print("111111",project_id)
            queryset = Task.objects.filter(project_id=project_id)
            print("qqqqqq",queryset)
            serializeobj = serializers.TaskSerializer(queryset,many=True)
            return JsonResponse(serializeobj.data ,safe= False)
        except Task.DoesNotExist:
            return_object = {
                "message":"No Task Found"
            }
        return JsonResponse(return_object ,safe= False)
    
    def delete(self,request,project_id):
        try:
            print("in delete",project_id)
            queryset = Project.objects.filter(pk=project_id).delete()
            return_object = {
                    "message":"Success"
                }
            return JsonResponse(return_object ,safe= False)
        except Task.DoesNotExist:
            return_object = {
                "message":"Fail"
            }
            return JsonResponse(return_object ,safe= False)

    def put(self,request,project_id):
        try:
            print("in put")
            projobj = Project.objects.get(pk=project_id)
            serializeobj = serializers.ProjectSerializer(projobj,data = request.data)
            if serializeobj.is_valid():
                print("3")
                serializeobj.save()
                return_object = {
                    "message":"Success"
                }
                return JsonResponse(return_object ,safe= False)
            else:
                print("not valid")
                return_object = {
                    "message":"Fail"
                }
                return JsonResponse(return_object ,safe= False)
        except:
            print("not valid")
            return_object = {
                "message":"Fail"
            }
            return JsonResponse(return_object ,safe= False)


class tasktupdateable(APIView):
    def get(self,request,project_id,task_id):
        try:
            queryset = Task.objects.filter(project_id=project_id,id=task_id)
            serializeobj = serializers.TaskSerializer(queryset,many=True)
            return JsonResponse(serializeobj.data ,safe= False)
        except Task.DoesNotExist:
            return_object = {
                "message":"No Task Found"
            }
        return JsonResponse(return_object ,safe= False)

    def put(self,request,project_id,task_id):
        try:
            taskobj = Task.objects.get(pk=task_id)
            serializeobj = serializers.TaskSerializer(taskobj,data = request.data)
            if serializeobj.is_valid():
                print("3")
                serializeobj.save()
                return_object = {
                    "message":"Success"
                }
                return JsonResponse(return_object ,safe= False)
            else:
                print("not valid")
                return_object = {
                    "message":"Fail"
                }
                return JsonResponse(return_object ,safe= False)
        except:
            print("not valid")
            return_object = {
                "message":"Fail"
            }
            return JsonResponse(return_object ,safe= False)

    def delete(self,request,project_id,task_id):
        try:
            queryset = Task.objects.filter(project_id=project_id,id=task_id).delete()
            return_object = {
                    "message":"Success"
                }
            return JsonResponse(return_object ,safe= False)
        except Task.DoesNotExist:
            return_object = {
                "message":"No Task Found"
            }
            return JsonResponse(return_object ,safe= False)


