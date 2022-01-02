import os
import json


dir = "exampleDir"

def crawl_dir(dir):
    dir_contents = os.listdir(dir)      # get files and directories in the given directory

    for path in dir_contents:
        path = os.path.join(dir, path)    # create full file path
        print(path)
        if os.path.isdir(path):
            crawl_dir(path)


crawl_dir(dir)



# result = glob(os.path.join(dir, "*", ""))
# print(result)

# json_data = json.dumps(dir_tree)
#print(json_data)

# result = os.listdir(path)
# print(result)