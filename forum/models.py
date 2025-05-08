from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    # Ensures that thread categories are displayed by their names (instead of IDs) in admin
    def __str__(self):
        return self.name

    # ThreadCategory alphabetically/ascending order by name
    class Meta:
        ordering = ['name']
        verbose_name = "Thread Category"
        verbose_name_plural = "Thread Categories" 

class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='threads')
    category = models.ForeignKey(ThreadCategory, null=True, on_delete=models.SET_NULL, related_name='threads')
    entry = models.TextField()
    image = models.ImageField(upload_to='thread_images/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum_detail', args=[str(self.id)])

    # Descending order by date
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Thread"
        verbose_name_plural = "Threads" 

class Comment(models.Model):
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='comments')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.author:
            return self.author.display_name
        else:
            return "Deleted User"

    # Ascending order by date
    class Meta:
        ordering = ['created_on']
        verbose_name = "Comment"
        verbose_name_plural = "Comments" 