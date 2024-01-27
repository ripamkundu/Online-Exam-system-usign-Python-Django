from django.contrib import admin

# Register your models here.
from.models import Question
class mocktestAdmin(admin.ModelAdmin):
    list_display=('q_id','question','option1','option2','option3','option4')
admin.site.register(Question,mocktestAdmin)

from.models import Question_s1
class mocktestAdmin(admin.ModelAdmin):
    list_display=('q_id','question','option1','option2','option3','option4')
admin.site.register(Question_s1,mocktestAdmin)
