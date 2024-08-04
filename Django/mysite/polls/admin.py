from django.contrib import admin
from .models import Question ,Choice
# Register your models here.
#Make the poll app modifiable in the admin

#Now that we’ve registered Question, Django knows that it should be displayed on the admin index page
admin.site.register(Choice)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['question_text']}),
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)
