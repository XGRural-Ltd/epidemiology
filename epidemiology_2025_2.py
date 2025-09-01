import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

AUTHOR = 'Kelves N D Costa'
# Definição dos estados
SUSCEPTIBLE = 0  # Saudável
INFECTED = 1     # Infectado
RECOVERED = 2    # Recuperado / Imune
DEAD = 3         # Morto

# Parâmetros da simulação
grid_size = 50  # Tamanho da grade
timesteps = 100  # tempo
infection_rate = 0.3  # Probabilidade de infecção
recovery_rate = 0.1  # Probabilidade de recuperação
mortality_rate = 0.02  # Probabilidade de morte
vaccination_rate = 0.005  # Taxa de vacinação
isolation = True  # Controle de isolamento social

# Inicialização da grade
grid = np.zeros((grid_size, grid_size), dtype=int)

# Posicionar alguns infectados iniciais
num_initial_infected = 5
for _ in range(num_initial_infected):
    x, y = np.random.randint(0, grid_size, 2)
    grid[x, y] = INFECTED

# Função para atualizar a grade
def update(frame):
    global grid
    new_grid = grid.copy()
    
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x, y] == INFECTED:
                # Probabilidade de recuperação ou morte
                if np.random.rand() < recovery_rate:
                    new_grid[x, y] = RECOVERED
                elif np.random.rand() < mortality_rate:
                    new_grid[x, y] = DEAD
                else:
                    # Espalhamento para vizinhos
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if (dx == 0 and dy == 0) or (isolation and np.random.rand() < 0.5):
                                continue
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                                if grid[nx, ny] == SUSCEPTIBLE and np.random.rand() < infection_rate:
                                    new_grid[nx, ny] = INFECTED
            
            # Vacinação
            if grid[x, y] == SUSCEPTIBLE and np.random.rand() < vaccination_rate:
                new_grid[x, y] = RECOVERED
    
    grid = new_grid
    mat.set_data(grid)
    return [mat]

# Configuração da visualização
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap='viridis')
ani = animation.FuncAnimation(fig, update, frames=timesteps, interval=200, blit=False)
plt.show()
