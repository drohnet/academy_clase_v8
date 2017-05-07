# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions


"""Asistencia detalle"""    
class student_attendance_detail(models.Model):
    """ Student Attendance Detail  """
    _name = 'student.attendance.detailv8'
    
    name=fields.Char('Name', required=True, size=64)
    attendance_id=fields.Many2one('student.attendancev8', string="Attendance", required=True)
    student_id=fields.Many2one('res.partner', string="Student", required=True, domain=[('is_student','=',True)])
    attendance_date=fields.Date(string='Date', required=True)
    sign=fields.Boolean(string='Sign', required=False)
    
