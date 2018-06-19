from django.db import models


class Encrypt(models.Model):
    text = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')
    encrypted_text = models.CharField(max_length=200)


class Decrypt(models.Model):
    text = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')
    decrypted_text = models.CharField(max_length=200)

