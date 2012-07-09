import sys

def reader(F):
    tmp, sys.stdin = sys.stdin, F
    line = raw_input()
    print(line)
    sys.stdin = tmp
    
reader(open('test-stream-mode.py'))  #input return text
reader(open('test-stream-mode.py', 'rb'))    #input return bytes

def writer(F):
    tmp, sys.stdout = sys.stdout, F
    print(99, 'spam')
    sys.stdout = tmp
    
writer(open('temp', 'w'))
print(open('temp').read())

writer(open('temp', 'wb'))    #fail, pass a textstr to binary-mode file
writer(open('temp', 'w', 0))  #fail, test file cannot be unbuffered
