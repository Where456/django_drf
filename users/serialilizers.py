from rest_framework import serializers

from .models import User, Payment
from .validators import PayValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        validators = [PayValidator(field1='paid_course', field2='paid_lesson')]
