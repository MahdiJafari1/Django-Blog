from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
class Author(models.Model):
    """Model definition for Author."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    class Meta:
        """Meta definition for Author."""

        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        """Unicode representation of Author."""
        return self.first_name + ' ' + self.last_name

class Post(models.Model):
    """Model definition for Post."""

    title = models.CharField(max_length=100)
    excerpt = models.TextField()
    image = models.ImageField(upload_to='posts')
    date = models.DateField(auto_now=True, )
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    content = models.TextField(max_length=10000, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField('Tag')

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.title 
    
class Tag(models.Model):
    """Model definition for Tag."""

    caption = models.CharField(max_length=100)
    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.caption

class Comment(models.Model):
    """Model definition for Comment."""

    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=254)
    text = models.TextField(max_length=400, validators=[MinLengthValidator(10), MaxLengthValidator(400)])
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Comment."""
        return self.user_name + ': ' + self.text[:20]
