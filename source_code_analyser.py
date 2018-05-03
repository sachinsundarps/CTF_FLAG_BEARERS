#!/usr/bin/python

import os
import sys
import re

def analyze(path,srcfile, regex):
    lines = srcfile.readlines()
    cnt = 1
    for line in lines:
        m = re.search(regex,line)
        if m:
            print(len(path) * '---', os.path.basename(srcfile.name), 'line', cnt, line)
        cnt = cnt+1

if __name__ == "__main__":
    options_dict = {
       'e': 'exec',
       's': 'system',
       'c': 'strcpy',
       'a': 'argv',
       'g': 'gets',
       'r': 'read',
       'n': 'strncpy',
       'p': 'popen',
       'f': 'printf',
       't': 'strcat',
       'z': 'strncat',
       'm': 'memcpy'

    }
    regex = "(exec|system|strcpy|argv|gets|read|strncpy|popen|printf|strcat|strncat|memcpy)"
    if len(sys.argv) == 1:
        print("Please add provide directory name as first argument")
        sys.exit()
    elif len(sys.argv) == 2: 
        rootpath = sys.argv[1]
        print("Options for methods to search for (all by default): ")
        print("e		: exec")
        print("s		: system")
        print("c		: strcpy")
        print("a		: argv")
        print("g		: gets")
        print("r		: read")
        print("n		: strncpy")
        print("p		: popen")
        print("f		: printf")
        print("t		: strcat")
        print("z		: strncat")
        print("m		: memcpy")
    elif len(sys.argv) == 3: 
        rootpath = sys.argv[1]
        if not sys.argv[2].startswith('-'):
            print("Invalid Format. Use -[options]")
            sys.exit()
        else:
            fn_list = []
            for x in sys.argv[2][1:]:
                if x in options_dict:
                    fn_list.append(options_dict[x])
                else:
                    print("Invalid Option: ", x)    
            if fn_list:
                regex = '('+'|'.join(fn_list) + ')'
    print(regex)
    if not os.path.exists(rootpath):
        print("Path does not exist.") 
        sys.exit()
    for root, dirs, files in os.walk(rootpath):
        path = root.split(os.sep)
        print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
    	    if file.endswith('.c'):
                with open(os.path.join(root,file),'r') as srcfile:
                   analyze(path, srcfile, regex)
