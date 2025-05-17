import numpy as np

class LorenzAttractor:
    def __init__(self, sigma=10.0, rho=28.0, beta=8.0/3.0):
        self.sigma = sigma
        self.rho = rho
        self.beta = beta

    def step(self, state, dt):
        x, y, z = state
        dx = self.sigma * (y - x)
        dy = x * (self.rho - z) - y
        dz = x * y - self.beta * z
        return np.array([x + dx * dt, y + dy * dt, z + dz * dt])

    def generate(self, initial_state, dt=0.01, steps=10000):
        trajectory = np.empty((steps, 3))
        state = np.array(initial_state)
        for i in range(steps):
            trajectory[i] = state
            state = self.step(state, dt)
        return trajectory
