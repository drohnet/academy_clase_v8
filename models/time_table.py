# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions

"""Horario"""
class time_table(models.Model):    
    """ Time table  """
    _name = 'time.tablev8'
    
    name=fields.Char(string='name' ,required=True, size=64)
    description=fields.Text('Description')
    time_detail_ids=fields.One2many('time.table.detailv8', 'time_table_id', string='Detail')
    
