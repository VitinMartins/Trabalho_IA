import numpy as np
import matplotlib.pyplot as plt

def objective_function(x):
    return np.exp(-(x[0]**2 + x[1]**2)) + 2 * np.exp(-((x[0] - 1.7)**2 + (x[1] - 1.7)**2))

def random_candidate():
    return np.array([np.random.uniform(-2, 4), np.random.uniform(-2, 5)])

def hill_climbing(epsilon=0.1, max_iterations=10000, t=100):
    x_best = np.array([-2.0, -2.0])
    best_score = objective_function(x_best)
    no_improvement_count = 0

    history = []
    
    for i in range(max_iterations):
        y = x_best + np.random.uniform(-epsilon, epsilon, 2)
        y[0] = np.clip(y[0], -2, 4) 
        y[1] = np.clip(y[1], -2, 5) 

        current_score = objective_function(y)
        
        if current_score > best_score:
            x_best = y
            best_score = current_score
            no_improvement_count = 0
        else:
            no_improvement_count += 1

        history.append(x_best) 

        if no_improvement_count >= t:
            break

    return x_best, history

def local_random_search(sigma=0.1, max_iterations=10000, t=100):
    x_best = random_candidate()
    best_score = objective_function(x_best)
    no_improvement_count = 0

    history = []

    for i in range(max_iterations):
        y = x_best + np.random.normal(0, sigma, 2)
        y[0] = np.clip(y[0], -2, 4)
        y[1] = np.clip(y[1], -2, 5) 

        current_score = objective_function(y)

        if current_score > best_score:
            x_best = y
            best_score = current_score
            no_improvement_count = 0
        else:
            no_improvement_count += 1

        history.append(x_best)

        if no_improvement_count >= t:
            break

    return x_best, history

def global_random_search(max_iterations=10000):
    x_best = random_candidate()
    best_score = objective_function(x_best)

    history = []

    for i in range(max_iterations):
        y = random_candidate()

        current_score = objective_function(y)

        if current_score > best_score:
            x_best = y
            best_score = current_score

        history.append(x_best)

    return x_best, history

def plot_3d_surface(history_hill, history_lrs, history_grs):
    x = np.linspace(-2, 4, 400)
    y = np.linspace(-2, 5, 400)
    x_grid, y_grid = np.meshgrid(x, y)
    z_grid = np.exp(-(x_grid**2 + y_grid**2)) + 2 * np.exp(-((x_grid - 1.7)**2 + (y_grid - 1.7)**2))

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x_grid, y_grid, z_grid, cmap='plasma', alpha=0.6, edgecolor='none')

    def plot_history(history, label, color):
        x_vals = [point[0] for point in history]
        y_vals = [point[1] for point in history]
        z_vals = [objective_function(point) for point in history]
        ax.plot(x_vals, y_vals, z_vals, color=color, label=label, linewidth=2)

    plot_history(history_hill, 'Hill Climbing', 'r')
    plot_history(history_lrs, 'Local Random Search', 'b')
    plot_history(history_grs, 'Global Random Search', 'g')

    ax.set_title("Maximização da função objetivo em 3D")
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("f(x1, x2)")
    ax.legend()

    plt.show()

hill_best, hill_history = hill_climbing()
lrs_best, lrs_history = local_random_search()
grs_best, grs_history = global_random_search()

plot_3d_surface(hill_history, lrs_history, grs_history)

print(f'Hill Climbing melhor solução: {hill_best}, valor: {objective_function(hill_best):.3f}')
print(f'Local Random Search melhor solução: {lrs_best}, valor: {objective_function(lrs_best):.3f}')
print(f'Global Random Search melhor solução: {grs_best}, valor: {objective_function(grs_best):.3f}')
