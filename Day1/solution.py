ints = '123456789'

# Replace 'your_file.txt' with the path to your text file
file_path = 'input.txt'

# Open and read the file
with open(file_path, 'r') as file:
    lines = file.readlines()

def dayOne(text, ints, arr = []):
    tempArr = []
    for i in range(len(text)):
        if text[i] in ints:
            tempArr.append(int(text[i]))
    arr.append(tempArr[0]*10 + tempArr[-1])
    return arr

solution = []
for i in range(len(lines)):
    dayOne(lines[i], ints, solution)

finalSolution = 0
for i in range(len(solution)):
    finalSolution = finalSolution + solution[i]

print(finalSolution)