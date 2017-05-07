# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions

COURSE_STATE = [('draft','Draft'),
                ('confirmed','Confirmed'),
                ('in_process','In Process'),
                ('cancel','Cancel'),
                ('done','Done')]

"""Cursos"""                     
class course(models.Model):    
    """ Course  """
    _name = 'course'
    
    name=fields.Char('Name', required=True, size=64)
    description=fields.Text('Description')
    hours=fields.Integer('Duration', required=True, help='Duration in hours')
    min_students=fields.Integer('Min students', required=True, help='Minimum quantity of students')
    max_students=fields.Integer('Min students', required=True, help='Minimum quantity of students')
    date_start=fields.Date('Start date', required=True, help='')
    date_end=fields.Date('End date', required=True, help='')
    price=fields.Float('Price', required=True, digits=(6,2), help='Price per student')
    state=fields.Selection(COURSE_STATE, 'state', required=False)
    subject_ids=fields.One2many('course.subject', 'course_id', string='Subjects',ondelete="Set null")
    academy_id=fields.Many2one('res.partner', string='Academy', required=True, domain=[('is_academy','=',True)], ondelete='restrict')
    student_ids=fields.Many2many('res.partner','course_student_table',string='Students', domain=[('is_student','=',True)])
    teacher_ids=fields.Many2many('res.partner','course_teacher_table',string='Teachers', domain=[('is_teacher','=',True)])
    time_table_id=fields.Many2one('time.table', string='Time table', required=True, ondelete='restrict')
    #campo a corregir
    time_table_id_detail_ids=fields.Related('time_table_id', 'time_detail_ids', type='one2many', relation='time.table.detail', string='Time table detail')
 
    _defaults = {
            state= COURSE_STATE[0][0]
    }
