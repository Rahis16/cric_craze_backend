from rest_framework import serializers
from .models import LiveStream, CrouselData



class LiveStreamSerializer(serializers.ModelSerializer):
    
    flags = serializers.SerializerMethodField()
    
    class Meta:
        model = LiveStream
        fields = ['id', 'title', 'teams', 'type', 'src', 'flags', 'start_time', 'created_at']
        
        
    def get_flags(self, obj):
        return {
            'left': obj.flag_left,
            'right': obj.flag_right,
        }


class CrouselDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CrouselData
        fields = ['id', 'image', 'order', 'created_at']  
        
    
    
    