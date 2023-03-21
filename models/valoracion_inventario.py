# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ValoracionStock(models.Model):
    _inherit = "stock.valuation.layer"

    total_costo = fields.Float('Total valor a costo de reposición', store=True, compute= '_compute_total') #,store= True ,related='product_id.standard_price'

    @api.depends('product_id')
    def _compute_total(self):
        for c in self:
            c.total_costo = c.quantity * c.product_id.with_company(c.company_id).replenishment_cost
