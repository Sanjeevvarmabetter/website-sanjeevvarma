from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

#to create thumbnails
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.


STATUS = (
    (0,"Draft"),
    (1,"Publish")

)

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    updated_on  = models.DateTimeField(auto_now = True)
    # content = models.TextField()
    content = RichTextField()
    image = models.ImageField(upload_to="post_images")
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100,50)],
                                     format='JPEG',
                                     options={'quality':60})
    
    # thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
