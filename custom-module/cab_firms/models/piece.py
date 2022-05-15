from odoo import models, fields, api


class Piece(models.Model):
    _name = 'piece.rechange'



    piece_id = fields.Many2one('cabfirms.cabfirms',string= "Cariere")
    date = fields.Datetime(required = True)
    fournisseur = fields.Many2one('res.users', ondelete='set null', index=True)
    piece = fields.Many2one('product.product',required = True)
    Quantite = fields.Integer()
    Matericule = fields.Char()
    chouffeur = fields.Many2one('res.users')
    description = fields.Text()
