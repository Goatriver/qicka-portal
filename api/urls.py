from rest_framework_bulk.routes import BulkRouter
from data_logger import views as data_logger_views


router = BulkRouter()
router.register(r'data-logger/data', data_logger_views.DataViewSet)
router.register(r'data-logger/gateway', data_logger_views.GatewayViewSet)
router.register(r'data-logger/node', data_logger_views.NodeViewSet)
router.register(r'data-logger/node-settings', data_logger_views.NodeSettingViewSet)


