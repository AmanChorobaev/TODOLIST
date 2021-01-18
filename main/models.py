from django.db import models

# Create your models here.

class ToDo (models.Model):
  text = models.CharField(max_length=100)
  created_at=models.DateField(auto_now_add=True)
  is_closed = models.BooleanField(default=False) 
  is_favorite = models.BooleanField(default=False)
  
class Books (models.Model):
  name=models.CharField (max_length=100, db_index=True)
  title=models.CharField (max_length=180)
  subtitle=models.CharField (max_length=180)
  description=models.CharField (max_length=180)
  price=models.CharField (max_length=150)
  genre=models.CharField (max_length=150)
  author=models.CharField (max_length=150)
  year=models.CharField (max_length=150)
  date=models.CharField (max_length=150)

  
