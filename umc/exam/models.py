from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200 , null=True)
    author = models.CharField(max_length=200 , null=True)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=200 , decimal_places=2)
    cover_page = models.ImageField(upload_to='images' , blank = True ,null = True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="images" , blank = True , null=True)

    def __str__(self):
        return self.title