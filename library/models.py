from django.db import models

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(TimestampMixin, Person): #на старой домашке решил использовать абстрактые классы если так можно
    bio = models.TextField()

class Publisher(TimestampMixin, Person):
    location = models.CharField(max_length=100)

class Book(TimestampMixin, models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', default=None, null=True, blank=True)

    def __str__(self):
        return self.title
