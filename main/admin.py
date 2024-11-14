from django.contrib import admin

from main.models import Tutorial

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    
    fieldsets=[
        ("Title", {"fields": ["tutorial_title"]}),
        ("Content", {"fields":["tutorial_content"]}),
        ("date", {"fields": ["tutorial_published"]})
    ]
    list_display= ['tutorial_published', 'tutorial_title', 'tutorial_content']
admin.site.register(Tutorial, TutorialAdmin)
