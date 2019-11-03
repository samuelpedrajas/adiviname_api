from django.contrib import admin
from django.utils.html import mark_safe

from .models import Expression, Game, GameClick, GameIcon, GameType

class ExpressionInline(admin.StackedInline):
    model = Expression
    extra = 30
    exclude = ["created_at", "updated_at", "creator"]


class GameTypeAdmin(admin.ModelAdmin):
	fields = ["name", "text"]
	list_display = ["name", "text"]


class GameClickAdmin(admin.ModelAdmin):
	fields = ["game_id", "num_clicks"]
	list_display = ["game_id", "num_clicks", "updated_at"]


class GameClickInline(admin.TabularInline):
    model = GameClick


class GameIconInline(admin.TabularInline):
    model = GameIcon
    fields = ["icon_preview", "file", "updated_at"]
    readonly_fields = ('icon_preview', 'updated_at',)

    def icon_preview(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url = obj.file.url,
                width = obj.file.width,
                height = obj.file.height,
            )
        )


class GameAdmin(admin.ModelAdmin):
    fields = ["id", 'title', "featured", "game_type", "description", "created_at", "updated_at", "image_updated_at", "expressions_updated_at", "creator"]
    list_display = ("id", 'title', "featured", "game_type", "created_at", "updated_at", "creator",)
    readonly_fields = ["id", "created_at", "updated_at", "image_updated_at", "expressions_updated_at", "creator"]
    inlines = [GameIconInline, GameClickInline, ExpressionInline]


class ExpressionAdmin(admin.ModelAdmin):
    fields = ['text', "created_at", "updated_at", "creator"]
    list_display = ('text', "created_at", "updated_at", "creator",)
    readonly_fields = ["created_at", "updated_at", "creator"]


admin.site.register(Game, GameAdmin)
admin.site.register(GameClick, GameClickAdmin)
admin.site.register(GameType, GameTypeAdmin)
admin.site.register(Expression, ExpressionAdmin)
