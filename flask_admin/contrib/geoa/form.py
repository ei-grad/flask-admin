from flask_admin.model.form import converts
from flask_admin.contrib.sqla.form import AdminModelConverter as SQLAAdminConverter
from .fields import GeometryField


class AdminModelConverter(SQLAAdminConverter):
    @converts('Geography', 'Geometry')
    def convert_geom(self, column, field_args, **extra):
        field_args['geometry_type'] = column.type.geometry_type
        return GeometryField(**field_args)
