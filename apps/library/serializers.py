from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField()

    def create(self, validate_data):
        # Create and return a new `Author` instance, given the validated data.
        return Author.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        # Update and return an existing `Author` instance, given the validated data.
        instance.name = validated_data.get('name', instance.name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()
        return instance
    
    def delete(self, instance):
        # Delete the `Author` instance.
        instance.delete()
        return instance
    

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())  # ForeignKey to Author model
    published_date = serializers.DateField()
    genre = serializers.CharField(max_length=50)
    is_archived = serializers.BooleanField(default=False)


    def create(self, validated_data):
        # Create and return a new `Book` instance, given the validated data.
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # Update and return an existing `Book` instance, given the validated data.
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.is_archived = validated_data.get('is_archived', instance.is_archived)
        instance.save()
        return instance
    
    def delete(self, instance):
        # Delete the `Book` instance.
        instance.delete()
        return instance