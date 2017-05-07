# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions

ATTENDANCE_STATE = [('draft','Draft'),
                    ('confirmed','Confirmed'),                    
                    ('cancel','Cancel'),
                    ('done','Done')]

"""Asistencia"""    
class student_attendance(models.Model):
    """ Student Attendance Header  """
    _name = 'student.attendancev8'
    
    name=fields.Char('Name', required=True, size=128)
    course_subject_id=fields.Many2one('course.subject', string="Course - Subject", required=True)
    date_start=fields.Date('Start date', required=True, help='')
    date_end=fields.Date('End date', required=True, help='')
    state=fields.Selection(ATTENDANCE_STATE, 'state', required=True)
    
    _defaults = {
                state=ATTENDANCE_STATE[0][0]
    }
