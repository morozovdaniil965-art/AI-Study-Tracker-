from django.contrib import admin
from .models import FieldOfStudy, Topic
# Register your models here.


admin.site.register( FieldOfStudy )


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'field_of_study', 'is_completed')
    list_filter = ('is_completed', 'field_of_study')
    search_fields = ('title', 'field_of_study__title')
