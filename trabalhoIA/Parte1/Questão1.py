import numpy as np

def hc(func, x_bounds, s=0.1, max_iter=10000, t=100):
    x1_min, x1_max = x_bounds
    x2_min, x2_max = x_bounds
    current_x1 = np.random.uniform(x1_min, x1_max)  # Inicialização aleatória
    current_x2 = np.random.uniform(x2_min, x2_max)
    best_x1, best_x2 = current_x1, current_x2
    best_value = func(best_x1, best_x2)
    
    for i in range(max_iter):
        # Gera mais vizinhos variando x1 e x2 simultaneamente e separadamente
        neighbors = [
            (best_x1 + np.random.uniform(-s, s), best_x2 + np.random.uniform(-s, s)),
            (best_x1 + np.random.uniform(-s, s), best_x2),
            (best_x1, best_x2 + np.random.uniform(-s, s)),
            (best_x1 - np.random.uniform(-s, s), best_x2 - np.random.uniform(-s, s)),
            (best_x1 - np.random.uniform(-s, s), best_x2),
            (best_x1, best_x2 - np.random.uniform(-s, s)),
        ]
        
        # Testa os vizinhos gerados
        for x1_new, x2_new in neighbors:
            if x1_min <= x1_new <= x1_max and x2_min <= x2_new <= x2_max:
                value = func(x1_new, x2_new)
                if value < best_value:
                    best_x1, best_x2 = x1_new, x2_new
                    best_value = value
        
        # Reduz gradualmente o passo de perturbação ao longo das iterações
        if i % t == 0:
            s *= 0.995  # Redução mais lenta do valor de s
            if best_value == func(best_x1, best_x2):
                break  # Interrompe se não houver melhora no valor de f(x1, x2)

    return best_x1, best_x2, best_value

# Função objetivo: f(x1, x2) = x1^2 + x2^2
def objective_function(x1, x2):
    return x1**2 + x2**2

# Definição dos limites para x1 e x2
bounds = (-100, 100)

# Execução do algoritmo Hill Climbing
result = hc(objective_function, bounds)
print(f"Melhor solução: x1 = {result[0]:.3f}, x2 = {result[1]:.3f}, f(x1, x2) = {result[2]:.3f}")



def lrs(func, x_bounds, sigma=0.1, max_iter=10000):
    x1_min, x1_max = x_bounds
    x2_min, x2_max = x_bounds
    best_x1 = np.random.uniform(x1_min, x1_max)
    best_x2 = np.random.uniform(x2_min, x2_max)
    best_value = func(best_x1, best_x2)
    
    for _ in range(max_iter):
        x1_new = np.random.normal(best_x1, sigma)
        x2_new = np.random.normal(best_x2, sigma)
        if x1_min <= x1_new <= x1_max and x2_min <= x2_new <= x2_max:
            value = func(x1_new, x2_new)
            if value < best_value:
                best_x1, best_x2 = x1_new, x2_new
                best_value = value

    return best_x1, best_x2, best_value

result = lrs(objective_function, bounds)
print(f"Melhor solução: x1 = {result[0]:.3f}, x2 = {result[1]:.3f}, f(x1, x2) = {result[2]:.3f}")


def grs(func, x_bounds, max_iter=10000):
    x1_min, x1_max = x_bounds
    x2_min, x2_max = x_bounds
    best_x1 = np.random.uniform(x1_min, x1_max)
    best_x2 = np.random.uniform(x2_min, x2_max)
    best_value = func(best_x1, best_x2)
    
    for _ in range(max_iter):
        x1_new = np.random.uniform(x1_min, x1_max)
        x2_new = np.random.uniform(x2_min, x2_max)
        value = func(x1_new, x2_new)
        if value < best_value:
            best_x1, best_x2 = x1_new, x2_new
            best_value = value

    return best_x1, best_x2, best_value

result = grs(objective_function, bounds)
print(f"Melhor solução: x1 = {result[0]:.3f}, x2 = {result[1]:.3f}, f(x1, x2) = {result[2]:.3f}")
