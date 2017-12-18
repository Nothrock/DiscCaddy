from django.contrib import admin
from pages.models import User, CheckIn, Comment, Course, Hazard, Hi_Five, Hole, CheckInComment, Friend, Disc

# Register your models here.
admin.site.register(User)

admin.site.register(CheckIn)

admin.site.register(Comment)

admin.site.register(Course)

admin.site.register(Hazard)

admin.site.register(Hi_Five)

admin.site.register(Hole)

admin.site.register(CheckInComment)

admin.site.register(Friend)

admin.site.register(Disc)
