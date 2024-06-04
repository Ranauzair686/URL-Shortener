from django.db import models
import string
import random

class URL(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f'{self.long_url} -> {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super().save(*args, **kwargs)

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        while True:
            short_url = ''.join(random.choice(characters) for _ in range(6))
            if not URL.objects.filter(short_url=short_url).exists():
                return short_url
