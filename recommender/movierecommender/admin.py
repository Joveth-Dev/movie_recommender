from django.contrib import admin

# Register your models here.

from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    actions = ["mark_as_watched"]
    fields = ["imdb_id", "genres", "original_title", "overview", "watched"]
    list_display = ("original_title", "genres", "release_date", "watched")
    search_fields = ["original_title", "overview"]

    @admin.action(description="Mark selected as Watched")
    def mark_as_watched(self, request, queryset):
        updated_count = queryset.update(watched=True)
        self.message_user(
            request,
            f"{updated_count} were successfully marked as watched.",
            "success",
        )


admin.site.register(Movie, MovieAdmin)
