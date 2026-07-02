from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StudentManagement(models.Model):
    _name = 'student.management'
    _description = 'Student Management'
    _rec_name = 'name'

    student_id = fields.Char(string='Student ID', required=True)
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    email = fields.Char(string='Email', required=True)
    department = fields.Char(string='Department')
    gpa = fields.Float(string='GPA')

    @api.constrains('age')
    def _check_age(self):
        for rec in self:
            if rec.age <= 15:
                raise ValidationError("Age must be greater than 15")

    @api.constrains('gpa')
    def _check_gpa(self):
        for rec in self:
            if rec.gpa > 4.0:
                raise ValidationError("GPA cannot exceed 4.0")

    @api.constrains('email')
    def _check_email_unique(self):
        for rec in self:
            if rec.email and self.search_count([
                ('email', '=', rec.email),
                ('id', '!=', rec.id),
            ]) > 0:
                raise ValidationError("Email must be unique")

    @api.constrains('student_id')
    def _check_student_id_unique(self):
        for rec in self:
            if rec.student_id and self.search_count([
                ('student_id', '=', rec.student_id),
                ('id', '!=', rec.id),
            ]) > 0:
                raise ValidationError("Student ID must be unique")
