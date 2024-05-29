
########### Write element by element in my file ##################
animals = ["fish", "dog", "cat"]

with open("zoo2.txt", "w") as filout:
    for animal in animals:
        filout.write(animal + "\n")
exit(-2)

# Readlines: all the file in a list of list every line is a list #
# with open("Zoo_1.txt", 'r') as filin:
# 	lines = filin.readlines()
# print(lines)
# print(lines[0][0])
#print(lines[0][0])
	# for line in lines:
	# 	print(line)
#exit(-2)

########## Readline: line by line, each line is a list ###########
# with open("Zoo_1.txt", "r") as filin:
#     line = filin.readline()
#     #print(line)
#     while line != "":
#         print(line)
#         #print(line[0])
#         line = filin.readline()
# exit(-2)

########## Iterate over the line of your file ###################
# with open("Zoo_1.txt", "r") as filin:
#     print(filin)
#     for line in filin:
#         #print(line)
# exit(-2)

########### Read: All the file as one list #######################
# with open("Zoo_1.txt", "r") as filin:
# 	    content = filin.read()
# print(content[0:8])

#exit(-2)

##################################################################