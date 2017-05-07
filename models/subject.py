# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions

class subject(osv.osv):    
    """ Subject  """
    _name = 'subject'
    
    name=fields.Char('Name', required=True, size=64)
    description=fields.Text('Description')
    hours=fields.Integer('Duration', required=True, help='Duration in hours')
    
