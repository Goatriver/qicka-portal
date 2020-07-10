from rest_framework_bulk.routes import BulkRouter
from data_logger_api import views


router = BulkRouter()
router.register(r'data', views.DataViewSet)
router.register(r'gateway', views.GatewayViewSet)
router.register(r'node', views.NodeViewSet)
router.register(r'node-settings', views.NodeSettingViewSet)


