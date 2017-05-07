# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions

ACADEMY_TYPE_LIST = [('public','Public'),
                     ('private','Private'),
                     ('concerted','Concerted')]

"""Herencia: Academias, Estudiantes, Profesores ->Tipo"""
class res_partner(models.Model):    
    _inherit = 'res.partner'

    academy_type=fields.Selection(ACADEMY_TYPE_LIST, 'Academy type', help="Select the academy type for the record")
    course_ids=fields.One2many('course', 'academy_id', string='Courses'),
    is_academy=fields.Boolean(string='Is Academy')
    is_student=fields.Boolean(string='Is student')
    is teacher=fields.Boolean(string='Is teacher')
 
