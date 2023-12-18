from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    img = fields.Str()
    description = fields.Str()
    status = fields.Bool()
    label = fields.Str()