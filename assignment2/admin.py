from django.contrib import admin

# Register your models here.
from assignment2.models import User, UserProfile, Hobby


class HobbyAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Hobby,HobbyAdmin)
