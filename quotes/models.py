from django.db import models
from django.contrib.auth.models import User
import uuid
import random

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    is_hidden = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_validated = models.BooleanField(default=True)

    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def list(cls):
        result = ''
        for author in cls.objects.all():
            result += f"{author.key}\t{author.name}\n"
        return result


class Quote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(max_length=400)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL)
    is_hidden = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_validated = models.BooleanField(default=True)

    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.text} - {self.author if self.author else 'unknown'}"

    @classmethod
    def random_quote(cls):
        qset = cls.objects.filter(is_hidden=False, is_deleted=False)
        n = random.randint(0, qset.count())
        return qset.all()[n]

    @classmethod
    def from_author(cls, author):
        qset = cls.objects.filter(author=author, is_hidden=False, is_deleted=False)
        n = random.randint(0, qset.count())
        return qset.all()[n]
