import matplotlib.pyplot as plt
from lorenz import LorenzAttractor

def plot_trajectories():
    model = LorenzAttractor()

    initial_state1 = [1.0, 1.0, 1.0]
    initial_state2 = [1.0001, 1.0001, 1.0001]

    traj1 = model.generate(initial_state1)
    traj2 = model.generate(initial_state2)

    fig = plt.figure(figsize=(12, 6))

    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot(traj1[:, 0], traj1[:, 1], traj1[:, 2], color='blue', label='Стан 1')
    ax1.plot(traj2[:, 0], traj2[:, 1], traj2[:, 2], color='red', label='Стан 2')
    ax1.set_title("Порівняння атракторів (3D)")
    ax1.legend()

    ax2 = fig.add_subplot(122)
    ax2.plot(traj1[:, 0], label='X1')
    ax2.plot(traj2[:, 0], label='X2')
    ax2.set_title("Похибка X з часом")
    ax2.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_trajectories()
