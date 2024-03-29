from django.utils import timezone

from django_cleanup import cleanup

from django.db import models
from .middleware import local


class GameType(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    text = models.CharField(max_length=100)

    def __unicode__(self):
        return self.text

    def __str__(self):
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
    title = models.CharField(max_length=100, null=False)
    game_type = models.ForeignKey(GameType, related_name='games', on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=False)
    examples = models.CharField(max_length=100, null=False)
    image_updated_at = models.DateTimeField(auto_now_add=True)
    image_base_updated_at = models.DateTimeField(auto_now_add=True)
    expressions_updated_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


def iconName(self, filename):
    return 'icons/' + filename


class GameIcon(BaseModel):
    game = models.OneToOneField(Game, related_name="icon", on_delete=models.CASCADE)
    file = models.ImageField(
        upload_to=iconName,
        max_length=254, blank=True, null=True
    )

    def save(self, *args, **kwargs):
        if self.game is not None:
            self.game.image_updated_at = timezone.now()
            self.game.save()
        return super(GameIcon, self).save(*args, **kwargs)

    def __str__(self):
        return self.file.name


def iconBaseName(self, filename):
    return 'icon_bases/' + filename


@cleanup.ignore
class GameIconBase(BaseModel):
    game = models.OneToOneField(Game, related_name="icon_base", on_delete=models.CASCADE)
    file = models.ImageField(
        upload_to=iconBaseName,
        max_length=254, blank=True, null=True
    )

    def save(self, *args, **kwargs):
        ret = super(GameIconBase, self).save(*args, **kwargs)
        for game in Game.objects.filter(icon_base__file=self.file):
            game.image_base_updated_at = timezone.now()
            game.save()
        return ret

    def __str__(self):
        return self.file.name


class GameClick(models.Model):
    game_id = models.OneToOneField(Game, related_name="clicks", primary_key=True, on_delete=models.CASCADE)
    num_clicks = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.num_clicks)

    def __str__(self):
        return str(self.num_clicks)


class Expression(BaseModel):
    text = models.CharField(max_length=100, null=False)
    game = models.ForeignKey(Game, related_name='expressions', on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if self.game is not None:
            self.game.updated_at = timezone.now()
            self.game.expressions_updated_at = timezone.now()
            self.game.save()
        return super(Expression, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.game is not None:
            self.game.updated_at = timezone.now()
            self.game.expressions_updated_at = timezone.now()
            self.game.save()
        return super(Expression, self).delete(*args, **kwargs)

    def __unicode__(self):
        return self.text + "(%s)" % str(self.game)

    def __str__(self):
        return self.text + "(%s)" % str(self.game)
