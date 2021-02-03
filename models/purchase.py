# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    duca = fields.Char('duca')
    numero_contenedor = fields.Char('Numero contenedor')
    bl = fields.Char('BL')
