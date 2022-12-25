from django.contrib import admin
from .models import ToDo
from .models import ToMeet
from .models import Habits


admin.site.register(ToDo)
admin.site.register(ToMeet)
admin.site.register(Habits)


# Register your models here.
