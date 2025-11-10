from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CrouselData, LiveStream
from .serializers import CrouselDataSerializer, LiveStreamSerializer




# Create your views here.
def home(request):
    return HttpResponse("<h1>Cric Craze Nepal</h1>")


@api_view(['GET'])
def live_streams(request):
    streams = LiveStream.objects.all()
    stream_serializer = LiveStreamSerializer(streams, many=True, context={'request': request})
    return Response(stream_serializer.data)


@api_view(['GET'])
def crousel_data(request):
    crousels = CrouselData.objects.all().order_by('order')
    crouselserializer = CrouselDataSerializer(crousels, many=True, context={'request': request})
    return Response(crouselserializer.data)