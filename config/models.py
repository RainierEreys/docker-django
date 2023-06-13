from django.db import models
from djangodoo.models import OdooModel

class Partner(OdooModel):
    _odoo_model = "res.partner"
    _odoo_fields = ['name']  # optional; if omitted, all fields are copied
