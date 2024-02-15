import unittest
from calculate import calculate_root_complex, calculate_root


class TestCalculate(unittest.TestCase):

    def test_calculate_root_complex_positive_real(self):
        self.assertEqual(calculate_root_complex(4, 2), (2 + 0j))

    def test_calculate_root_complex_complex_number(self):
        self.assertAlmostEqual(calculate_root_complex(1 + 1j, 2).real, 1.0987, places=4)
        self.assertAlmostEqual(calculate_root_complex(1 + 1j, 2).imag, 0.4551, places=4)

    def test_calculate_root_positive(self):
        self.assertAlmostEqual(calculate_root(16, 2, 10), 4)

    def test_calculate_root_zero(self):
        self.assertEqual(calculate_root(0, 3, 10), 0)


if __name__ == '__main__':
    unittest.main()
