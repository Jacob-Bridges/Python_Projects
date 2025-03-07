# Jacob Bridges
# 2/17/24
# List Comprehension

def main():
    list1 = [4, 5, 8, 2]
    list2 = [2, 5, 9]
    list3 = [num * 2 - 3 for num in range(6)]
    list4 = [[i, j] for i in range(4) for j in range(5) if i % 2 == 1 and j % 2 == 0]
    list5 = [i ** 3 for i in list1]
    # I'm not sure what the last steps are asking
    list8 = [[list1[i], '@', list2[j]] for i in range(len(list1)) for j in range(len(list2))]

    print(f'Step b: {list3}')
    print(f'Step c: {list4}')
    print(f'Step d: {list5}')
    list6 = [int(input('Enter Sequence for this list: ')) for i in list1]
    print(f'Step e: {list6}')
    list7 = [int(input('Enter Sequence for this list: ')) for i in list1 for j in list2]
    print(f'Step f: {list7}')
    print(f'Step g: {list8}')


# Call the main function
main()
