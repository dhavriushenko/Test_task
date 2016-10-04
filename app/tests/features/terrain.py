from lettuce import *
import os, io

@before.all
def create_file():
    get_current_path = os.path.dirname(os.path.abspath(__file__))
    path = get_current_path + "/test.txt"
    with io.FileIO(path, "w") as inf:
        world.path = path
        inf.close()



@after.all
def remove_file(self):
    os.remove(world.path)
