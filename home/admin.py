from django.contrib import admin
from . models import event,feedback,comment

# Register your models here.

admin.site.register(event)
admin.site.register(feedback)
admin.site.register(comment)
