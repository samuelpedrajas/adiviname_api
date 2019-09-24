from django.db import models

 # Create Game Model
class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update
    creator = models.ForeignKey('auth.User', related_name='game', on_delete=models.CASCADE)


class Expression(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update
    creator = models.ForeignKey('auth.User', related_name='expression', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name='expression', on_delete=models.CASCADE)
