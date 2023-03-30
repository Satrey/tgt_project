from django.contrib import admin
from .models import Theme, Ticket, Question, Answer


class ThemeAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class TicketsInLine(admin.TabularInline):
    model = Question


class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'theme']
    list_filter = ('theme',)
    # inlines = [TicketsInLine]
    prepopulated_fields = {"slug": ("title",)}


class QuestionsInline(admin.StackedInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'theme']
    list_filter = ('theme',)
    inlines = [QuestionsInline]


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Question, QuestionAdmin)


