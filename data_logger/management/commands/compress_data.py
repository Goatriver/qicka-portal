from django.core.management.base import BaseCommand, CommandError
from data_logger.models import Data, Node
from datetime import datetime, timedelta
import pytz
from django.conf import settings
import logging


logger = logging.getLogger('django.' + __name__)


class Command(BaseCommand):
    help = 'Compresses data entries in db by counting an average based on resolution'

    def handle(self, *args, **options):
        # convert older than one month in hourly average
        # convert older than six months in 12 hour average
        # convert older than one year into daily average
        nodes = Node.objects.all()
        for node in nodes:
            self.convert_to_next_resolution(node, 0)
            self.convert_to_next_resolution(node, 10)
            self.convert_to_next_resolution(node, 20)

    def convert_to_next_resolution(self, node, resolution):
        logger.info("node name/address = {}/{}, Converting from resolution {}".format(node.name,node.address, resolution))
        skip_days, resolution_time_delta = self.get_skip_days_and_resolution_time_delta(resolution)
        older_than = datetime.now(tz=pytz.timezone(settings.TIME_ZONE)) - timedelta(days=skip_days)
        logger.info("converting older than {}".format(str(older_than)))
        node_datas = Data.objects.filter(
            timestamp__lte=older_than) \
            .filter(node__address=node.address) \
            .filter(resolution=resolution).order_by('timestamp')
        try:
            logger.info("data count = {}".format(len(node_datas)))
            start = node_datas[0].timestamp
            end = start + resolution_time_delta

        except IndexError:
            return

        while start < older_than:
            compress_data = node_datas.filter(timestamp__gte=start, timestamp__lte=end)
            averages = self.count_averages(compress_data)
            if not averages:
                start += resolution_time_delta
                end = start + resolution_time_delta
                continue
            logger.info(averages)
            for key, value in averages.items():
                new_data = Data.objects.create(
                    timestamp=compress_data[0].timestamp,
                    resolution=resolution + 10,
                    type=key,
                    value=value['average'],
                    node=node
                )
                if not new_data:
                    self.stdout.write("New data not created for node {}/{} with key {}".format(
                        node.name, node.address, key
                    ), self.style.ERROR)
                else:
                    self.stdout.write("Created new data with next resolution: {}".format(new_data), self.style.SUCCESS)

            deleted, row_count = compress_data.delete()
            if deleted:
                logger.info("compressed {} rows from node {}".format(row_count['data_logger.Data'], node.name))
                self.stdout.write("compressed {} rows from resolution {} to resolution {} from node {}/{}".format(
                    row_count['data_logger.Data'],
                    resolution,
                    resolution + 10,
                    node.name,
                    node.address
                ), self.style.SUCCESS
                )

            start += resolution_time_delta
            end = start + resolution_time_delta

    @staticmethod
    def count_averages(node_datas):
        logger.info(node_datas)
        data_averages = {}
        for node_data in node_datas:
            try:
                data_value = float(node_data.value)
            except ValueError:
                continue

            try:
                data_averages[node_data.type]['count'] += 1.0
                data_averages[node_data.type]['sum'] += data_value
                data_averages[node_data.type]['average'] = \
                    data_averages[node_data.type]['sum'] / data_averages[node_data.type]['count']
            except KeyError:
                data_averages[node_data.type] = {
                    'count': 1.0,
                    'sum': float(node_data.value),
                    'average': float(node_data.value)
                }

        return data_averages

    @staticmethod
    def get_skip_days_and_resolution_time_delta(resolution):
        skip_days = 30
        resolution_time_delta = timedelta(hours=1)
        if resolution == 10:
            skip_days = 180
            resolution_time_delta = timedelta(hours=12)
        elif resolution == 20:
            skip_days = 365
            resolution_time_delta = timedelta(hours=24)
        return skip_days, resolution_time_delta

