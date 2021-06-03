from django.contrib import admin

from blog.models import Album, Photo, Comment, Bookmark

admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Bookmark)
