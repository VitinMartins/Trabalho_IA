import numpy as np

def f(x1, x2):
    term1 = -(x2 + 47) * np.sin(np.sqrt(np.abs(x1 / 2 + (x2 + 47))))
    term2 = -x1 * np.sin(np.sqrt(np.abs(x1 - (x2 + 47))))
    return term1 + term2

def hill_climbing_min(iterations=10000, step_size=0.1, stop_early=100):
    x1, x2 = np.random.uniform(-200, 200), np.random.uniform(-200, 200)  
    best = f(x1, x2)
    no_improvement = 0

    for _ in range(iterations):
        x1_new = x1 + np.random.uniform(-step_size, step_size)
        x2_new = x2 + np.random.uniform(-step_size, step_size)

        if -200 <= x1_new <= 200 and -200 <= x2_new <= 200:
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

def lrs_min(iterations=10000, sigma=10):
    x1, x2 = np.random.uniform(-200, 200), np.random.uniform(-200, 200)  
    best = f(x1, x2)

    for _ in range(iterations):
        x1_new = x1 + np.random.normal(0, sigma)
        x2_new = x2 + np.random.normal(0, sigma)

        if -200 <= x1_new <= 200 and -200 <= x2_new <= 200:
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
        x1 = np.random.uniform(-200, 200)
        x2 = np.random.uniform(-200, 200)
        value = f(x1, x2)

        if value < best:  
            best_x1, best_x2 = x1, x2
            best = value

    return best_x1, best_x2, best

x1, x2, best_value = grs_min()
print(f"GRS: x1 = {x1:.3f}, x2 = {x2:.3f}, f(x1, x2) = {best_value:.3f}")


