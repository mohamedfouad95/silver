from odoo.addons.website.controllers.main import Website
from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request
class website_cust(WebsiteSale):
     

    """def values_postprocess(self, order, mode, values, errors, error_msg):
        
        new_values = {}
        authorized_fields = request.env['ir.model']._get('res.partner')._get_form_writable_fields()
         
        
        for k, v in values.items():
            
            # don't drop empty value, it could be a field to reset
            if k=='mobile' or k=='floor'or k=='block':
                new_values[k] = v

            if k in authorized_fields and v is not None:
                new_values[k] = v
            else:  # DEBUG ONLY
                if k not in ('field_required', 'partner_id', 'callback', 'submitted'): # classic case
                    _logger.debug("website_sale postprocess: %s value has been dropped (empty or not writable)" % k)

        new_values['customer'] = True
        new_values['team_id'] = request.website.salesteam_id and request.website.salesteam_id.id
        new_values['user_id'] = request.website.salesperson_id and request.website.salesperson_id.id
        new_values['website_id'] = request.website.id

        lang = request.lang if request.lang in request.website.mapped('language_ids.code') else None
        if lang:
            new_values['lang'] = lang
        if mode == ('edit', 'billing') and order.partner_id.type == 'contact':
            new_values['type'] = 'other'
        if mode[1] == 'shipping':
            new_values['parent_id'] = order.partner_id.commercial_partner_id.id
            new_values['type'] = 'delivery'
        
        return new_values, errors, error_msg"""
    @http.route(['/add_all/product/<model("product.template"):product>'], type='http', auth="public", website=True)
    def product_ppp(self, product, category='', search='',add_qty=1, **kwargs):
        _logger.info("Add NEW ")
        _logger.info(kwargs)
        _logger.info(product)
        product_twmp=request.env['product.product'].search([('product_tmpl_id','=',product.id)]).id
        _logger.info(product_twmp)
        self.cart_update(product_twmp)
        return request.redirect('/shop')
class partner((models.Model)):
    _inherit="res.partner"
    floor=fields.Char("Floor")
    block=fields.Char("Block")
 