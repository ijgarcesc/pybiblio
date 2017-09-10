

import sys
import pandas

def pybiblio(infilename):

    ## CSV file
    data = pandas.read_csv(infilename)
    print(data.head())



if __name__ == '__main__':
    ##
    pybiblio(infilename = sys.argv[1])
    ##
