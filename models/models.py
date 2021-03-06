# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Pos(models.Model):
    _inherit = 'product.product'

    codigo_mann = fields.Char(
        string='Codigo Mann',related="product_tmpl_id.codigo_man",store=True,
        required=False)
    marca_filtro = fields.Char(
        string='Marca Filtro',related="product_tmpl_id.marca_filtro_id.name",store=True,
        required=False)
    pos_categ = fields.Char(
        string='Categegoria',related="product_tmpl_id.pos_categ_id.name",store=True,
        required=False)
    ubicacion = fields.Char(
        string='Ubicación Stock',related="product_tmpl_id.ubicacion_id.name",store=True,
        required=False)


