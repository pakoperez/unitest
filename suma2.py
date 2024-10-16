import unittest

from suma import suma

class testSuma(unittest.TestCase):         
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
    def test_sumadecimales(self):    
        self.assertEqual(suma(2.5, 3.5), 6)
    def test_sumacombinada(self):    
        self.assertEqual(suma(2, 3.5), 5.5)
    def test_sumamal(self):    
         with self.assertRaises(TypeError):
            suma(2, "texto")

if __name__== '__main__':
    unittest.main()    