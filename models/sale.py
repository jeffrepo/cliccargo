# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    numero_movimientos = fields.Char('No. movimientos')
    origen = fields.Char('Origen')
    destino = fields.Char('Destino')
    custodio = fields.Char('Custodio')
    numero_contenedor = fields.Char('Numero contenedor')
    hora_fecha_carga = fields.Datetime('Hora y fecha de carga')
    hora_fecha_salida = fields.Datetime('Hora y fecha de salida')
    hora_fecha_entrega = fields.Datetime('Hora y fecha de entrega')
