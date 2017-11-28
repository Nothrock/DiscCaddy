from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class User(AbstractUser):
    city = models.CharField(max_length=255, null=True, blank=True)
    age = models.CharField(max_length=3, null=True, blank=True)
    bio = models.TextField()
    pdga_member = models.BooleanField(default=False)
    pdga_number = models.CharField(max_length=8, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)

class Course(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    number_of_holes = models.CharField(max_length=2, null=False, blank=False)
    par_for_course = models.CharField(max_length=3, null=False, blank=False)
    course_length = models.CharField(max_length=255, null=False, blank=False)
    course_description = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name[:50])
        super(Course, self).save(*args, **kwargs)


class Hole(models.Model):
    hole_number = models.CharField(max_length=3, null=False, blank=False)
    par_for_hole = models.CharField(max_length=2, null=False, blank=False)
    hole_length = models.CharField(max_length=255, null=False, blank=False)
    course = models.ForeignKey('Course', related_name='holes')

    def __str__(self):
        return self.hole_number


class Hazard(models.Model):
    hazard_description = models.TextField()
    hole = models.ForeignKey('Hole', related_name='hazards')
    user = models.ForeignKey(User, related_name='my_hazards')


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='comments')


class Hi_Five(models.Model):
    hi_five_er = models.ForeignKey(User, related_name='fives_given')
    hi_five_ee = models.ForeignKey(User, related_name='fives_received')
    check_in = models.ForeignKey('CheckIn', related_name='hi_fives')



class CheckIn(models.Model):
    user = models.ForeignKey(User, related_name='my_check_in')
    check_in_time = models.DateTimeField(auto_now_add=True)
    hole_number = models.ForeignKey('Hole', related_name='check_ins')
    user_comment = models.TextField(null=True, blank=True)
    hole_rating = models.IntegerField(null=True, blank=True)
    user_score = models.CharField(max_length=3, null=True, blank=True)

    class Meta:
        ordering = ['-check_in_time']


class CheckInImage(models.Model):
    img = models.ImageField()
    check_in = models.ForeignKey('CheckIn', related_name='images')


class CheckInComment(models.Model):
    comment = models.ForeignKey('Comment')
    check_in = models.ForeignKey('CheckIn', related_name='comments')


class Friend(models.Model):
    requestor = models.ForeignKey(User, related_name='requests_sent')
    requestee = models.ForeignKey(User, related_name='requests_received')
    accepted = models.NullBooleanField(default=None, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Disc(models.Model):
    brand = models.CharField(max_length=255, null=True, blank=True)
    disc = models.CharField(max_length=255, null=True, blank=True)
    plastic = models.CharField(max_length=255, null=True, blank=True)
    weight = models.CharField(max_length=7, null=True, blank=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.brand, self.plastic, self.disc, self.weight)


class News(models.Model):
    updates = models.CharField(max_length=999, null=False, blank=False)
    coming_soon = models.CharField(max_length=999, null=False, blank=False)