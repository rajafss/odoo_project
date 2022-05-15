# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cabfirms(models.Model):
    _name = 'cabfirms.cabfirms'


    name = fields.Char(string="Nom de carriere",required = True)
    responsible_id = fields.Many2one('res.users',required = True)
    date_debut = fields.Datetime()
    date_fin = fields.Datetime()
    description = fields.Text()
    materieux = fields.One2many('materieux.materieux','mat_id')
    produits = fields.One2many('produit.order','produit_id')
    pieces = fields.One2many('piece.rechange', 'piece_id')
    gazoils = fields.One2many('gazoil.litter', 'gazoil_id')
    commands = fields.One2many('cabfirms.commande','commande_id')





class Materieux(models.Model):
    _name = 'materieux.materieux'

    mat_id = fields.Many2one('cabfirms.cabfirms',string="Carriere")
    date = fields.Datetime(required = True)
    name = fields.Many2one('product.product',string="Materieux",required = True)
    quantite = fields.Integer()
    fournisseur = fields.Many2one('res.users')




