from rest_framework.viewsets import ModelViewSet
from cv import models
from cv import serializers


# Create your views here.
class SocialsViewSet(ModelViewSet):

    queryset = models.Socials.objects.all()
    serializer_class = serializers.SocialsSerializer


class BasicPublicInfoViewSet(ModelViewSet):

    queryset = models.BasicPublicInfo.objects.all()
    serializer_class = serializers.BasicPublicInfoSerializer

    def get_queryset(self):
        queryset = models.BasicPublicInfo.objects.all()
        lan = self.request.query_params.get('lan', 'fi')
        return queryset.filter(language=lan)


class ProfessionalSkillsViewSet(ModelViewSet):

    queryset = models.ProfessionalSkills.objects.all().order_by('-level')
    serializer_class = serializers.ProfessionalSkillsSerializer


class LanguageSkillsViewSet(ModelViewSet):

    queryset = models.LanguageSkills.objects.all().order_by('-level')
    serializer_class = serializers.LanguageSkillsSerializer


class OtherInterestsViewSet(ModelViewSet):

    queryset = models.OtherInterests.objects.all()
    serializer_class = serializers.OtherInterestsSerializer

    def get_queryset(self):
        queryset = models.OtherInterests.objects.all()
        lan = self.request.query_params.get('lan', 'fi')
        return queryset.filter(language=lan)


class ExperienceViewSet(ModelViewSet):
    queryset = models.Experience.objects.all().order_by('-end_date')
    serializer_class = serializers.ExperienceSerializer

    def get_queryset(self):
        queryset = models.Experience.objects.all().order_by('-end_date')
        lan = self.request.query_params.get('lan', 'fi')
        return queryset.filter(language=lan)


class EducationViewSet(ModelViewSet):
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer

    def get_queryset(self):
        queryset = models.Education.objects.all()
        lan = self.request.query_params.get('lan', 'fi')
        return queryset.filter(language=lan)
