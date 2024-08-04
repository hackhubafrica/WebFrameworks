from django.shortcuts import render
from django.http import HttpResponse
from . models import Article

# Create your views here.
'''
Each view is responsible for doing one of two things: Returning an HttpResponse object containing the content
for the requested page, or raising an exception such as Http404. The rest is up to you.

Generally, a view retrieves data according to the parameters, loads a template and renders the template with the
retrieved data.
'''
def index(request):
	return HttpResponse("Hello, world. You're at the news index.")


def year_archive(request, year):
	a_list = Article.objects.filter(pub_date__year=year)
	context = {'year': year, 'article_list': a_list}
	return render(request, 'news/year_archive.html', context)
