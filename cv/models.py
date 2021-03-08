from django.db import models

# Create your models here.
LEVELS_RANGE = {
    (1, "FUNDAMENTAL_AWARNESS"),
    (2, "NOVICE"),
    (3, "INTERMEDIATE"),
    (4, "ADVANCED"),
    (5, "EXPERT"),
}

LANGUAGE_CHOICES = {
    ("en", "English"),
    ("fi", "Suomi"),
}


class BasicPublicInfo(models.Model):
    name = models.TextField()
    profession = models.TextField()
    location = models.TextField(blank=True, null=True)
    birthdate = models.DateTimeField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    description = models.TextField()
    language = models.CharField(max_length=2, default="fi", choices=LANGUAGE_CHOICES)


class Socials(models.Model):
    SERVICE_CHOICES = {
        ("FACE", "Facebook"),
        ("LINKEDIN", "LinkedIn"),
        ("GITHUB", "GitHub"),
        ("INSTA", "Instagram")
    }
    service = models.TextField(choices=SERVICE_CHOICES)
    url = models.URLField()
    name = models.TextField()
    language = models.CharField(max_length=2, default="fi", choices=LANGUAGE_CHOICES)


class Experience(models.Model):
    corporate = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    profession = models.TextField()
    description = models.TextField()
    link = models.URLField()
    language = models.CharField(max_length=2, default="fi", choices=LANGUAGE_CHOICES)


class Education(models.Model):
    facility_name = models.TextField()
    title = models.TextField()
    branch = models.TextField(blank=True, null=True)
    graduation_date = models.DateTimeField()
    rating_scale = models.TextField(blank=True, null=True)
    average_rating = models.TextField(blank=True, null=True)
    thesis = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=2, default="fi", choices=LANGUAGE_CHOICES)


class ProfessionalSkills(models.Model):
    name = models.TextField()
    level = models.IntegerField(choices=LEVELS_RANGE)


class LanguageSkills(models.Model):
    name = models.TextField()
    level = models.IntegerField(choices=LEVELS_RANGE)


class OtherInterests(models.Model):
    name = models.TextField()
    language = models.CharField(max_length=2, default="fi", choices=LANGUAGE_CHOICES)

