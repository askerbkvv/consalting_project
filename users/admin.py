from django.contrib import admin

from .models import Form, Comment, University, Admin

admin.site.register(Form)
admin.site.register(Admin)
admin.site.register(Comment)
admin.site.register(University)
