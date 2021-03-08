from rest_framework_bulk.routes import BulkRouter
from data_logger import views as data_logger_views
from cv import views as cv_views

router = BulkRouter()
router.register(r'data-logger/data', data_logger_views.DataViewSet)
router.register(r'data-logger/gateway', data_logger_views.GatewayViewSet)
router.register(r'data-logger/node', data_logger_views.NodeViewSet)
router.register(r'data-logger/node-settings', data_logger_views.NodeSettingViewSet)
router.register(r'cv/socials', cv_views.SocialsViewSet)
router.register(r'cv/public-info', cv_views.BasicPublicInfoViewSet)
router.register(r'cv/professional-skills', cv_views.ProfessionalSkillsViewSet)
router.register(r'cv/language-skills', cv_views.LanguageSkillsViewSet)
router.register(r'cv/other-interests', cv_views.OtherInterestsViewSet)
router.register(r'cv/experience', cv_views.ExperienceViewSet)
router.register(r'cv/education', cv_views.EducationViewSet)
