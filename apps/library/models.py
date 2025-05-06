from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth  = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey to Author model
    published_date = models.DateField()
    genre = models.CharField(max_length=50)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title