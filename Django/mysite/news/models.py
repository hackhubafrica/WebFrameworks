from django.db import models

# Create your models here.
#Although you can use Django without a database, it comes with an object-relational mapper in which you describe your database layout in Python code.

class Reporter(models.Model):
	full_name = models.CharField(max_length=70)
	def __str__(self):
		return self.full_name

class Article(models.Model):
	pub_date = models.DateField()
	headline = models.CharField(max_length=200)
	content = models.TextField()
	reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
	def __str__(self):
		return self.headline

"""
Next, run the Django command-line utilities to create the database tables automatically:
$ python manage.py makemigrations
$ python manage.py migrate
The makemigrations command looks at all your available models and creates migrations for whichever tables
don’t already exist. migrate runs the migrations and creates tables in your database, as well as optionally providing
much richer schema control.

"""
