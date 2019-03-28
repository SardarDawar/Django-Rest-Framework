from rest_framework import serializers
from .models import finder




class FindSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = finder
        fields = ('id', 'Photo',"Name", "Description",'status','Date_lost','ContactNumber','TrackAddress','TrackImage')