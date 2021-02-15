from django.contrib import admin

# Register your models here.
from .models import Stolica, Drvo, User

admin.site.register(Stolica)
admin.site.register(Drvo)
admin.site.register(User)