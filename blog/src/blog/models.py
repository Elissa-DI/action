from django.db import models
from django.contrib.auth.models import User

class CreateUpdateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        
STATUS_CHOICES = (
    ('Draft', 'Draft'),
    ("Publish", "Publish"),
    ("Archive", "Archive")
)
class Post(CreateUpdateModel):
    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=120, unique=True)
    content = models.TextField()
    status = models.CharField(max_length=10, default='Draft', choices=STATUS_CHOICES)
    hero_image = models.ImageField(upload_to='post', default="post/sample.jpg")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.title
    
class Comment(CreateUpdateModel):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    is_comment_approved = models.BooleanField(default=False)

