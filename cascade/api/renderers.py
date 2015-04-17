from rest_framework import renderers
from rest_framework.utils.serializer_helpers import ReturnList
import inflection
import json


class JSONRenderer(renderers.BaseRenderer):
    media_type = 'application/json'
    format = 'json'

    def render(self, data, media_type=None, renderer_context=None):
        name = renderer_context['view'].get_queryset().first().__class__.__name__
        name = inflection.underscore(name)

        if type(data) is ReturnList:
            name = inflection.pluralize(name)

        data = {name: data}
        return json.dumps(data)
