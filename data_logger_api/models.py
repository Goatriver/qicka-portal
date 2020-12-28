from django.db import models
from django.utils import timezone


# Create your models here.
class NodeSettings(models.Model):

    NODE_SETTINGS = [
        (10, "TEMP_FORWARD"),
        (11, "RANDOM_SETTING"),
        (12, "ALERT_TIME")
    ]

    setting = models.IntegerField(choices=NODE_SETTINGS)
    value = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Node settings"

    def __str__(self):
        return "{}: {}".format(self.get_setting_display(), self.value)


class Gateway(models.Model):
    UPDATE_INTERVAL_CHOICES = [
        (30, "30 seconds"),
        (60, "minute"),
        (90, "minute and a half"),
        (120, "two minutes"),
        (150, "two and a half minutes"),
        (180, "three minutes"),
        (210, "three and a half minutes")
    ]

    name = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=64, primary_key=True)
    update_interval_seconds = models.IntegerField(
        choices=UPDATE_INTERVAL_CHOICES,
        default=120
    )


class Node(models.Model):

    TYPE_CHOICES = [
            (0, 'ruuvi'),
            (1, 'qicka_sensor'),
            (2, 'qicka_clock'),
            (3, 'qicka_sleep_traffic_light')
        ]

    ACTIVATION_CHOICES = [
        (0, 'Activated'),
        (1, 'Not Activated'),
    ]

    # define fields
    name = models.CharField(max_length=64, blank=True, null=True)
    type = models.IntegerField(choices=TYPE_CHOICES)
    address = models.CharField(max_length=64, primary_key=True)
    settings = models.ManyToManyField(NodeSettings, blank=True)
    gateway = models.ForeignKey(Gateway, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.name, self.address)


class Data(models.Model):

    RESOLUTION_CHOICES = [
        (0, "real_time"),
        (10, "hour_avg"),
        (20, "day_avg")
    ]

    timestamp = models.DateTimeField(default=timezone.now, blank=True)
    resolution = models.IntegerField(choices=RESOLUTION_CHOICES, default=0)
    type = models.CharField(max_length=64)
    value = models.CharField(max_length=512)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)


class AlertRule(models.Model):

    ALERT_TYPES = [
        (10, "is less than"),  # convert to int/float
        (20, "is less or equal to"),  # convert to int/float
        (30, "is more than"),  # convert to int/float
        (40, "is more or equal to"),  # convert to int/float
        (50, "is equal to")  # do not convert
    ]

    type = models.IntegerField(choices=ALERT_TYPES)
    field = models.CharField(max_length=64)
    value = models.CharField(max_length=64)

    def __str__(self):
        return "{} {} {} ".format(self.field, self.get_type_display(), self.value)


class Alert(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    rules = models.ManyToManyField(AlertRule)


