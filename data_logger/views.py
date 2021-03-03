from rest_framework_bulk import BulkModelViewSet
from rest_framework.viewsets import ModelViewSet
from data_logger import serializers
from data_logger import models


# Data logger DRF-endpoints
class DataViewSet(BulkModelViewSet):

    serializer_class = serializers.DataSerializer
    queryset = models.Data.objects.all().order_by("-timestamp")


class GatewayViewSet(ModelViewSet):

    queryset = models.Gateway.objects.all()
    serializer_class = serializers.GatewaySerializer


class NodeViewSet(ModelViewSet):

    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSerializer


class NodeSettingViewSet(ModelViewSet):

    queryset = models.NodeSettings.objects.all()
    serializer_class = serializers.NodeSettingsSerializer
