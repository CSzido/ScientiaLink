from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Main.models import Research, Interest


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    researches = models.ManyToManyField(Research, blank=True)
    full_name = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images")
    interests = models.ManyToManyField(Interest, blank=True)
    followers = models.ManyToManyField('Profile', related_name="followers_profile")
    following = models.ManyToManyField('Profile', related_name="following_profiles")

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)