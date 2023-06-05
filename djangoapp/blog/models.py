from django.db import models
from utils.rands import slugify_new


class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=12,)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=17,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=30,)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=35,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Page(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    title = models.CharField(max_length=65,)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=70
    )
    is_published = models.BooleanField(
        default=False, help_text=(
            'This field must be checked in order for the'
            'page to be publicly displayed.'
        )
    )
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
