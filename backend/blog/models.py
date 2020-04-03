from django.contrib.auth import get_user_model
from django.db import models
from autoslug import AutoSlugField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

User = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=250, null=False, help_text='Post title', default=None)
    slug = AutoSlugField(populate_from='title', unique=True, null=False, default=None)
    description = models.TextField(null=True, blank=True)
    post_image = ProcessedImageField(upload_to='post-images', null=True, default=None, blank=True,
                                     processors=[ResizeToFill(1280, 720)],
                                     format='JPEG',
                                     options={'quality': 100})

    post_thumbnail = ProcessedImageField(upload_to='post-images/thumbnails', null=True, default=None, blank=True,
                                         processors=[ResizeToFill(320, 240)],
                                         format='JPEG',
                                         options={'quality': 100})
    tags = models.ManyToManyField(
        'blog.PostTag',
        default=None,
        blank=True,
    )

    author = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        default=None,
        null=False,
        related_name='post_author'
    )

    category = models.ForeignKey(
        'blog.PostCategory',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        related_name='post_category'
    )

    sub_category = models.ForeignKey(
        'blog.PostSubCategory',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name='post_sub_category'
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return u'%s' % self.title

    def __init__(self, *args, **kwargs):
        super(BlogPost, self).__init__(*args, **kwargs)
        self.__original_post_image = self.post_image

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):

        if self.post_image and self.post_image != self.__original_post_image:
            self.post_thumbnail = self.post_image.file
        # elif self.__original_cover_image == "":
        #     self.cover_image_thumbnail = None

        super(BlogPost, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class PostCategory(models.Model):
    name = models.CharField(max_length=120, null=False, default=None)
    slug = AutoSlugField(populate_from='name', unique=True, null=False, default=None)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class PostSubCategory(models.Model):
    name = models.CharField(max_length=120, null=False, default=None)
    slug = AutoSlugField(populate_from='name', unique=True, null=False, default=None)

    parent = models.ForeignKey(
        'blog.PostCategory',
        on_delete=models.CASCADE,
        default=None,
        null=False,
        related_name='subcategory_parent'
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'


class PostTag(models.Model):
    tag = models.CharField(max_length=120, null=False, default=None)
    slug = AutoSlugField(populate_from='tag', unique=True, null=False, default=None)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return u'%s' % self.tag

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

