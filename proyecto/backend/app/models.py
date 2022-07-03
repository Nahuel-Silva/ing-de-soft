from distutils.command.upload import upload
from pyexpat import model
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    image = models.ImageField(default='icono_SinImagen.jpg')

    def __str__(self):
        return f"Perfil de {self.user.username}"

    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user)\
                                .values_list('to_user_id', flat=True) # Te da una lista con las relaciones del usuario.
        return User.objects.filter(id__in=user_ids) # Te devuelve los usuario que vos seguis.

    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user)\
                                .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids) # Te devuelve los usuario que te siguen.
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    timestamp = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100, default="")
    imagen_album = models.ImageField(upload_to="media")

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.username} : {self.title}"

class Relationship(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="relationships")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="related_to")

    def __str__(self):
        return f"{self.from_user} to {self.to_user}"

    class Meta:
        indexes = [
            models.Index(fields=['from_user', 'to_user', ]),
        ]