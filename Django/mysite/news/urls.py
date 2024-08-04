#created on 3rd August 2024
#created by @HackHubAfrica
#Design your URLs
"""
A clean, elegant URL scheme is an important detail in a high-quality Web application. Django encourages beautiful
URL design and doesn’t put any cruft in URLs, like .php or .asp.
To design URLs for an app, you create a Python module called a URLconf . A table of contents for your app, it contains
a mapping between URL patterns and Python callback functions. URLconfs also serve to decouple URLs from Python
code.
"""
from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('articles/<int:year>/', views.year_archive),
#path('articles/<int:year>/<int:month>/', views.month_archive),
#path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]



"""
The code above maps URL paths to Python callback functions (“views”). The path strings use parameter tags to
“capture” values from the URLs. When a user requests a page, Django runs through each path, in order, and stops at
the first one that matches the requested URL. (If none of them matches, Django calls a special-case 404 view.) This is
blazingly fast, because the paths are compiled into regular expressions at load time.
"""
