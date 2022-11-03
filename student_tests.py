import unittest
from class_definitions.student import Student as n

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.t = n("Stone", "Steven", "Computer Science", 4.0)
    def tearDown(self):
        del self.t
    def test_object_created_required_attributes(self):
        self.assertEqual(self.t.last_name, "Stone")
        self.assertEqual(self.t.first_name, "Steven")
    def test_object_created_all_attributes(self):
        t = n("Smith", "Jane", "Fashion", 4.0)
        assert t.last_name == "Smith"
        assert t.first_name == "Jane"
        assert t.major == "Fashion"
        assert t.gpa == 4.0
    def test_student_str(self):
        self.assertEqual(str(self.t), "Stone, Steven has major Computer Sciencewith gpa: 4.0")
    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            t = n("123", "Steven", "Computer Science", 4.0)
    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            t = n("Stone", "123", "Computer Science", 4.0)
    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            t = n("Stone", "Steven", "123", 4.0)
    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            t = n("Stone", "Steven", "Computer Science", "hello")
        with self.assertRaises(ValueError):
            t = n("Stone", "Steven", "Computer Science", 5)
if __name__ == "__main__":
    student1 = n("Fuller", "Joe", "Biology", 3.5)
    print(str(student1))
    student2 = n("Doe", "John", "Math", 3.0)
    print(str(student2))
    unittest.main()
def main():
    __name__()

