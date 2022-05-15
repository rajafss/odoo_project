from odoo import models, fields, api


class Produit(models.Model):
    _name = 'produit.order'



    produit_id = fields.Many2one('cabfirms.cabfirms',string= "Cariere")
    date = fields.Datetime(required = True)
    produit = fields.Many2one('product.product',required=True)
    Matericule = fields.Char()
    chouffeur = fields.Many2one('res.users')
    nb_voyage = fields.Integer()
    description = fields.Text()
