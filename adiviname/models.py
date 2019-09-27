from django.db import models

from .middleware import local


class GameType(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    text = models.CharField(max_length=100)

    def __unicode__(self):
        return self.text


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.pk is None and hasattr(local, 'user'):
            self.creator = local.user
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['-id']


 # Create Game Model
class Game(BaseModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class GameClick(models.Model):
    game_id = models.OneToOneField(Game, related_name="click", primary_key=True, on_delete=models.CASCADE)
    num_clicks = models.IntegerField()


class Expression(BaseModel):
    text = models.CharField(max_length=100)
    game = models.ForeignKey(Game, related_name='expressions', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text + "(%s)" % str(self.game)
