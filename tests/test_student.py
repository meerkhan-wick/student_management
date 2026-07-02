from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestStudentManagement(TransactionCase):

    def test_01_create_student(self):
        student = self.env['student.management'].create({
            'name': 'Ali',
            'age': 20,
            'email': 'ali@gmail.com',
            'student_id': 'ST001',
            'gpa': 3.4,
        })
        self.assertEqual(student.name, 'Ali')
        self.assertEqual(student.age, 20)
        self.assertEqual(student.email, 'ali@gmail.com')
        self.assertEqual(student.student_id, 'ST001')
        self.assertEqual(student.gpa, 3.4)

    def test_02_invalid_age(self):
        with self.assertRaises(ValidationError):
            self.env['student.management'].create({
                'name': 'Young Student',
                'age': 10,
                'email': 'young@gmail.com',
                'student_id': 'ST002',
                'gpa': 3.0,
            })

    def test_03_invalid_gpa(self):
        with self.assertRaises(ValidationError):
            self.env['student.management'].create({
                'name': 'High GPA Student',
                'age': 22,
                'email': 'highgpa@gmail.com',
                'student_id': 'ST003',
                'gpa': 5.0,
            })

    def test_04_duplicate_email(self):
        self.env['student.management'].create({
            'name': 'Student A',
            'age': 20,
            'email': 'abc@gmail.com',
            'student_id': 'ST004',
            'gpa': 3.0,
        })
        with self.assertRaises(ValidationError):
            self.env['student.management'].create({
                'name': 'Student B',
                'age': 21,
                'email': 'abc@gmail.com',
                'student_id': 'ST005',
                'gpa': 3.2,
            })

    def test_05_duplicate_student_id(self):
        self.env['student.management'].create({
            'name': 'Student C',
            'age': 20,
            'email': 'c@gmail.com',
            'student_id': 'ST006',
            'gpa': 3.0,
        })
        with self.assertRaises(ValidationError):
            self.env['student.management'].create({
                'name': 'Student D',
                'age': 21,
                'email': 'd@gmail.com',
                'student_id': 'ST006',
                'gpa': 3.2,
            })
