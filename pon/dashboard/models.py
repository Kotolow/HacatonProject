from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)
    picked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='news/', blank=True, null=True)
    rating = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    place = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

