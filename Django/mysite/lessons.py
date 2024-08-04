#VIEWS.PY
from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Question ,Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# Create your views here.
#This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {'latest_question_list': latest_question_list,}
	#return HttpResponse(template.render(context, request))
	return render(request, 'polls/index.html', context)

	"""
	A shortcut: render()
	It’s a very common idiom to load a template, fill a context and return an HttpResponse object with the result of the
	rendered template. Django provides a shortcut , the render() 
	The render() function takes the request object as its first argument, a template name as its second argument and a
	dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with
	the given context.

	"""

"""
That code loads the template called polls/index.html and passes it a context. The context is a dictionary
mapping template variable names to Python objects

There’s a problem here with the first approach, though: the page’s design is hard-coded in the view. If you want to change the way the page
looks, you’ll have to edit this Python code. So let’s use Django’s template system to separate the design from Python
by creating a template that the view can use.
	#latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output = ', '.join([q.question_text for q in latest_question_list])
	#return HttpResponse(output)
	

"""

"""
A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific
template. For example, in a blog application, you might have the following views:
• Blog homepage – displays the latest few entries.
• Entry “detail” page – permalink page for a single entry.
• Year-based archive page – displays all months with entries in the given year.
• Month-based archive page – displays all days with entries in the given month.
• Day-based archive page – displays all entries in the given day.
• Comment action – handles posting comments to a given entry.
In our poll application, we’ll have the following four views:
• Question “index” page – displays the latest few questions.
• Question “detail” page – displays a question text, with no results but with a form to vote.
• Question “results” page – displays results for a particular question.
• Vote action – handles voting for a particular choice in a particular question.

"""
def detail(request, question_id):
	'''
	# Raising a 404 error
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})
	'''
	#return HttpResponse("You're looking at question %s." % question_id)

	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

	"""
	#A shortcut: get_object_or_404()
	It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. Django provides a shortcut
	The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of
	keyword arguments, which it passes to the get() function of the model’s manager. It raises Http404 if the object
	doesn’t exist
	"""

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
		'question': question,
		'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

	#return HttpResponse("You're voting on question %s." % question_id)
"""db.sqlite3"""

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})
	
	#response = "You're looking at the results of question %s."
	#return HttpResponse(response % question_id)


"""
Your view can read records from a database, or not. It can use a template system such as Django’s – or a third-party
Python template system – or not. It can generate a PDF file, output XML, create a ZIP file on the fly, anything you
want, using whatever Python libraries you want.

"""




















































#MODELS.PY

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
'''
A model is the single, definitive source of truth about your data. It contains the essential fields and behaviors of
the data you’re storing. Django follows the DRY Principle. The goal is to define your data model in one place and
automatically derive things from it.
'''
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):									
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text


def was_published_recently(self):
	now = timezone.now()
	return now - datetime.timedelta(days=1) <= self.pub_date <= now
'''
Wait a minute. <Question: Question object (1)> isn’t a helpful representation of this object. Let’s fix
that by editing the Question model (in the polls/models.py file) and adding a __str__() method to both
Question and Choice:

It’s important to add __str__() methods to your models, not only for your own convenience when dealing with the
interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated
admin.
'''





"""
Here, each model is represented by a class that subclasses django.db.models.Model. Each model has a number
of class variables, each of which represents a database field in the model.

Each field is represented by an instance of a Field class – e.g., CharField for character fields and
DateTimeField for datetimes. This tells Django what type of data each field holds.
"""



"""
#python manage.py makemigrations polls

By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case,
you’ve made new ones) and that you’d like the changes to be stored as a migration.
Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You
can read the migration for your new model if you like; it’s the file polls/migrations/0001_initial.py.
Don’t worry, you’re not expected to read them every time Django makes one, but they’re designed to be human-editable
in case you want to manually tweak how Django changes things.

There’s a command that will run the migrations for you and manage your database schema automatically - that’s
called migrate, and we’ll come to it in a moment - but first, let’s see what SQL that migration would run. The
sqlmigrate command takes migration names and returns their SQL:

• Change your models (in models.py).
• Run python manage.py makemigrations to create migrations for those changes
• Run python manage.py migrate to apply those changes to the database.
The reason that there are separate commands to make and apply migrations is because you’ll commit migrations to
your version control system and ship them with your app; they not only make your development easier, they’re also
usable by other developers and in production.
Read the django-admin documentation for full information on what the manage.py utility can do.

"""
