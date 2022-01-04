import os
import json


dir = "exampleDir"
# tree2 = {}
# tree2["exampleDir/foobar"] = ["exec", "DS_store"]
tree = {}
# tree[dir] = [tree2]


# result = json.dumps(tree, indent = 2)




def crawl_dir(dir, prev_tree):
    dir_contents = os.listdir(dir)        # get list of files and directories in the given directory
    current_tree = {}
    folder = []
    prev_tree[dir] = folder

    for path in dir_contents:
        path = os.path.join(dir, path)    # create full file path
        if os.path.isdir(path):

            crawl_dir(path, prev_tree)
    
        folder.append(path)
    return prev_tree
    


output = crawl_dir(dir, tree)
json_tree = json.dumps(output, indent=2)
print(json_tree)


# json_data = json.dumps(dir_tree)
#print(json_data)

# result = os.listdir(path)
# print(result)