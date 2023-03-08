# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ValoracionStock(models.Model):
    _inherit = "stock.valuation.layer"
    
    total_costo = fields.Float('Total valor a costo de reposición',related='product_id.standard_price')
