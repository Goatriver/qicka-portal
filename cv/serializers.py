from rest_framework import serializers
from cv import models


class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Socials
        fields = '__all__'


class BasicPublicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasicPublicInfo
        fields = '__all__'


class ProfessionalSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfessionalSkills
        fields = '__all__'


class LanguageSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LanguageSkills
        fields = '__all__'


class OtherInterestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtherInterests
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = '__all__'

