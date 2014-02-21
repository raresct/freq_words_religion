#!/usr/bin/python
     
import sys
 
def main():

    max_digits = 20
    # input comes from STDIN
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

        # parse the input we got from mapper.py
        word, count = line.split('\t', 1)
        if len(count)>max_digits:
            continue
        no_zeros = max_digits-len(count)
        count = '0'*no_zeros+count
        print '%s\t%s' % (count, word)

if __name__ == "__main__":
    main()
