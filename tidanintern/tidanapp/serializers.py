from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Task,Attendence


class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class Attendanceserizer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = '__all__'