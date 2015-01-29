from __future__ import absolute_import

from celery import shared_task

import requests
import json


@shared_task
def push_to_map(url, data):

    form_data = {
        'features': data,
        'gdbVersion': '',
        'rollBackOnFailure': True,
        'f': 'pjson'
    }
    
    response = requests.post(url, data=form_data)
    
    print(form_data)

    print(response.request.headers)
    print(response.json())
