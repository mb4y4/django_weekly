from django.contrib import admin
from .models import Food

# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'date_added', 'user')
    search_fields = ('name', 'user__username')  # Enable searching by name and user
    list_filter = ('user', 'date_added')  # Enable filtering by user and date_added

    def save_model(self, request, obj, form, change):
        """Override save_model to set the user based on the logged-in user."""
        if not change:  # If creating a new object
            obj.user = request.user
        obj.save()
