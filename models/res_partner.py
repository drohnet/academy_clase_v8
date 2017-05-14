# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions

ACADEMY_TYPE_LIST = [('public','Public'),
                     ('private','Private'),
                     ('concerted','Concerted')]

"""Herencia: Academias, Estudiantes, Profesores ->Tipo"""
class res_partner(models.Model):    
    _inherit = 'res.partner'
    
    academy_type=fields.Selection(ACADEMY_TYPE_LIST, 'Academy type', help="Select the academy type for the record")
    course_ids=fields.One2many('coursev8', 'academy_id', string='Courses')
    is_academy=fields.Boolean(string='Is Academy')
    is_student=fields.Boolean(string='Is student')
    is_teacher=fields.Boolean(string='Is teacher')
    
    @api.multi
    @api.constrains("name")
    def _check_name(self):
        
        if self.is_teacher == True :
            previous_name_ids = self.search( [('id','!=',self.id),('name','=ilike',self.name),('is_teacher','=',True)])
            if previous_name_ids.name == self.name:
                raise exceptions.ValidationError(
                        _("Try enter other Teacher name !! This is taken."))
                return
                
        if self.is_academy == True :
            previous_name_ids = self.search( [('id','!=',self.id),('name','=ilike',self.name),('is_academy','=',True)])
            if previous_name_ids.name == self.name:
                raise exceptions.ValidationError(
                        _("Try enter other Academy name !! This is taken."))
                return
                
        if self.is_student == True :
            previous_name_ids = self.search( [('id','!=',self.id),('name','=ilike',self.name),('is_student','=',True)])
            if previous_name_ids.name == self.name:
                raise exceptions.ValidationError(
                        _("Try enter other Student name !! This is taken."))
                return

    @api.multi
    @api.onchange("name")
    def onchange_name(self):
        if self.name:
            self.name = self.name.title()
        return 
   
 
