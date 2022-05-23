from rest_framework import serializers
from todo_list.models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    body = serializers.CharField(required=False, allow_blank=True, max_length=100)
    is_completed = serializers.BooleanField(required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Create and return a new `Todo` instance, given the validated data.
        """
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Todo` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save()
        return instance

    """
    class Meta:
        model = Todo
        fields = "__all__"
    """

class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'todos']