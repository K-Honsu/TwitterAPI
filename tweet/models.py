from django.db import models


class Tweet(models.Model):
    message = models.CharField(max_length=140)
    upload1 = models.ImageField(upload_to='uploads/', blank=True)
    upload2 = models.ImageField(upload_to='uploads/', blank=True)
    upload3 = models.ImageField(upload_to='uploads/', blank=True)
    upload4 = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return f"{self.message} ({self.upload1}, {self.upload2}, {self.upload3}, {self.upload4})"


class Retweet(models.Model):
    retweet_id = models.ForeignKey(
        Tweet, on_delete=models.CASCADE, related_name='retweets')

    def __str__(self):
        return self.retweet_id


class Likes(models.Model):
    LIKE_CHOICES = [
        ('UP', 'up'),
        ('DOWN', 'down'),
    ]
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    like_choices = models.BooleanField(
        choices=[(True, 'Like'), (False, 'Dislike')])

    def __str__(self):
        return self.like_choices
