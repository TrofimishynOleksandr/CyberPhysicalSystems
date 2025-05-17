import unittest
from lorenz import LorenzAttractor
import numpy as np

class TestLorenzAttractor(unittest.TestCase):
    def setUp(self):
        self.model = LorenzAttractor()

    def test_initial_step(self):
        initial = [1.0, 1.0, 1.0]
        result = self.model.step(initial, dt=0.01)
        self.assertEqual(len(result), 3)

    def test_generate_trajectory_length(self):
        traj = self.model.generate([1.0, 1.0, 1.0], dt=0.01, steps=1000)
        self.assertEqual(traj.shape, (1000, 3))

    def test_sensitivity_to_initial_conditions(self):
        traj1 = self.model.generate([1.0, 1.0, 1.0], steps=10000)
        traj2 = self.model.generate([1.0001, 1.0001, 1.0001], steps=10000)
        diff = np.linalg.norm(traj1 - traj2, axis=1)
        max_diff = np.max(diff)
        self.assertGreater(max_diff, 10.0, f"Очікуване велике відхилення, але отримано лише {max_diff}")


if __name__ == "__main__":
    unittest.main()
