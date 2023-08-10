from django.db import models

class UserRegistration(models.Model):
    email = models.EmailField(unique=True)
    app_password = models.CharField(max_length=100)
    new_password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

class UserDetails(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class DraftEmail(models.Model):
    subject = models.CharField(max_length=255)
    toaddr = models.TextField()
    body = models.TextField()

class option(models.Model):
    option = models.CharField(max_length=100)


class Details:
    email: str
    password: str


class Compose:
    recipient: str
    subject: str
    body: str
