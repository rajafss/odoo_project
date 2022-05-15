

from odoo import models, fields, api


class Commande(models.Model):
    _name = 'cabfirms.commande'


    name = fields.Char(string="Commande",required = True)
    code_bar = fields.Integer()
    fournisseur = fields.Many2one('res.users')
    date = fields.Datetime(required = True)
    prix_unit = fields.Float()
    prix_total = fields.Float()
    description = fields.Text()
    quantite = fields.One2many('cabfirms.livraison','quantite_id')
    commande_id = fields.Many2one('cabfirms.cabfirms')

    def delevery(self):
        view_id = self.env.ref('cab_firms.cab_firms_form').id
        context = self._context.copy()
        return {
            'name': 'Bon Livraison',
            'view_type': 'form',
            'view_mode': 'form',
            'views': [(view_id, 'form')],
            'res_model': 'cabfirms.cabfirms',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': context}






class Livraison(models.Model):
    _name = 'cabfirms.livraison'

    quantite_id = fields.Many2one('cabfirms.commande',string="Commande_id")
    quantite_total= fields.Integer()
    quantite_utilise = fields.Integer()
    produit = fields.Many2one('product.product')