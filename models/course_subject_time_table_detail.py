# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions

DAYS_OF_WEEK = [('monday','Monday'),
                ('tuesday','Tuesday'),
                ('wednesday','Wednesday'),
                ('thursday','Thursday'),
                ('friday','Friday'),
                ('saturday','Saturday'),
                ('sunday','Sunday'),]

"""curso-materia-horario-detalle"""    
class course_subject_time_table_detail(models.Models):    
    """ Course subject time table detail  """
    _name = 'course.subject.time.table.detailv8'
    
    name=fields.Char('Name', required=True, size=16,ondelete='cascade')
    sequence=fields.Integer('Sequence',ondelete='cascade')
    course_subject_id=fields.Many2one('course.subject', 'Course-Subject relation', required=True,ondelete='cascade')
    day_of_week=fields.selection(DAYS_OF_WEEK, 'Days of week', required=True,ondelete='cascade')
    hour_start=fields.Float('From',digits=(4,2), required=True, help='Hour from',ondelete='cascade')
    hour_end=fields.Float('To', digits=(4,2), required=True, help='Hour to',ondelete='cascade')
 
