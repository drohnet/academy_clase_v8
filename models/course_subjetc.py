# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions

"""Relación curso-materia-horario"""
class course_subject(models.Model):
    _name = 'course.subjectv8'
    
    name=fields.Char('Name', required=True, size=64,ondelete='cascade')
    course_id=fields.Many2one('coursev8', string='Course', required=True, ondelete='cascade')
    course_id_time_table_id=fields.Char(related='course_id.name', string='Course time table', store= True)
    subject_id=fields.Many2one('subjectv8', string='Subject', required=True, ondelete='restrict')
    test_id=fields.Many2one('subjectv8', string='test_id',  ondelete='cascade')
    child_ids=fields.One2many('course.subject.time.table.detailv8', 'course_subject_id', string='Time table', ondelete='cascade')
    time_table_id_detail_ids=fields.One2many('time.table.detailv8','name',string="time table details",compute="change_change")
 
    @api.multi
    @api.onchange('subject_id')
    def change_na(self):
        if self.subject_id.name:
            self.name=str(self.course_id_time_table_id)+" - "+str(self.subject_id.name)
            return
        
    @api.multi
    @api.onchange("course_id","course_id_time_table_id")
    def change_change(self):
        if self.course_id:
            self.time_table_id_detail_ids = self.course_id.time_table_id_detail_ids
            return
       
        
