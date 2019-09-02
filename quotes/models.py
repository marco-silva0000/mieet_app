from django.db import models
import uuid
import random

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def list(cls):
        result = ''
        for author in cls.objects.all():
            result += f"{author.key}\t{author.name}"
        return result


class Quote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(max_length=400)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.text} - {self.author if self.author else 'unknown'}"

    @classmethod
    def random_quote(cls):
        n = random.randint(0, cls.objects.count())
        return cls.objects.all()[n]

    @classmethod
    def from_author(cls, author):
        qset = cls.objects.filter(author=author)
        n = random.randint(0, qset.count())
        return qset.all()[n]
