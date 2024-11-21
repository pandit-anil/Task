from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import  UserForm
from .serializers import UserFormSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserFormView(ModelViewSet):
    queryset = UserForm.objects.all()
    serializer_class = UserFormSerializers
    
    

#Other Method

class FormView(APIView):
    def get(self,request):
        queryset = UserForm.objects.all()
        serializer = UserFormSerializers(queryset, many=True)
        return Response({'status': 200, 'payload': serializer.data})
    
    def post(self, request):
        serializer = UserFormSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        try:
            user_data = UserForm.objects.get(id = request.data.get('id'))
            serializer = UserFormSerializers(user_data, data=request.data, partial=True )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({'errors':'user not fount'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
       
            user_data = UserForm.objects.filter(id = request.data.get('id'))
            if user_data.exists():
                user_data.delete()
                return Response({'message':'deleted successfully'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':'user not fount'},status=status.HTTP_400_BAD_REQUEST)
        