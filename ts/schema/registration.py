from ts.model.registration import Application

from ts import ma


class ApplicationSchema(ma.ModelSchema):
    class Meta:
        model = Application
        exclude = ('updated_at', 'created_at')


