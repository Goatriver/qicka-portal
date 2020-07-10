from rest_framework import serializers
from rest_framework_bulk import BulkSerializerMixin
from data_logger_api import models


class DataSerializer(BulkSerializerMixin, serializers.HyperlinkedModelSerializer):

    node = serializers.PrimaryKeyRelatedField(
        queryset=models.Node.objects.all()
    )

    class Meta:
        model = models.Data
        fields = ['type', 'value', 'node']


class GatewaySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Gateway
        fields = ['name', 'address', 'nodes', 'update_interval_seconds']


class NodeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Node
        fields = ['name', 'type', 'address', 'settings']


class NodeSettingsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.NodeSettings
        fields = ["setting", "value"]

