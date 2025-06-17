

# f = open("file.txt")
# data = f.read()
# print(data)
# f.close


# by using with we don't need explecitly close the file
with open("file2.txt", "a") as f:
    f.write("\nHey govind you are so genius")
