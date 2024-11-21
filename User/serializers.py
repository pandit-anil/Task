from rest_framework import serializers
from .models import UserForm

class UserFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserForm
        fields = '__all__'