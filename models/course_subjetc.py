# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions

"""Relación curso-materia-horario"""
class course_subject(models.Model):
    _name = 'course.subjectv8'
    
    name=fields.Char('Name', required=True, size=64,ondelete='cascade')
    course_id=fields.Many2one('course', string='Course', required=True, ondelete='cascade')
    #fix it
    course_id_time_table_id=fields.Char(related='course_id.time_table_id_detail_ids', string='Course time table')
    time_table_id_detail_ids=fields.Char('course_id.time_table_id.time_detail_ids')
    subject_id=fields.Many2one('subject', string='Subject', required=True, ondelete='restrict')
    test_id=fields.Many2one('subject', string='test_id',  ondelete='cascade')
    child_ids=fields.One2many('course.subject.time.table.detail', 'course_subject_id', string='Time table', ondelete='cascade')
    #fix it
    test=fields.Char(related='course_id.time_table_id.time_detail_ids',string='test1')
    #fix it
    testt=fields.Char(related='course_id.time_table_id.time_detail_ids', string='Testt2')
    #fix it
    testtt=fields.Char('course.time_table_id_detail_ids.day_of_week' )
   
