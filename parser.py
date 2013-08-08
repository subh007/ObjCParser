import argparse

def tokanizeFile(readStream):
    print('############ start parsing ##########')
    #print(readStream)
    i = 0
    for line in readStream:
        i += 1
        print("%d. %s" % (i, line))

    print('############ stop parsing ##########')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('objFile',help='file name to parse')
    # parser.add_argument('--source','-s',help='this is echo', dest='echovar')
    parser.add_argument('--header','-hd', dest='header', help='header file for the protocol')
    
    args = parser.parse_args()
    
    print('objective c file -- %s' % args.objFile)
    print('header file for protocol -- %s' % args.header)
    
    # now read the file to parse
    readStream = open(args.objFile, 'r')

    # now we have the whole file. 
    # move for tokanization
    tokanizeFile(readStream)
