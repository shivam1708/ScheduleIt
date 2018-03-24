from django.contrib import admin
from app.models import UserProfileInfo, User,CouncilProfileInfo

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(CouncilProfileInfo)
