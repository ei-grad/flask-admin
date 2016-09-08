from wtforms import fields
from geoalchemy2.elements import WKBElement
from geoalchemy2.shape import to_shape

from .widgets import LeafletWidget


class GeometryField(fields.TextAreaField):
    widget = LeafletWidget()

    def __init__(self, *args, **kwargs):
        self.geometry_type = kwargs.pop('geometry_type')
        super(GeometryField, self).__init__(*args, **kwargs)

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        if isinstance(self.data, WKBElement):
            return to_shape(self.data).to_wkt()
        return ''

    def process_formdata(self, valuelist):
        # exclude empty values from valuelist, because empty WKT is invalid WKT
        if valuelist and valuelist[0]:
            self.data = valuelist[0]
