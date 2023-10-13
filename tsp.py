from random import randint

V = 7
genes = "ABCDEFG"
start = 0
pop_size = 10

class individual:
    def __init__(self) -> None:
        self.gnome = ""
        self.fitness = 0

    def __lt__(self, other):
        return self.fitness < other.fitness
    
    def __gt__(self, other):
        return self.fitness > other.fitness

def rand_num(start, end):
    return randint(start, end-1)
 
def repeat(s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            return True
 
    return False

def mutatedGene(gnome):
    gnome = list(gnome)
    while True:
        r = rand_num(1, V)
        r1 = rand_num(1, V)
        if r1 != r:
            temp = gnome[r]
            gnome[r] = gnome[r1]
            gnome[r1] = temp
            break
    return ''.join(gnome)

def create_gnome():
    gnome = "0"
    while True:
        if len(gnome) == V:
            gnome += gnome[0]
            break
 
        temp = rand_num(1, V)
        if not repeat(gnome, chr(temp + 48)):
            gnome += chr(temp + 48)
 
    return gnome

def cal_fitness(gnome):
    tsp = [ 
    [0, 12, 10, float('inf'), float('inf'), float('inf'), 12],
    [12, 0, 8, 12, float('inf'), float('inf'), float('inf')],
    [10, 8, 0, 11, 3, float('inf'), 9],
    [float('inf'), 12, 11, 0, 11, 10, float('inf')],
    [float('inf'), float('inf'), 3, 11, 0, 6, 7],
    [float('inf'), float('inf'), float('inf'), 10, 6, 0, 9],
    [12, float('inf'), 9, float('inf'), 7, 9, 0]
    ]
    f = 0
    for i in range(len(gnome) - 1):
        if tsp[ord(gnome[i]) - 48][ord(gnome[i + 1]) - 48] == float('inf'):
            return float('inf')
        f += tsp[ord(gnome[i]) - 48][ord(gnome[i + 1]) - 48]
 
    return f


def cooldown(temp):
    return (90 * temp) / 100

def TSPUtil(mp):
    gen = 1
    gen_thres = 100
 
    population = []
    temp = individual()
 
    for i in range(pop_size):
        temp.gnome = create_gnome()
        temp.fitness = cal_fitness(temp.gnome)
        population.append(temp)
 
    print("\nInitial population: \nGNOME     FITNESS VALUE\n")
    for i in range(pop_size):
        print(population[i].gnome, population[i].fitness)
    print()
 
    found = False
    temperature = 10000
 
    while temperature > 1000 and gen <= gen_thres:
        population.sort()
        print("\nCurrent temp: ", temperature)
        new_population = []
 
        for i in range(pop_size):
            p1 = population[i]
 
            while True:
                new_g = mutatedGene(p1.gnome)
                new_gnome = individual()
                new_gnome.gnome = new_g
                new_gnome.fitness = cal_fitness(new_gnome.gnome)
 
                if new_gnome.fitness <= population[i].fitness:
                    new_population.append(new_gnome)
                    break
 
                else:
 
                    prob = pow(
                        2.7,
                        -1
                        * (
                            (float)(new_gnome.fitness - population[i].fitness)
                            / temperature
                        ),
                    )
                    if prob > 0.5:
                        new_population.append(new_gnome)
                        break
 
        temperature = cooldown(temperature)
        population = new_population
        print("Generation:", gen)
        print("GENOME     FITNESS VALUE")
 
        for i in range(pop_size):
            print(population[i].gnome, population[i].fitness)
        gen += 1
 

tsp = [ 
    [0, 12, 10, float('inf'), float('inf'), float('inf'), 12],
    [12, 0, 8, 12, float('inf'), float('inf'), float('inf')],
    [10, 8, 0, 11, 3, float('inf'), 9],
    [float('inf'), 12, 11, 0, 11, 10, float('inf')],
    [float('inf'), float('inf'), 3, 11, 0, 6, 7],
    [float('inf'), float('inf'), float('inf'), 10, 6, 0, 9],
    [12, float('inf'), 9, float('inf'), 7, 9, 0]
    ]
TSPUtil(tsp)
