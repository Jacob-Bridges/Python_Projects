# Jacob Bridges
# 3/23/24
# Random Sets Program

def main():
    import random
    set1 = set()
    for i in range(0, 8):
        ran_num = random.randint(1, 16)
        set1.add(ran_num)

    print(f'set1: {set1}')
    set2 = set()
    for i in range(0, 8):
        ran_num = random.randint(1, 16)
        set2.add(ran_num)
    print(f'set2: {set2}')
    set3 = set1.union(set2)
    print(f'Union of set1 and set2: {set3}')
    set3 = set1.intersection(set2)
    print(f'Intersection of set1 and set2: {set3}')
    set3 = set1.difference(set2)
    print(f'Difference of set1 and set2: {set3}')
    set3 = set1.symmetric_difference(set2)
    print(f'Symmetric difference of set1 and set2: {set3}')
    set3 = {item for item in set1.union(set2) if item < 10}
    print(f'Less than 10 in union of set1 and set2: {set3}')


main()
