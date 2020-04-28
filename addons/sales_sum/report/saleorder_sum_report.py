from odoo import api, models
from dateutil.relativedelta import relativedelta
import datetime
import logging
import pytz
from collections import OrderedDict
_logger = logging.getLogger(__name__)


class ReportProductSale(models.AbstractModel):
    _name = "report.sales_sum.saleorder_sum_report"
    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        _logger.info("OOO")
        _logger.info(docs)
        product_list=[]
        customer_list,cst=[],[]
        sales_rep_list=[]
        sales_rep=''
        for rec in docs.order_line:
            product_list.append(rec.product_id.id)
            customer_list.append(rec.order_id.partner_id.id)
            sales_rep_list.append(rec.order_id.user_id.id)
        #{'id':rec.order_id.partner_id.id,'address':rec.order_id.partner_id.street,'name':rec.order_id.partner_id.street,'phone':rec.order_id.partner_id.phone}
        customer_list=list(OrderedDict.fromkeys(customer_list))
        sales_rep_list=list(OrderedDict.fromkeys(sales_rep_list))
        if len(sales_rep_list)==1:
            sales_rep=self.env['res.users'].search([('id','=',sales_rep_list)]).name
        for customer in customer_list:
            partner_id=self.env['res.partner'].search([('id','=',customer)])
            if partner_id:
                
                cst.append({'address':partner_id.street+"-"+partner_id.city+"-"+partner_id.state_id.name,'name':partner_id.name,'phone':partner_id.phone})


        _logger.info("Customer")
        _logger.info(customer_list)
        product_list=list(OrderedDict.fromkeys(product_list))
        list_qty=[]
        
        
      

        _logger.info("PPPPPPPPP")
        _logger.info(product_list)
        for pro in product_list:
            qty=0
            pro_name=self.env['product.product'].search([('id','=',pro)]).name
            for order in docs.order_line:
                if pro ==order.product_id.id:
                    qty+=order.product_uom_qty
            list_qty.append({'product':pro_name,'qty':qty})
        _logger.info(list_qty)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'sale.order',
            'docs': docs,
            'list_qty':list_qty,
            'cst':cst,
            'sales_rep':sales_rep,
            'proforma': True
        }