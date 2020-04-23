from django.db import models
import datetime
# Create your models here.
# title
# publish date
# image 
# body

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    publish_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')
    body = models.TextField()

    def summary(self):
        return self.body[:100]
    
    def publish_date_pretty(self):
        return self.publish_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title