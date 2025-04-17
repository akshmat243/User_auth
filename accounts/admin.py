from django.contrib import admin
from .models import UserProfile, SlideCarousel, TeamMember, WebServices

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(SlideCarousel)
admin.site.register(TeamMember)
admin.site.register(WebServices)