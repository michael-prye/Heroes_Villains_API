from dataclasses import dataclass
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super

@api_view(['GET', 'POST'])
def all_supers(request):
    if request.method == 'GET':
        param = request.query_params.get('type')
        custom_response_dictionary = {}
        if param:
            query=Super.objects.filter(super_type__type=param)
            serializer=SuperSerializer(query,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:

            hero_query=Super.objects.filter(super_type__type='hero')
            hero_serializer=SuperSerializer(hero_query, many=True)
            villain_query=Super.objects.filter(super_type__type='villain')
            villain_serializer=SuperSerializer(villain_query,many=True)
            custom_response_dictionary={
            'hero': hero_serializer.data,
            'villain': villain_serializer.data
            }
            return Response(custom_response_dictionary, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def single_super(request, pk):
    query_set = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(query_set)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SuperSerializer(query_set, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        query_set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

