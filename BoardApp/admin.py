from django.contrib import admin
from BoardApp.models import *

# Register your models here.

admin.site.register([Post,Board])
