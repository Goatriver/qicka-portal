from django.core.management.base import BaseCommand, CommandError
from data_logger_api.models import Data, Node
from datetime import datetime, timedelta
import pytz
from django.conf import settings
import logging


logger = logging.getLogger('django.' + __name__)


class Command(BaseCommand):
    help = 'Compresses data entries in db by counting an average based on resolution'

    def handle(self, *args, **options):
        # convert older than one month in hourly average
        # convert older than one year into daily average
        nodes = Node.objects.all()
        for node in nodes:
            self.convert_to_next_resolution(node, 0)
            self.convert_to_next_resolution(node, 10)

    def convert_to_next_resolution(self, node, resolution):
        logger.info("Converting from resolution {}".format(resolution))
        skip_days = 5
        resolution_time_delta = timedelta(hours=1)
        if resolution > 0:
            skip_days = 365
            resolution_time_delta = timedelta(hours=24)

        older_than = datetime.now(tz=pytz.timezone(settings.TIME_ZONE)) - timedelta(days=skip_days)
        logger.info("converting older than {}".format(str(older_than)))
        node_datas = Data.objects.filter(
            timestamp__lte=older_than) \
            .filter(node__address=node.address) \
            .filter(resolution=resolution).order_by('timestamp')
        try:
            start = node_datas[0].timestamp
            end = start + resolution_time_delta

        except IndexError:
            return

        while start < older_than:
            compress_data = node_datas.filter(timestamp__gte=start, timestamp__lte=end)
            averages = self.count_averages(compress_data)

            for key, value in averages.items():
                Data.objects.create(
                    timestamp=compress_data[0].timestamp,
                    resolution=resolution + 10,
                    type=key,
                    value=value['average'],
                    node=node
                )

            deleted, row_count = compress_data.delete()
            if deleted:
                logger.info("compressed {} rows from node {}".format(row_count['data_logger_api.Data'], node.name))
            start += resolution_time_delta
            end = start + resolution_time_delta

    @staticmethod
    def count_averages(node_datas):
        data_averages = {}
        for node_data in node_datas:
            if isinstance(node_data.value, str):
                continue
            else:
                try:
                    data_averages[node_data.type]['count'] += 1.0
                    data_averages[node_data.type]['sum'] += float(node_data.value)
                    data_averages[node_data.type]['average'] = \
                        data_averages[node_data.type]['sum'] / data_averages[node_data.type]['count']
                except KeyError:
                    data_averages[node_data.type] = {
                        'count': 1.0,
                        'sum': float(node_data.value),
                        'average': float(node_data.value)
                    }

        return data_averages


