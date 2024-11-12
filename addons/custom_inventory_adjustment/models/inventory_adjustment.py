from odoo import models, fields, api

class CustomInventoryAdjustment(models.Model):
    _inherit = 'stock.inventory'

    custom_notes = fields.Text(string='Custom Notes')
    adjustment_reason = fields.Selection([
        ('damaged', 'Damaged Goods'),
        ('expired', 'Expired Products'),
        ('theft', 'Theft or Loss'),
        ('received', 'Goods Received'),
        ('other', 'Other')
    ], string='Adjustment Reason')

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code('custom.inventory.adjustment') or '/'
        return super(CustomInventoryAdjustment, self).create(vals)

class CustomInventoryAdjustmentLine(models.Model):
    _inherit = 'stock.inventory.line'

    custom_remarks = fields.Char(string='Remarks')