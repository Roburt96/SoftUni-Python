from unittest import TestCase

from project.student import Student


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student = Student('Roburt')
        self.student_with_course = Student('Roburt', {'Python': ['Basics']})

    def test_successfully_init(self):
        self.assertEqual('Roburt', self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({'Python': ['Basics']}, self.student_with_course.courses)

    def test_add_course_and_check_is_already_added(self):
        output = "Course already added. Notes have been updated."
        inputs = self.student_with_course.enroll("Python", "basics")
        self.assertEqual(output, inputs)

    def test_add_notes_and_course(self):
        output = "Course and course notes have been added."
        inputs = self.student_with_course.enroll("Java", "basics", "Y")
        self.assertEqual(output, inputs)

    def test_add_new_course(self):
        output = "Course has been added."
        inputs = self.student_with_course.enroll("JavaScript", "basics", '1')
        self.assertEqual(output, inputs)
        self.assertEqual([], self.student_with_course.courses['JavaScript'])

    def test_successfully_add_notes(self):
        output = "Notes have been updated"
        inputs = self.student_with_course.add_notes("Python", "advanced")
        self.assertEqual(output, inputs)

    def test_cant_find_course_with_that_name(self):
        output = "Cannot add notes. Course not found."
        with self.assertRaises(Exception) as ecp:
            self.student_with_course.add_notes("javascript", "basics")
        self.assertEqual(str(ecp.exception), output)

    def test_successfully_leave_course_name(self):
        output = "Course has been removed"
        inputs = self.student_with_course.leave_course('Python')
        self.assertEqual(inputs, output)

    def test_cant_find_course_with_that_name_to_leave(self):
        output = "Cannot remove course. Course not found."
        with self.assertRaises(Exception) as ecp:
            self.student_with_course.leave_course('javascript')
        self.assertEqual(str(ecp.exception), output)


