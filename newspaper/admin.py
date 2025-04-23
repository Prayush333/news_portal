from django.contrib import admin
from newspaper.models import Advertisement, Category, Comment, Contact, Post, Tag,UserProfile,Newsletter

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Advertisement)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Newsletter)

