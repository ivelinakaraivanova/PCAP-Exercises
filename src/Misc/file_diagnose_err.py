from os import strerror


try:
    stream = open('some_file.txt')
    stream.close()
except Exception as e:
    print(e.errno)


try:
    stream = open('some_file.txt')
    stream.close()
except Exception as e:
    print(strerror(e.errno))
