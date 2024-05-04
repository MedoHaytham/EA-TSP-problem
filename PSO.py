import numpy as np

filename = input("dataset/large.csv")

# Load TSP dataset
def load_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        cities = []
        for line in lines:
            city_id, x, y = map(float, line.split())
            cities.append((x, y))
        return cities


# Calculate distance between two cities
def distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Calculate total distance of a path
def total_distance(path, cities):
    dist = 0
    for i in range(len(path) - 1):
        dist += distance(cities[path[i]], cities[path[i + 1]])
    return dist

# Particle Swarm Optimization (PSO) for TSP
def pso_tsp(cities, num_particles, max_iter):
    num_cities = len(cities)
    # Initialize particles and velocities
    particles = np.random.permutation(num_cities)  # Initial permutation of cities
    velocities = np.zeros((num_particles, num_cities), dtype=int)
    # Initialize global best solution
    global_best = particles[np.argmin([total_distance(particles, cities) for _ in range(num_particles)])]
    for _ in range(max_iter):
        for i in range(num_particles):
            # Update velocity
            velocities[i] = np.random.permutation(num_cities)
            # Update position
            particles[i] = np.roll(particles[i], velocities[i][0])
            # Evaluate fitness
            if total_distance(particles[i], cities) < total_distance(particles[global_best], cities):
                global_best = i
    return particles[global_best]

# Load dataset
cities = load_data('dataset_1000.txt')
# PSO parameters
num_particles = 20
max_iter = 100
# Run PSO algorithm
best_path_pso = pso_tsp(cities, num_particles, max_iter)
print("Best path found by PSO:", best_path_pso)
print("Total distance:", total_distance(best_path_pso, cities))

