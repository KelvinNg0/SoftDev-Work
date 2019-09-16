import random

def inputCSV():
    csv = open("occupations.csv", "r")
    dict = {}
    for line in csv:
        values = line.replace("\n", "").split(',')
        if(values[0] != "Job Class" and values[0] != "Total"):
            if(values[0].find("\"") != -1):
                counter = 1
                temp = values[0]
                while(values[counter].find("\"") == -1):
                    temp += values[counter]
                    counter += 1
                temp += values[counter]
                dict[temp] = float(values[counter + 1])
            else:
                dict[values[0]] = float(values[1])
    return dict

def randomValue(dict):
    keys = []
    values = []
    for key in dict:
        keys.append(key)
        values.append(dict[key])
    return random.choices(keys, weights = values, k=1)


def main():
    print(randomValue(inputCSV()))

main()
