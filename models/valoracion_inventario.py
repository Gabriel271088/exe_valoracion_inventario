# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ValoracionStock(models.Model):
    _inherit = "stock.valuation.layer"

    total_costo = fields.Float('Total valor a costo de reposición', compute= '_compute_total') #,store= True ,related='product_id.standard_price'

    def _compute_total(self):
        for c in self:
            c.total_costo = c.product_id.qty_available * c.product_id.with_company(c.company_id).replenishment_cost
