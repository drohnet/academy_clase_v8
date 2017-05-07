# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions

class subject(models.Model):    
    """ Subject  """
    _name = 'subjectv8'
    
    name=fields.Char('Name', required=True, size=64)
    description=fields.Text('Description')
    hours=fields.Integer('Duration', required=True, help='Duration in hours')
    
