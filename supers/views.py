from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super

@api_view(['GET', 'POST'])
def all_supers(request):
    if request.method == 'GET':
        print('it made it')
        query_set = Super.objects.all()
        serializer = SuperSerializer(query_set, many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)
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

