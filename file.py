import vysye
import unittest
class testvysye(unittest.TestCase):
    def test_add(self):
        self.assertEqual(vysye.add(10,10),20)
        self.assertEqual(vysye.add(12.2,12.2),24.4)
    def test_sub(self):
        self.assertEqual(vysye.sub(10, 10), 20)
        self.assertEqual(vysye.sub(12.2, 12.2), 24.4)
if __name__=="__main__":
    unittest.main()