from django.contrib import admin
from data_logger_api import models
from django.contrib.admin import register
# Register your models here.


@register(models.Node)
class NodeAdminPage(admin.ModelAdmin):
    model = models.Node
    list_display = ['address', 'name']


@register(models.Data)
class DataAdminPage(admin.ModelAdmin):
    model = models.Data
    list_display = ['timestamp', 'node', 'type', 'value', 'resolution']
    list_filter = ['resolution', 'type', 'node']


@register(models.NodeSettings)
class NodeSettingsAdminPage(admin.ModelAdmin):
    model = models.Data
    list_display = ["setting", "value", "nodes"]

    def nodes(self, obj):
        return ",".join([k.name for k in obj.node_set.all()])


admin.site.register(models.Gateway)
admin.site.register(models.Alert)
admin.site.register(models.AlertRule)







