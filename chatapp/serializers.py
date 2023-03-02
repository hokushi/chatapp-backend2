from rest_framework import serializers
from .models import ChatappMessage, ChatappUser

# request -> validation -> DBに保存
class MessagePostSerializer(serializers.Serializer):
    chatappUser_id = serializers.IntegerField()
    message = serializers.CharField()

    def create(self, validated_data):
        return ChatappMessage.objects.create(
            sendername=ChatappUser.objects.get(id=validated_data["chatappUser_id"]), 
            message=validated_data["message"]
        )
    
    def update(self, instance, validated_data):
        instance.sendername = ChatappUser.objects.get(id=validated_data["chatappUser_id"])
        instance.message = validated_data["message"]
        instance.save()
        return instance

# DB → いい感じにデータ整形 → response
class MessageGetSerializer(serializers.Serializer):
    message = serializers.CharField()
    sendername = serializers.CharField()
    sendername_id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
