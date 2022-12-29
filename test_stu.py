import unittest
from student import student
class test_student(unittest.TestCase):
    def setUp(self):
        print("setup")
    def tearDown(self):
        print("teardown")
    def test_email(self):
        obj = student("vyshnavi", "nalam", 50)
        print("mail")
        self.assertEqual(obj.email,'vyshnavi.nalam@gmail.com')
    def test_something(self):
        obj=student("vyshnavi", "nalam", 50)
        obj.something()
        self.assertEqual(obj.some_thing,"vyshnavinalam")
if __name__=="__main__":
    unittest.main()