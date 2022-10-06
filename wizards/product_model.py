# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Niyas Raphy and Sreejith P (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from . import barcode
from odoo import api, models


class ProductAutoBarcode(models.Model):
    _inherit = 'product.product'

    @api.model
    def create(self, vals):
        res = super(ProductAutoBarcode, self).create(vals)
        ean = barcode.generate_ean(self, str(res.id))
        res.barcode = ean
        print("res.barcode",res.barcode)
        return res


class ProductTemplateAutoBarcode(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, vals_list):
        templates = super(ProductTemplateAutoBarcode, self).create(vals_list)
        #ean = templates.product_variant_id.barcode
        #templates.barcode = ean
        print("TEMPLATES BARCODE: ",templates.barcode)

        return templates


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
