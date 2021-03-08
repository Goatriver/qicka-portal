from django.contrib import admin
from cv import models
from django.contrib.admin import register


@register(models.BasicPublicInfo)
class BasicPublicInfoAdminPage(admin.ModelAdmin):
    model = models.BasicPublicInfo


@register(models.Socials)
class SocialsAdminPage(admin.ModelAdmin):
    model = models.Socials


@register(models.Experience)
class ExperienceAdminPage(admin.ModelAdmin):
    model = models.Experience


@register(models.Education)
class EducationAdminPage(admin.ModelAdmin):
    model = models.Education


@register(models.ProfessionalSkills)
class ProfessionalSkills(admin.ModelAdmin):
    model = models.ProfessionalSkills


@register(models.LanguageSkills)
class LanguageSkillsAdminPage(admin.ModelAdmin):
    model = models.LanguageSkills


@register(models.OtherInterests)
class OtherInterestsAdminPage(admin.ModelAdmin):
    model = models.OtherInterests
