from django.contrib import admin


# Register your models here.
from .models import Menstrual
admin.site.register(Menstrual)

from .models import User
admin.site.register(User)
