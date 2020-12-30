odoo.define('pos_product_reference.pos_receipt', function (require) {
"use strict";

var gui = require('point_of_sale.gui');
var models = require('point_of_sale.models');
models.load_fields("product.product", ['default_code']);
models.load_fields("product.product", ['codigo_mann']);
models.load_fields("product.product", ['marca_filtro']);
models.load_fields("product.product", ['pos_categ']);
models.load_fields("product.product", ['ubicacion']);

});
