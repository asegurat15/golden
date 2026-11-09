# -*- coding: utf-8 -*-

from odoo import models, fields
class AccountAccount(models.Model):
    _inherit = 'account.account'
    
    account_local_code = fields.Char(string='Código de equivalencia')


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    po_number   = fields.Char(string="PO#")
