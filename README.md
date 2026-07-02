Student Management System - Odoo 19 TDD Project
Created by: Ameer Nawaz

Purpose
This project is a Student Management module for Odoo 19, built to practice Test-Driven
Development (TDD). It manages basic student records — Student ID, Name, Age, Email,
Department, GPA — while enforcing four business rules: GPA can't exceed 4.0, age must
be over 15, and both email and student ID must be unique.

How it works
The module defines a single model, student.record (or student.management), with the
fields above. Validation is handled through Odoo's @api.constrains decorators — Python
methods that run automatically whenever a record is created or updated, raising a
ValidationError if a rule is broken. Users interact with the data through standard list, form,
and search views, reachable from a dedicated menu, with access controlled by two
security groups (User and Manager).

Testing
Following TDD, the tests were written before the model implementation. Five tests cover:
creating a valid student, rejecting an underage student, rejecting a GPA over 4.0, rejecting
a duplicate email, and rejecting a duplicate student ID — each expecting a validation error
or integrity block. The tests run via Odoo's built-in test runner (--test-enable), and only
execute when a module is freshly installed or explicitly updated (-u), not on every server
start. 

All 5 tests currently pass against a live Odoo 19 instance.
Test execution command:
./odoo-bin -c debian/odoo.conf -d student_db -u student_record --test-enable --stop-
after-init
Produces 5 passing tests, 0 failures, confirming all four business rules are correctly
enforced.

Challenges Faced

Odoo 19 Upgrades: I adapted to major framework changes, including using <list>
instead of <tree>, dropping <group> tags inside search views, and adjusting to new
models.Constraint and user group privilege structures.•


Constraint Logic: I resolved a conflict where database unique constraints overrode
my custom Python messages. I relied on @api.constrains and database flush
handling so the exact business validation errors would trigger properly.

Testing Commands: I learned that once my module is installed, I must use the -u
(update) flag instead of -i (install), otherwise Odoo skips running my tests.
Test Bug Fix: I fixed a copy-paste error in my test file where the duplicate ID test
was accidentally using two different IDs, ensuring it now properly tests for
duplicates.

Conclusion
The module satisfies all stated business rules using a proper TDD workflow: failing tests
were written first, then the model was implemented until all tests passed. The module
includes full CRUD views, menu/action, access-rights security, and both Python- and SQL-
level data validation, and is ready to install on Odoo 19.
