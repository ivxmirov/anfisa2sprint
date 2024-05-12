from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добавляет флаг is_published и название объекта."""
    is_published = models.BooleanField('Опубликовано', default=True)
    title = models.CharField('Название', max_length=256)


    class Meta:
        abstract = True
