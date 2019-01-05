import os

file = open('retrieve_func_def.txt', 'w')

def iterate_dir(dir_path):
    if os.path.isdir(dir_path):
        for filename in os.listdir(dir_path):
            # Iterate using recursive
            iterate_dir(os.path.join(dir_path, filename))
            # If the file has ".py" extension
            if os.path.join(dir_path, filename)[-3:] == ".py" and \
               filename.find("test") == -1:
               #print(filename)
               file.write("================================================================================\n")
               file.write(filename + "\n")
               with open(os.path.join(dir_path, filename)) as f:
                   func_defs = []
                   for line in f:
                       if "def " in line:
                           # Write to file if found second time since there are definition in comments at the top of the class.
                           if line in func_defs:
                               file.write("\t" + line)
                               print("\t" + line, end='')
                           func_defs.append(line)
  

               file.write("================================================================================\n")

iterate_dir("C:\\Users\\Nickj\\Desktop\\WY_PROJ_BLENDER_EDITOR\\WY_PROJ_BLENDER_EDITOR\\MAIN\\src\\main")
