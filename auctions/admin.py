from django.contrib import admin
from .models import Listing, Bidding, Comment, User

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Bidding)

