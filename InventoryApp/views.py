from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from .models import *
from django.db.models import Q

from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer  
from rest_framework.decorators import api_view, renderer_classes
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .serializers import *

def get_equipment(request,id):
        equip=get_object_or_404(Equipment,id=id)
        serializer=EquipmentSerializer(equip)
        return Response(serializer.data,status=status.HTTP_200_OK)

class EquipmentListView(generics.ListAPIView):
   
    
        queryset=Equipment.objects.all()
        serializer_class=EquipmentSerializer
        
class EquipmentDetailView(APIView):

    def get(self, request,id):
        return get_equipment(request,id)
    
    # sending access-request to manager
    def post(self, request,id):
        equip=get_object_or_404(Equipment,id=id)
        if equip.issued:
             return Response({'message':'Item is already Issued'},status=status.HTTP_208_ALREADY_REPORTED)
        user_type='Employee' 
        access_request=AccessRequest.objects.get_or_create(access_request='Sent',issued_element=equip,user_type=user_type)
        return Response({'success':'Access Request sent successfully'},status=status.HTTP_200_OK)    

class IssueandReturn(APIView):

    def get(self, request,id):
        return get_equipment(request,id)

    #return_item_to_manager
    def post(self, request,id):

        equip=get_object_or_404(Equipment,id=id)
        if equip.issued==False:
            return Response({'message':'No acccess rights to send unissued element to manager '},status=status.HTTP_401_UNAUTHORIZED)

        equip.send_to_manager=True
        equip.save()

        return Response({'success':'Item Successfully returned to Manager'},status=status.HTTP_200_OK)    

class AccessRequestListView(generics.ListAPIView):

    # Shows list of Access-Requests to manager
    
        queryset=AccessRequest.objects.filter(access_request='Sent',user_type='Employee')
        serializer_class=AccessRequestSerializer


class List_issued_elements(generics.ListAPIView):
    queryset=Equipment.objects.filter(Q(issued=True)|Q(send_to_manager=True))
    serializer_class=EquipmentSerializer
   
     