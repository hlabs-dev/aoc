import aocd
input = aocd.get_data(day=4, year=2024).splitlines()

def rotate(input) :
    return list(map(list, zip(*input[ ::- 1]) ))

def flip(input):
    return [l[ ::- 1] for l in input]

def dediag(input) :
    return [[*line[i:], '#', *line[:i]] for i, line in enumerate(input) ]

def count_xmas(input) :
    return sum("".join(row).count("XMAS")+
               "".join(row).count("SAMX") for row in input)

def print_xmas(input) :
    for l in input:
        print("".join(l))
    print()

tot = 0
for _ in range(2):
    tot += count_xmas(input)
    print(tot)
    input = rotate(input)


tot += count_xmas(rotate(dediag(input) ))
print(tot)
tot += count_xmas(rotate(dediag(flip(input))))

print(tot)

def count_mas_cross(input) :
    return sum((c == line[i+2] == "M" and input [j+1] [i+1] == "A" and input [j+2] [i] == input [j+2] [i+2] == "S") for j,
               line in enumerate(input[ :- 2]) for i, c in enumerate(line[ :- 2]))

tot = 0
for _ in range(4):
    tot += count_mas_cross(input)
    input = rotate(input)

print(tot)