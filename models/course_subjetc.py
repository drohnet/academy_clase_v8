# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions

"""Relación curso-materia-horario"""
class course_subject(models.Model):
    _name = 'course.subject'
    
    name=fields.Char('Name', required=True, size=64,ondelete='cascade')
    course_id=fields.Char('Name', required=True, size=64,ondelete='cascade')
    #fix it
    course_id_time_table_id=fields.Related('course_id','time_table_id_detail_ids',type='many2one' ,relation='time.table', string='Course time table')
    time_table_id_detail_ids=fields.Related('course_id','time_table_id', 'time_detail_ids', type='one2many', relation='time.table.detail', string='Time table detail')
    subject_id=fields.Many2one('subject', string='Subject', required=True, ondelete='restrict')
    test_id=fields.Many2one('subject', string='test_id',  ondelete='cascade')
    child_ids=fields.One2many('course.subject.time.table.detail', 'course_subject_id', string='Time table', ondelete='cascade')
    #fix it
    test=fields.Related('course_id','time_table_id','time_detail_ids',type="one2many",relation='time.table.detail' ,string='test1')
    #fix it
    testt=fields.Related('course_id','time_table_id', 'time_detail_ids', type='one2many', relation='time.table.detail', string='Testt2')
    #fix it
    testtt=fields.Related('course','time_table_id_detail_ids','day_of_week' ,string="testtt3")
   
