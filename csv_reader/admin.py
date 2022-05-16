from django.contrib import admin

from .models import Answers, Question, User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "user_id", "name", "sex")
    search_fields = ("name",)
    list_filter = ("time_create",)
    empty_value_display = "-пусто-"


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("pk", "text_question")
    search_fields = ("text_question",)


class AnswersAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "question", "answer")
    search_fields = ("answer",)


admin.site.register(Question, QuestionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Answers, AnswersAdmin)
