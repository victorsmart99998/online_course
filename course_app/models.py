from django.db import models
from django.db.models import Sum
from userauths.models import User

# Create your models here.

RATING = (
    (1, '⭐☆☆☆☆'),
    (2, '⭐⭐☆☆☆'),
    (3, '⭐⭐⭐☆☆'),
    (4, '⭐⭐⭐⭐☆'),
    (5, '⭐⭐⭐⭐⭐'),
)

class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='category/')

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Author(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='author/')
    bio = models.TextField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name


class Course(models.Model):
    STATUS = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='author/')
    video_link = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    descriptions = models.TextField(null=True, blank=True)
    price = models.IntegerField(default='0', null=True)
    discount = models.IntegerField(default='0', null=True)
    status = models.CharField(choices=STATUS, max_length=200, null=True)
    thumb_nail = models.ImageField(upload_to='author/', null=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def get_time_duration(self):
        time_duration = Video.objects.filter(course__id=self.id).aggregate(sum=Sum('time_duration'))
        return time_duration


def __str__(self):
        return self.name


class What_to_learn(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    points = models.CharField(max_length=700, null=True)

    def __str__(self):
        return self.points


class Requirements(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    points = models.CharField(max_length=700, null=True)

    def __str__(self):
        return self.points


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=700, null=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    serial_number = models.IntegerField(null=True)
    image = models.ImageField(upload_to='video/')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=700, null=True)
    youtube_id = models.CharField(max_length=700, null=True, blank=True)
    time_duration = models.IntegerField(null=True, blank=True)
    preview = models.BooleanField(default=False)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name


class User_course(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    paid = models.BooleanField(default=False)
    points = models.CharField(max_length=700, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.name


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.CharField(max_length=10, choices=RATING, default=1, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "product review"

    def __str__(self):
        return self.review


class NewsletterSubscribers(models.Model):
    email = models.CharField(max_length=700, null=True)

    def __str__(self):
        return self.email


class Payment(models.Model):
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user


class ShippingAddress(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
