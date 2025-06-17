'''Parallel Columbus
'''

def unique_discoveries(M, columbus_data):
    discoveries = set()

    for data in columbus_data:

        identifier, discovery_list = data.split(":")
        discovery_list = discovery_list.strip()[1:-1].split(", ")  


        discoveries.update(discovery_list)

    return len(discoveries)


M = 3
columbus_data = [
    "Columbus1: [America, India]",
    "Columbus2: [India, Japan]",
    "Columbus3: [America, Japan, Australia]"
]

print(unique_discoveries(M, columbus_data))



