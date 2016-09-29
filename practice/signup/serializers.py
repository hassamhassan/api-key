from rest_framework import serializers
from signup.models import SignUp


class SignUpSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SignUp
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                  'zip_code', 'job_interest', 'owner')
