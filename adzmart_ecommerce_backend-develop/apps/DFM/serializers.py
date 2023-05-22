from rest_framework import serializers
from .models import MediaAdvisory, MediaBrief, Support


class MediaAdvisorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAdvisory
        exclude = ("created_at", "updated_at", "uuid")


class MediaBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaBrief
        exclude = ("created_at", "updated_at", "uuid")
        

class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        exclude = ("created_at", "updated_at", "uuid")


class MediaBriefListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaBrief
        exclude = ("created_at", "updated_at", "uuid")


class MediaAdvisoryListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAdvisory
        exclude = ("created_at", "updated_at", "uuid")


class SupportListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        exclude = ("created_at", "updated_at", "uuid")
