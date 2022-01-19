from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles_api import serializers


class HelloApiView(APIView):
    '''Test API View'''
    serializer_class = serializers.HelloSerializer # serializer class가 포함되도록 api보기가 구성
    #게시물 넣기 또는 패치요청을 보낼때 마다 이름이 있는 입력이 필요, 최대길이 10가지 해당 입력의 유효성을 검사함

    def get(selfself, request, format = None):
        '''Returns a list of APIView features'''

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over uou application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        '''Create a hello message with our name'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        '''Handle updating an object'''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''Handle a partial update of an object'''
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk=None):
        '''Delete an object'''
        return Response({'method': 'DELETE'})



