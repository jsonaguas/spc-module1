from app.extensions import ma
from app.models import ServiceTickets, Mechanic
from marshmallow import fields

class ServiceTicketsSchema(ma.SQLAlchemyAutoSchema):
    mechanics = fields.Nested("MechanicSchema", many=True)
    class Meta:
        model = ServiceTickets
        fields = ("mechanic_ids", "service_date", "service_desc", "VIN", "id", "customer_id", "mechanics")

service_ticket_schema = ServiceTicketsSchema()
service_tickets_schema = ServiceTicketsSchema(many=True)
