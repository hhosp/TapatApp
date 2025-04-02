import unittest

def resta(a, b):
    return a - b

def divideix(a, b):
    if b == 0:
        return "Error, divisio entre zero"
    return a /b

class TestResta(unittest.TestCase):
    def test_resta(self):
        return self.assertEqual(resta(15, 10), 5)
    
class TestDivisio(unittest.TestCase):
    def test_divisio(self):
        return self.assertEqual(divideix(500, 5), 100)
    
if __name__ == "__main__":
    unittest.main()