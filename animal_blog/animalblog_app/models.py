from django.db import models


class AnimalCategory(models.Model):
    #категория :
    # -- кошки
    # --ссобаки
    # -- грызуны
    #  -и т.д.
    class Meta:
        ordering = "pk",
        verbose_name_plural = 'Animal Categories'

    name = models.CharField(max_length=80)
    description = models.TextField(null=False, blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    class Meta:
        ordering = "pk",
        verbose_name_plural = 'Authors'

    username = models.CharField(max_length=80)
    name = models.CharField(max_length=130)
    description = models.TextField(null=False, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    class Meta:
        ordering = "pk",

    title = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    category = models.ForeignKey(AnimalCategory, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
