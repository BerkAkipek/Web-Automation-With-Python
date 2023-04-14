#!/usr/bin/python3


# Read files 
file = open("/home/berk/web-automation-python/read_write_python/notes01.md")
# content = file.read()

# file.readlines() -> read all content returns a list

lines = file.readlines()
for line in lines:
    print(line)


file.close()


