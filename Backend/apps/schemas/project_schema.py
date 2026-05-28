from marshmallow import Schema, fields


class MaterialSchema(Schema):
    item_name = fields.String(required=True)
    quantity = fields.Integer(required=True)
    unit = fields.String(required=True)
    estimated_price = fields.Float(required=True)
    total_cost = fields.Float(required=True)


class ToolSchema(Schema):
    icon_id = fields.Integer(required=True)
    svg_path = fields.String(dump_only=True, allow_none=True)
    name = fields.String(required=True)
    category = fields.String(required=True)


class SourcingLocationSchema(Schema):
    store_name = fields.String(required=True)
    address = fields.String(required=True)
    distance_km = fields.Float(required=True)
    provides = fields.String(required=False, allow_none=True)
    google_maps_url = fields.String(required=False, allow_none=True)


class ProjectCreateSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    status = fields.String(required=False, allow_none=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=False, allow_none=True)
    location = fields.String(required=False, allow_none=True)
    volunteer_count = fields.Integer(required=False, allow_none=True)
    photo_url = fields.Url(required=False, allow_none=True)
    materials = fields.List(fields.Nested(MaterialSchema), required=False)
    tools = fields.List(fields.Nested(ToolSchema), required=False)
    sourcing_locations = fields.List(fields.Nested(SourcingLocationSchema), required=False)


class ProjectUpdateSchema(Schema):
    title = fields.String(required=False)
    description = fields.String(required=False, allow_none=True)
    status = fields.String(required=False, allow_none=True)
    start_date = fields.Date(required=False)
    end_date = fields.Date(required=False, allow_none=True)
    location = fields.String(required=False, allow_none=True)
    volunteer_count = fields.Integer(required=False, allow_none=True)
    photo_url = fields.Url(required=False, allow_none=True)
    materials = fields.List(fields.Nested(MaterialSchema), required=False)
    tools = fields.List(fields.Nested(ToolSchema), required=False)
    sourcing_locations = fields.List(fields.Nested(SourcingLocationSchema), required=False)


class ProjectResponseSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String(required=True)
    description = fields.String(allow_none=True)
    status = fields.String(allow_none=True)
    start_date = fields.String(required=True)
    end_date = fields.String(allow_none=True)
    location = fields.String(allow_none=True)
    volunteer_count = fields.Integer(allow_none=True)
    photo_url = fields.String(allow_none=True)
    created_at = fields.String(required=True)
    updated_at = fields.String(required=True)
    materials = fields.List(fields.Nested(MaterialSchema))
    tools = fields.List(fields.Nested(ToolSchema))
    sourcing_locations = fields.List(fields.Nested(SourcingLocationSchema))
