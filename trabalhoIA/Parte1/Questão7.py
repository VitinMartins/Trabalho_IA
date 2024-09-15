import numpy as np
import matplotlib.pyplot as plt

def objective_function(x):
    x1, x2 = x
    term1 = -np.sin(x1) * (np.sin(x1**2 / np.pi))**(2 * 10)
    term2 = -np.sin(x2) * (np.sin(2 * x2**2 / np.pi))**(2 * 10)
    return term1 - term2

def random_candidate():
    return np.array([np.random.uniform(0, np.pi), np.random.uniform(0, np.pi)])

def hill_climbing(epsilon=0.1, max_iterations=10000, t=100):
    x_best = np.array([0.0, 0.0]) 
    best_score = objective_function(x_best)
    no_improvement_count = 0

    history = []
    
    for i in range(max_iterations):
        y = x_best + np.random.uniform(-epsilon, epsilon, 2)
        y[0] = np.clip(y[0], 0, np.pi)  
        y[1] = np.clip(y[1], 0, np.pi) 

        current_score = objective_function(y)
        
        if current_score < best_score:
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
        y[0] = np.clip(y[0], 0, np.pi) 
        y[1] = np.clip(y[1], 0, np.pi)  

        current_score = objective_function(y)

        if current_score < best_score:
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

        if current_score < best_score:
            x_best = y
            best_score = current_score

        history.append(x_best)

    return x_best, history

def plot_3d_surface(history_hill, history_lrs, history_grs):
    x = np.linspace(0, np.pi, 400)
    y = np.linspace(0, np.pi, 400)
    x_grid, y_grid = np.meshgrid(x, y)
    z_grid = (-np.sin(x_grid) * (np.sin(x_grid**2 / np.pi))**(2 * 10) 
              - np.sin(y_grid) * (np.sin(2 * y_grid**2 / np.pi))**(2 * 10))

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x_grid, y_grid, z_grid, cmap='viridis', alpha=0.6, edgecolor='none')

    def plot_history(history, label, color):
        x_vals = [point[0] for point in history]
        y_vals = [point[1] for point in history]
        z_vals = [objective_function(point) for point in history]
        ax.plot(x_vals, y_vals, z_vals, color=color, label=label, linewidth=2)

    plot_history(history_hill, 'Hill Climbing', 'r')
    plot_history(history_lrs, 'Local Random Search', 'b')
    plot_history(history_grs, 'Global Random Search', 'g')

    ax.set_title("Minimização da função objetivo em 3D")
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
