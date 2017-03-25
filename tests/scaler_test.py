import unittest
from controllers.scaler import Scale


class ScalerTestCase(unittest.TestCase):
    def test_scale_input(self):
        scale = Scale(scale_out_max=1, scale_in_max=100, scale_out_min=0, scale_in_min=0)
        value = 50
        scaled = scale.input(value)
        self.assertEqual(scaled, 0.5)

        value = 100
        scaled = scale.input(value)
        self.assertEqual(scaled, 1)

        value = 200
        scaled = scale.input(value)
        self.assertEqual(scaled, 2)

    def test_scale_output(self):
        scale = Scale(scale_out_max=100, scale_in_max=1, scale_out_min=0, scale_in_min=0)

        value = 0.5
        scaled = scale.input(value)
        self.assertEqual(scaled, 50)

        value = 1
        scaled = scale.input(value)
        self.assertEqual(scaled, 100)

        value = 2
        scaled = scale.input(value)
        self.assertEqual(scaled, 200)


if __name__ == '__main__':
    unittest.main()
