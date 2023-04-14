#!/usr/bin/python3


with open("./notes01.md") as file:
    content = file.readlines()
    result = []
    for i in range(len(content) - 1, -1, -1):
        result.append(content[i])
    with open("./output.txt", "w") as out:
        out.writelines(result)



