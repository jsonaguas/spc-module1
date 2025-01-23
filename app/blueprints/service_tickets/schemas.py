from app.extensions import ma
from app.models import ServiceTickets, Mechanic
from marshmallow import fields

class EditTicketSchema(ma.Schema):
    add_customer_ids = fields.List(fields.Int(), required=False)
    remove_customer_ids = fields.List(fields.Int(), required=False)
    add_part_ids = fields.List(fields.Int(), required=False)
    class Meta:
        fields = ('add_customer_ids', 'remove_customer_ids', 'add_part_ids')

class ServiceTicketsSchema(ma.SQLAlchemyAutoSchema):
    mechanics = fields.Nested("MechanicSchema", many=True)
    class Meta:
        model = ServiceTickets
        fields = ("mechanic_ids", "service_date", "service_desc", "VIN", "id", "customer_id", "mechanics")

service_ticket_schema = ServiceTicketsSchema()
service_tickets_schema = ServiceTicketsSchema(many=True)
edit_ticket_schema = EditTicketSchema()
