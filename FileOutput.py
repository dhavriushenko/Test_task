
import sys
import os


if len(sys.argv) != 2:
    print('Usage: FileOutput.py <File> ')
    sys.exit(1)

filename = sys.argv[2]
#filename = '/Users/temp/Desktop/test/1.plist'
line = 5


class Output(object):

    def outputlast5lines(self, line):
        buffersize = 1024
        filesize = os.stat(self).st_size
        iter = 0
        with open(self) as inf:
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

Output.outputlast5lines(filename, line)