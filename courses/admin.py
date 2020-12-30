from django.contrib import admin
from courses.models import *



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
    
    
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
    
# Register your models here.
admin.site.register(Quiz)
admin.site.register(QuizProfile)
admin.site.register(Leadership_board)
admin.site.register(QuestionChoice)
admin.site.register(QuizQuestion)
