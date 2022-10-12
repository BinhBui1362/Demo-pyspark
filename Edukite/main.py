from components import Data
from components import Population
from components.DisplayMgr import DisplayMgr
from components.GeneticAlgorithm import GeneticAlgorithm
import time

POPULATION_SIZE = 20
NUMB_OF_ELITE_SCHEDULES = 1
ROULETTE_SELECTION_SIZE = 0
MUTATION_RATE = 0.2

grade = int(input('Nhập khối: '))
start = time.time()
data = Data.Data(grade)
displayMgr = DisplayMgr(data)
displayMgr.print_available_data()
generationNumber = 0
print("\n> Generation # " + str(generationNumber))
population = Population.Population(POPULATION_SIZE, data)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
displayMgr.print_generation(population)
displayMgr.print_schedule_as_table(population.get_schedules()[0])
geneticAlgorithm = GeneticAlgorithm(data, NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE, MUTATION_RATE, ROULETTE_SELECTION_SIZE)

while generationNumber < 20:
    generationNumber += 1
    print("\n> Generation # " + str(generationNumber))
    population = geneticAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    displayMgr.print_generation(population)
    displayMgr.print_schedule_as_table(population.get_schedules()[0])
    displayMgr.writeToJsonFile(population.get_schedules()[0])
    print("\n\n")
end = time.time()
elapse = end - start
print(f"Runtime: {elapse}")