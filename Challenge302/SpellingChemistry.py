import csv


def create_lookup():
    input_file = csv.DictReader(open("data.csv"))
    look_table = {}
    for row in input_file:
        look_table[row['SI Symbol'].strip()] = row['Element'].strip()
    return look_table


def chemistry_word(word, table):
    begin = 0
    end = 2
    answer = ''
    chemical = []
    while end <= len(word):
        for element in table:
            if word[begin:end].upper() == element.upper():
                answer += element
                chemical.append(table[element])
                begin += 2
                end += 2
                continue
            elif word[begin:end-1].upper() == element.upper():
                answer += element
                chemical.append(table[element])
                begin += 1
                end += 1
                continue
    return answer, chemical


challenge_inputs = ['functions', 'bacon', 'poison', 'sickness', 'ticklish']
lookup_table = create_lookup()

for x in challenge_inputs:
    solution = chemistry_word(x, lookup_table)
    word = solution[0]
    formulas = solution[1]
    plus = ', '
    print(word + ' (' + plus.join(formulas) + ')')
