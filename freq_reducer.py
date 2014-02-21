#!/usr/bin/python
     
import sys
 
def main():
    current_word = None
    current_count = 0
    word = None

    # input comes from STDIN
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        print line

if __name__ == "__main__":
    main()
