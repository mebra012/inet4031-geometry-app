import unittest
import sphere

class sphereTest(unittest.TestCase):

    def test_volume1(self):
        self.assertAlmostEqual(sphere.volume(1), 4.1887902047863905)

    def test_volume2(self):
        self.assertAlmostEqual(sphere.volume(3), 113.09733552923255)

    def test_volume3(self):
        self.assertAlmostEqual(sphere.volume(0), 0.0)

if __name__ == '__main__':
    unittest.main()