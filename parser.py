import argparse

def removeCommentedLines(parseData):
    ''' two condition to remove commented code
        1. remove all the characters from // to \n
        2. remove /* to */
    '''

    # removing /* to */
    print(parseData)
    print('======= after removing /* */========')
    while '/*' in parseData:
        # remove all character between /* and */
        start = parseData.find('/*')
        end  = parseData.find('*/') + 2
        parseData = parseData[:start] + parseData[end:]
    print (parseData)
    return parseData
    

def tokanizeFile(readStream):
    print('############ start parsing ##########')
    readStream.seek(0,0)
    parseData = readStream.read()

    # remove commented line 
    parseData = removeCommentedLines(parseData)

    # replave \n character with whitespace

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
