from __future__ import absolute_import

from celery import shared_task

from django.conf import settings
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

import requests
import json
import urllib


@shared_task
def push_to_map(data, route):

    route = [x.strip() for x in route.split(',')]

    paths = []

    for point in route:

        address = urllib.quote_plus('%s, Raleigh, NC' % point)
        resp = requests.get(settings.GOOGLE_GEOCODE_URL_BASE + address + '&key=%s' % settings.GOOGLE_API_KEY)
        lat_long = resp.json()['results'][0]['geometry']['location']

        paths.append([lat_long['lng'], lat_long['lat']])

    arcgis_data = [
        {
            "geometry": {
                  "paths": [paths],
                  "spatialReference": {"wkid": settings.WKID}
            },
            "attributes": data
        }
    ]

    form_data = {
        'features': json.dumps(arcgis_data),
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    resp = requests.post(settings.FEATURE_SERVER_URL, data=urllib.urlencode(form_data), headers=headers)

    print(resp.text)


@shared_task
def distributed_rabbit_test():

    logger.info("Successfully used remote RabbitMQ node to execute this task.")
