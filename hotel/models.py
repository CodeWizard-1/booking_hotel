from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class City(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.city_name


class Hotel (models.Model):
    hotel_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description_hotel = models.TextField()
    hotel_image = CloudinaryField('image', default='plaseholder')
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.hotel_name


class Facilities(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    room_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_booked = models.BooleanField(default=False)
    capacity = models.IntegerField()
    description_room = models.TextField()
    room_image = CloudinaryField('image', default='plaseholder')
    facilities = models.ManyToManyField(Facilities, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='room_likes', blank=True)

    def __str__(self) -> str:
        return self.room_name

    def number_of_likes(self):
        return self.likes.count()


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Customer(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='customers')

    def __str__(self):
        return self.customer


class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    checking_date = models.DateTimeField(blank=True, null=True)
    checkout_date = models.DateTimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=14, null=True)
    email = models.EmailField()
    is_cancelled = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    people_count = models.PositiveIntegerField(default=1)
    children_count = models.PositiveIntegerField(default=0)
    children_ages = models.CharField(max_length=255, null=True, blank=True)
    child_bed = models.BooleanField(default=False)
    playroom_services = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.hotel = self.room.hotel
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return self.customer.username


class CheckIn(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.room.slug


class CheckOut(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    check_out_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer


class Guest_reviews(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name="rooms")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.name}"
