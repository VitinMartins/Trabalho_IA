import numpy as np

def f(x1, x2):
    return -np.sin(x1) * np.sin((x1**2 / np.pi)**2.10) - np.sin(x2) * np.sin((2 * x2**2 / np.pi)**2.10)

def hill_climbing_min(iterations=10000, step_size=0.1, stop_early=100):
    x1, x2 = np.random.uniform(0, np.pi), np.random.uniform(0, np.pi)  
    best = f(x1, x2)
    no_improvement = 0

    for _ in range(iterations):
        x1_new = x1 + np.random.uniform(-step_size, step_size)
        x2_new = x2 + np.random.uniform(-step_size, step_size)

        if 0 <= x1_new <= np.pi and 0 <= x2_new <= np.pi:
            value_new = f(x1_new, x2_new)
            if value_new < best:  
                x1, x2 = x1_new, x2_new
                best = value_new
                no_improvement = 0
            else:
                no_improvement += 1

        if no_improvement > stop_early:
            break

    return x1, x2, best

x1, x2, best_value = hill_climbing_min()
print(f"Hill Climbing: x1 = {x1:.3f}, x2 = {x2:.3f}, f(x1, x2) = {best_value:.3f}")

def lrs_min(iterations=10000, sigma=0.1):
    x1, x2 = np.random.uniform(0, np.pi), np.random.uniform(0, np.pi) 
    best = f(x1, x2)

    for _ in range(iterations):
        x1_new = x1 + np.random.normal(0, sigma)
        x2_new = x2 + np.random.normal(0, sigma)

        if 0 <= x1_new <= np.pi and 0 <= x2_new <= np.pi:
            value_new = f(x1_new, x2_new)
            if value_new < best: 
                x1, x2 = x1_new, x2_new
                best = value_new

    return x1, x2, best

x1, x2, best_value = lrs_min()
print(f"LRS: x1 = {x1:.3f}, x2 = {x2:.3f}, f(x1, x2) = {best_value:.3f}")

def grs_min(iterations=10000):
    best = np.inf
    best_x1, best_x2 = None, None

    for _ in range(iterations):
        x1 = np.random.uniform(0, np.pi)
        x2 = np.random.uniform(0, np.pi)
        value = f(x1, x2)

        if value < best:  
            best_x1, best_x2 = x1, x2
            best = value

    return best_x1, best_x2, best

x1, x2, best_value = grs_min()
print(f"GRS: x1 = {x1:.3f}, x2 = {x2:.3f}, f(x1, x2) = {best_value:.3f}")

