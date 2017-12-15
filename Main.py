from SequenceParser import *
from Greedy import Greedy
from DPXDrop import DPXDrop

data_set1 = SequenceParser.GenBank("data/test_data.txt")

division = 100  # length of input string for DXDrop algorithm

f = open("data/results.txt", 'w')

for i in range(0, len(data_set1), 2):
    pair = [data_set1[i], data_set1[i+1]]
    if len(pair[0].sequence) > len(pair[1].sequence):
        iterations = len(pair[0].sequence) // division + 1
    else:
        iterations = len(pair[1].sequence) // division + 1
    drop_sum = 0
    for j in range(iterations):
        piece1 = pair[0].sequence[division * j:division * j + division]
        piece2 = pair[1].sequence[division * j:division * j + division]
        drop = DPXDrop(Sequence(0, piece1), Sequence(1, piece2))
        drop_sum += drop.main()

    result = [str(len(pair[0].sequence)), str(len(pair[1].sequence))]
    result.append(str(drop_sum))
    result.append(str(Greedy(*pair).main()))
    f.write("{} {} {} {}\n".format(*result))
f.close()
