from rest_framework import serializers
from .models import Encrypt, Decrypt


class EncryptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encrypt
        fields = ('encrypted_text', )


class DecryptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decrypt
        fields = ('decrypted_text', )
