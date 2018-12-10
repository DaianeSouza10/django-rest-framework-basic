from django.shortcuts import render
from .models import Contato
from .serializers import ContatoSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def contato_list(request):
    contatos = Contato.objects.all()
    serializer = ContatoSerializer(contatos, context={'request': request}, many=True)
    return Response(serializer.data)
