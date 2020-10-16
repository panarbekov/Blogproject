from django.contrib import admin
from core.models import Article, Profile

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = [ "title", "views", 
    "publicated", "author",
    "created_date", "updated_date"]
    list_display_links = ["title", ]
    list_editable = ["publicated"]
    ordering = ["-views"]
    list_filter = ("publicated","author",
     "created_date" )
    fields = ["title", "text", 
    "created_date", "updated_date"]
    readonly_fields = ["created_date", 
    "updated_date"]
    list_per_page = 2
    search_fields = [
    "text", "title", "author__username", 
    "author__first_name", "author__last_name"
    ]
    
admin.site.register(Article, ArticleAdmin)


admin.site.register(Profile)

# Register your models here.
