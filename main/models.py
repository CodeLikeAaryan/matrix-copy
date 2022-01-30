from django.contrib.auth.models import User
from django.db import models
from matplotlib.pyplot import title


# Create your models here.

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    # pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='book/cover/', null=True, blank=True)

    def __str__(self):
        return self.title





class PersonalFiles(models.Model):
    IMPDOCS = (
        ('notes', 'NOTES'),
        ('certificate', 'CERTIFICATE'),
        ('documents', 'DOCUMENTS'),
        ('question Papers', 'QUESTION PAPERS'),
        ('study material', 'STUDY MATERIAL'),
    )

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=IMPDOCS)
    cover = models.ImageField(upload_to='book/cover/', null=True, blank=True)


    def __str__(self):
        return self.file_name

"""
class PersonalFiles(models.Model):
    CATEGORY = (
        'Notes', 'Notes',
        'Certificates, Certificates',
    )

    # relationwith user
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL) 
    file_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY)
    file = models.FileField(upload_to="")

    def __str__(self):
        return self.file_name
"""
