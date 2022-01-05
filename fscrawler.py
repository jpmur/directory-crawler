import os
import json


def crawl_dir(dir, parent_tree, parent_dir):
    dir_contents = os.listdir(dir)        
    current_tree = {}
    folder = []
    current_tree[dir] = folder                          # create new key/value pair (JSON object) for this directory
    if dir != parent_dir:                               # will only be true for first iteration (top level dir)
        parent_tree[parent_dir].append(current_tree)    # insert new JSON object into the parent dir's value array

    for path in dir_contents:
        path = os.path.join(dir, path)    
        if os.path.isdir(path):
            crawl_dir(path, current_tree, dir)
        else:
            folder.append(path)
    return current_tree
    


dir = "exampleDir"
tree = {}
tree[dir] = []
output = crawl_dir(dir, tree, dir)
json_tree = json.dumps(output, indent=2)
print(json_tree)
