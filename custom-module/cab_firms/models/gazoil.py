from odoo import models, fields, api


class Gazoil(models.Model):
    _name = 'gazoil.litter'



    gazoil_id = fields.Many2one('cabfirms.cabfirms',string= "Carriere")
    date = fields.Datetime(required=True)
    fournisseur = fields.Many2one('res.users', ondelete='set null', index=True)
    gazoil = fields.Many2one('product.product',required = True)
    litter = fields.Integer()
    matricule = fields.Char()
    chouffeur = fields.Many2one('res.users')
    description = fields.Text()