# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# Copyright 2017 eHanse
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class SaleOrderExtended(models.Model):
    _inherit = "sale.order"

    quot_report_note = fields.Text(
        'Notes'
    )

    subconsigned = fields.Boolean(
        string='Sub Consigned',
    )

