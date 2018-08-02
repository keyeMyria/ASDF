from django.contrib import admin

from home.models import Post,Comment,Addlikes

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Addlikes)
