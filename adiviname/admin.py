from django.contrib import admin

from .models import Game, Expression

class ExpressionInline(admin.StackedInline):
    model = Expression
    extra = 30
    exclude = ["created_at", "updated_at", "creator"]


class GameAdmin(admin.ModelAdmin):
    fields = ['title', 'description', "created_at", "updated_at", "creator"]
    list_display = ('title', 'description', "created_at", "updated_at", "creator",)
    readonly_fields = ["created_at", "updated_at", "creator"]
    inlines = [ExpressionInline]


class ExpressionAdmin(admin.ModelAdmin):
    fields = ['text', "created_at", "updated_at", "creator"]
    list_display = ('text', "created_at", "updated_at", "creator",)
    readonly_fields = ["created_at", "updated_at", "creator"]


admin.site.register(Game, GameAdmin)
admin.site.register(Expression, ExpressionAdmin)
