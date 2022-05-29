from odoo import fields, models, api


class ResConfigSettingExtend(models.TransientModel):
    _inherit = 'res.config.settings'

    barcode_prefix = fields.Char(size=2, default="10", required=True)

    def set_values(self):
        res = super(ResConfigSettingExtend, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        param.set_param('product_barcode_generator_odoo.barcode_prefix', self.barcode_prefix)
        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettingExtend, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(barcode_prefix=params.get_param('product_barcode_generator_odoo.barcode_prefix'))
        return res
