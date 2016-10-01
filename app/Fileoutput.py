
import sys
import os


if len(sys.argv) != 2:
    print('Usage: FileOutput.py <File> ')
    sys.exit(1)
print(sys.argv[1])
filename = sys.argv[1]
#filename = '/Users/temp/PycharmProjects/Test_task/tests/features/test_input.txt'

line = 5


class Output(object):

    def outputlast5lines(self, filename):
        buffersize = 1024
        filesize = os.stat(filename).st_size
        iter = 0
        with open(filename) as inf:
            result = []
            if buffersize > filesize:
                buffersize = filesize - 1
            while True:
                iter = +1
                position = inf.tell()
                inf.seek(filesize - buffersize * iter)
                result.extend(inf.readlines())
                if len(result) >= line or position == 0:
                    print(''.join(result[-5::]))
                    break

Output().outputlast5lines(filename)
