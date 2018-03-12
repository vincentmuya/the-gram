from django.contrib import admin
from .models import Editor,Post,Comments

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    filter_horizontal =()

admin.site.register(Editor)
admin.site.register(Post,PostAdmin)
admin.site.register(Comments)
