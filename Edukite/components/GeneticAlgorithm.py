from components import Population
import random as rnd
from components.Schedules import Schedule
from components import Lessons


class GeneticAlgorithm:
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    def __init__(self, inData, eliteSchedule, popSize, mutationRate, seletionSize):
        self._data = inData
        self._NUMB_OF_ELITE_SCHEDULES = eliteSchedule
        self._POPULATION_SIZE = popSize
        self._MUTATION_RATE = mutationRate
        self._ROULETTE_SELECTION_SIZE = seletionSize

    def _crossover_population(self, pop):
        crossover_pop = Population.Population(0, [])
        for i in range(self._NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = self._NUMB_OF_ELITE_SCHEDULES
        while i < self._POPULATION_SIZE:
            schedule1 = self._select_roulette(pop).get_schedules()[0]
            schedule2 = self._select_roulette(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def _mutate_population(self, population):
        for i in range(self._NUMB_OF_ELITE_SCHEDULES, self._POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule(self._data).initialize()
        for i in range(0, len(crossoverSchedule.get_lessons())):
            if rnd.random() > 0.5:
                crossoverSchedule.get_lessons()[i] = schedule1.get_lessons()[i]
            else:
                crossoverSchedule.get_lessons()[i] = schedule2.get_lessons()[i]
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule):
        for i in range(0, len(mutateSchedule.get_lessons())):
            random1 = rnd.randrange(0, len(mutateSchedule.get_lessons()))
            random2 = rnd.randrange(0, len(mutateSchedule.get_lessons()))
            temp = Lessons.Lesson(0)
            if self._MUTATION_RATE > rnd.random():
                temp.set_lesson_teacher(mutateSchedule.get_lessons()[random1].get_lesson_teacher())
                mutateSchedule.get_lessons()[random1].set_lesson_teacher(
                    mutateSchedule.get_lessons()[random2].get_lesson_teacher())
                mutateSchedule.get_lessons()[random2].set_lesson_teacher(temp.get_lesson_teacher())
        return mutateSchedule

    def _select_roulette(self, pop):
        roulette_pop = Population.Population(0, [])
        i = 0
        while i < self._ROULETTE_SELECTION_SIZE:
            fitness_list = []
            select_rate = rnd.random()
            schedules = pop.get_schedules()
            for j in range(0, len(schedules)):
                fitness_list.append(schedules[j].get_fitness())
            scale_fitness_list = self._scale_fitness(fitness_list)
            for n in range(0, len(scale_fitness_list)):
                if select_rate < scale_fitness_list[n]:
                    roulette_pop.get_schedules().append(schedules[n])
            i += 1
        roulette_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return roulette_pop

    def _scale_fitness(self, sumList):
        scaledList = []
        cumulativeList = []
        cumulativeValue = 0.0
        total = 0
        for i in range(0, len(sumList)):
            total += sumList[i]
        for i in range(0, len(sumList)):
            scaledList.append(sumList[i] / total)
        for i in range(0, len(scaledList)):
            cumulativeValue += scaledList[i]
            cumulativeList.append(cumulativeValue)
        return cumulativeList
