from django.contrib import admin

# Register your models here.
from .models import Room
from .models import Message
from .models import UserProfile


admin.site.register(Message)
admin.site.register(UserProfile)
admin.site.register(Room)