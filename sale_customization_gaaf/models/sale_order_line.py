from odoo import api, fields, models, _
from odoo.tools import format_date

class AccountMoveLine(models.Model):
    _inherit = "sale.order.line"

    delivery_date = fields.Date(string="Fecha de entrega")
