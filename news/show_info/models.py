from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField('Category name', max_length=255)

    def __str__(self):
        return self.name


class New(models.Model):
    title = models.CharField('Title', max_length=255)
    text = models.TextField('Text')
    photo = models.ImageField('Photo', upload_to='news/%Y/%m/%d/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Category')
    date = models.DateField('Date', auto_now_add=True)
    slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.title, self.date)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify('{}-{}'.format(self.title, self.category.name))
        super(New, self).save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse('show_post', kwargs={'post_slug': self.slug})
