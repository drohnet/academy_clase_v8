# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions

DAYS_OF_WEEK = [('monday','Monday'),
                ('tuesday','Tuesday'),
                ('wednesday','Wednesday'),
                ('thursday','Thursday'),
                ('friday','Friday'),
                ('saturday','Saturday'),
                ('sunday','Sunday'),]

"""Horario detalle"""    
class time_table_detail(models.Model):    
    """ Time table detail  """
    _name = 'time.table.detailv8'
    
    name=fields.Char('Name', required=True, size=16)
    time_table_id=fields.Many2one('time.tablev8', 'Time table', required=True)
    day_of_week=fields.Selection(DAYS_OF_WEEK, 'Days of week', required=True)
    hour_start=fields.Float('From',digits=(4,2), required=True, help='Hour from')
    hour_end=fields.Float('To', digits=(4,2), required=True, help='Hour to')
    sequence=fields.Integer('Sequence')
    
    _defaults = {
                'sequence':1,
    }
  
