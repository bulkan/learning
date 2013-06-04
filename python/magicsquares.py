from pyevolve import G2DList
from pyevolve import GSimpleGA
from pyevolve import Consts
from pyevolve import Selectors

class G(list):
    def getWidth(self):
        return 3

    def getHeight(self):
        return 3

g = G([ (8,1,6),
        (3,5,7),
        (4,9,2)
])


def sumall(genome):
    unique = set()

    colsum = {}
    for i in range(genome.getWidth()):
        colsum.setdefault(i,0)

    d1 = 0
    d2 = 0

    nums = set()

    for i, row in enumerate(genome):
        for c in range(genome.getHeight()):
            # col sum
            colsum[i] += genome[c][i]

        # diag sum
        d1 += genome[i][i]
        d2 += genome[i][len(row) - (i+1)]

        s = 0
        # row sum and number uniqueness
        for n in row: 
            nums.add(n)
            s+=n

        unique.add(s)

    sums = colsum.values()
    sums.extend([d1,d2])

    for v in sums:
        unique.add(v)

    return unique, colsum, d1, d2, nums


def eval_func(genome):

    unique_sums, colsum, d1, d2, nums = sumall(genome)

    score = 0

    if len(nums) < 9:
        score = 0.5

    if len(unique_sums) > 1:
        score = ((genome.getHeight() * 2) + 2) - len(unique_sums)

    elif d1 != d2:
        score = genome.getHeight() * 2 - len(unique_sums)

    return score


def main():


    genome = G2DList.G2DList(3, 3)
    genome.evaluator.set(eval_func)
    genome.setParams(rangemin=1, rangemax=9)
    #max_score = genome.getHeight() * genome.getWidth() * 10 
    #genome.setParams(bestRawScore=max_score*1000)

    ga = GSimpleGA.GSimpleGA(genome)
    ga.setGenerations(2000)
    ga.setElitism(True)
    ga.setMinimax(Consts.minimaxType["maximize"])
    #ga.setMutationRate(0.6)
    #ga.selector.set(Selectors.GRankSelector)
    #Selectors.GRouletteWheel
    #ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)
    #ga.terminationCriteria.set(GSimpleGA.RawScoreCriteria)

    ga.evolve(freq_stats=100)

    # Best individual
    print ga.bestIndividual()

    unique, colsum, d1, d2, nums = sumall(ga.bestIndividual())
    #unique, colsum, d1, d2, nums = sumall(g)

    print "Unique sums:  ", unique
    #print "Column sums: ", colsum
    print "nums: " , nums
    print "D1: " , d1
    print "D2: " , d2

    #print "score: ", eval_func(g) 

if __name__ == '__main__':
    main()
