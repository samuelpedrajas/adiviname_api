from django.contrib import admin

from .models import Expression, Game, GameClick, GameType

class ExpressionInline(admin.StackedInline):
    model = Expression
    extra = 30
    exclude = ["created_at", "updated_at", "creator"]


class GameTypeAdmin(admin.ModelAdmin):
	fields = ["name", "text"]
	list_display = ["name", "text"]


class GameClickAdmin(admin.ModelAdmin):
	fields = ["game_id", "num_clicks", "updated_at"]
	list_display = ["game_id", "num_clicks", "updated_at"]


class GameClickInline(admin.TabularInline):
    model = GameClick


class GameAdmin(admin.ModelAdmin):
    fields = ["id", 'title', 'description', "game_type", "created_at", "updated_at", "creator"]
    list_display = ("id", 'title', 'description', "created_at", "updated_at", "creator",)
    readonly_fields = ["id", "created_at", "updated_at", "creator"]
    inlines = [GameClickInline, ExpressionInline]


class ExpressionAdmin(admin.ModelAdmin):
    fields = ['text', "created_at", "updated_at", "creator"]
    list_display = ('text', "created_at", "updated_at", "creator",)
    readonly_fields = ["created_at", "updated_at", "creator"]


admin.site.register(Game, GameAdmin)
admin.site.register(GameClick, GameClickAdmin)
admin.site.register(GameType, GameTypeAdmin)
admin.site.register(Expression, ExpressionAdmin)
