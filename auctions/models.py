from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Topic(models.Model):
    d = models.AutoField(primary_key=True)


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    start_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(default="https://static.thenounproject.com/png/1211233-200.png")
    isActive = models.BooleanField(default=True)
    category = models.CharField(max_length=64)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return f"{self.title}: by {self.seller.username}."

class Bidding(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE,)
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    bid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} bid on {self.listing.title} by {self.bidder.username}."

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.listing.title} by {self.user.username} is posted."

    
