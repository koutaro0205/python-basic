import sys

COUNTRIES = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

def population_ranking(rank):
    if 0 < rank <= 10:
      return COUNTRIES[rank - 1]
    else:
      return "Error: Rank must be between 1 and 10."

rank = int(sys.argv[1])
print(population_ranking(rank))
