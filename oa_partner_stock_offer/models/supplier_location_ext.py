# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limted
# Copyright 2017 eHanse
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class SupplierLocation(models.Model):
    _inherit = "supplier.location"

    short_loc = fields.Char(
        'Location',
        readonly=True,
    )

    @api.model
    def create(self, vals):
        to_shorten = vals['name']
        splits = to_shorten.split(" ")
        vals['short_loc'] = splits[1] if len(splits) > 1 else vals['name']
        return super(SupplierLocation, self).create(vals)

    @api.multi
    def write(self,vals):
        if 'name' in vals:
            to_shorten = vals['name']
            splits = to_shorten.split(" ")
            vals['short_loc'] = splits[1] if len(splits) > 1 else vals['name']
        return super(SupplierLocation,self).write(vals)
