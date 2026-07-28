# Genetic Algorithm for Optimization

population = [5, 12, 8, 20, 15]

print("Initial Population:", population)

best = max(population)
print("Best Solution:", best)

child = (population[1] + population[3]) // 2
print("New Child:", child)

population.append(child)

best = max(population)
print("Optimized Solution:", best)