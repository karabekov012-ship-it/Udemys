from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField()
    StausChoiceRole = (
        ('student', 'student'),
        ('teacher', 'teacher')
    )
    status = models.CharField(max_length=64, choices=StausChoiceRole, default='student')
    date_register = models.DateField(auto_now_add=True)


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.subcategory_name


class Level(models.Model):
    LevelChoices = (
        ('elementary', 'elementary'),
        ('average', 'average'),
        ('advanced', 'advanced')
    )
    level = models.CharField(max_length=32, choices=LevelChoices)

    def __str__(self):
        return self.level


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='courses')
    level = models.ManyToManyField(Level)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.course_name}, {self.created_by}'

    def get_avg_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum([i.rating for i in reviews]) / reviews.count(), 1)

    def get_count_people(self):
        reviews = self.reviews.all()
        return reviews.count()


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField()
    content = models.FileField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title


class AssignMent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    students = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Exam(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self):
        return self.title


class Questions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='quests')
    question_name = models.CharField(max_length=64)
    score = models.PositiveSmallIntegerField(choices=[(i, str(i))for i in range(1, 6)])

    def __str__(self):
        return self.question_name


class Option(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='options')
    option_name = models.CharField(max_length=64)
    option_type = models.BooleanField()

    def __str__(self):
        return self.option_name


class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField()
    certificate_url = models.FileField()


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i))for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f'{self.user}, {self.comment}'