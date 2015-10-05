import unittest
from bsearch import bsearch
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_0(self):
        a=[]
        a.sort()
        self.assertEqual( bsearch(a,0), 0)
 
    def test_small_array(self):
        a=[12,23,56,78,9,-90,4]
        a.sort()
        self.assertEqual( bsearch(a,9), 1)
 
if __name__ == '__main__':
    unittest.main()
