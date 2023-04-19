from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class GetEd(APIView):
    def get(self, request):
        ed=ElectricDevice.objects.all()
        serializer=ElectricDeviceSerializer(ed, many=True)
        return Response({
            'message':'Your data is here',
            'data':serializer.data,
        })
    

class PostEd(APIView):
    def post(self, request):
        serializer=ElectricDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'Your data is added',
                'data':serializer.data,
                'status':status.HTTP_201_CREATED,
            })
        
        return Response({
            'message':'Something went wrong',
            'error':serializer.errors,
        })    
    
    
class PutEd(APIView):
    def put(self, request):
        data=request.data
        ed=ElectricDevice.objects.get(id=data.get('id'))
        serializer=ElectricDeviceSerializer(ed, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'Your data is updated',
                'data':serializer.data,
                'status':status.HTTP_200_OK,
            })
        
        return Response({
            'message':'Something went wrong',
            'error':serializer.errors,
            'status':status.HTTP_400_BAD_REQUEST,
        })
        
        
class PatchtEd(APIView):
    def patch(self, request):
        data=request.data
        ed=ElectricDevice.objects.get(id=data.get('id'))
        serializer=ElectricDeviceSerializer(ed, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'Your data is updated',
                'data':serializer.data,
                'status':status.HTTP_200_OK,
            })
        
        return Response({
            'message':'Something went wrong',
            'error':serializer.errors,
        })
        
        
class DeleteEd(APIView):
    def delete(self, request,pk):
        ed=ElectricDevice.objects.filter(pk=pk)
        ed.delete()
        return Response({
            'message':'Your data is deleted'
        })