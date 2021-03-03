from rest_framework import serializers
from rest_framework_bulk import BulkSerializerMixin
from data_logger import models


class DataSerializer(BulkSerializerMixin, serializers.ModelSerializer):

    node = serializers.PrimaryKeyRelatedField(
        queryset=models.Node.objects.all()
    )

    class Meta:
        model = models.Data
        fields = ['type', 'value', 'node']


class NodeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Node
        fields = ['name', 'type', 'address', 'settings', 'gateway']


class GatewaySerializer(serializers.HyperlinkedModelSerializer):

    nodes = NodeSerializer(required=False, many=True, source='node_set')

    class Meta:
        model = models.Gateway
        fields = ['name', 'address', 'nodes', 'update_interval_seconds']


class NodeSettingsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.NodeSettings
        fields = ["setting", "value"]

