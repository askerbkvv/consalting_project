from rest_framework import serializers
from .models import Form, Comment, University


class FormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Form
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = '__all__'
