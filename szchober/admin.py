from django.contrib import admin
from szchober.models import User, Rating, Feedback, Lift
# Register your models here.
admin.site.register(User)

admin.site.register(Rating)

admin.site.register(Feedback)
admin.site.register(Lift)