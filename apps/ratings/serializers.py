from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    rate_user = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]

    def get_rate_user(self, obj):
        return obj.rate_user.username

    def get_agent(self, obj):
        return obj.agent.user.username
