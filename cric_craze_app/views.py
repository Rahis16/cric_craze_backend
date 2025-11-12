from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CrouselData, LiveStream, AppVersion
from .serializers import CrouselDataSerializer, LiveStreamSerializer, AppVersionSerializer
from rest_framework import status
from rest_framework.views import APIView


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


class LatestAppVersionView(APIView):
    """
    GET /api/latest-app-version/
    Returns the latest app version info.
    """
    def get(self, request):
        latest_version = AppVersion.objects.order_by('-version_code').first()
        if not latest_version:
            return Response({"detail": "No version found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AppVersionSerializer(latest_version, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)