import argparse

def removeCommentedLines(parseData):
    ''' two condition to remove commented code
        1. remove all the characters from // to \n
        2. remove /* to */
    '''

    # removing /* to */
    while '/*' in parseData:
        # remove all character between /* and */
        start = parseData.find('/*')
        end  = parseData.find('*/') + 2
        parseData = parseData[:start] + parseData[end:]
    
    # now remove the commented lines

    while '//' in parseData:
        start = parseData.find('//')
        end = parseData.find('\n')+1
        parseData = parseData[:start] + parseData[end:]
    return parseData
    

def getClassName(tokens):
    ''' this method return the name of class'''
    # next item to the @iterface token will contain
    # the classname
    indexClassNameToken = tokens.index('@interface') + 1
    return tokens[indexClassNameToken]

def getTokens(parseData):

    ''' this method will give list of tokens after
        removing the white spaces'''
    tokens = []
    for line in parseData.splitlines():
        line.strip()
        tokensInLine = line.split(' ')
        while '' in tokensInLine :
            tokensInLine.remove('')
        tokens = tokens + tokensInLine
    return tokens

def tokanizeFile(readStream):
    # print('############ start parsing ##########')
    readStream.seek(0,0)
    parseData = readStream.read()

    # remove commented line 
    parseData = removeCommentedLines(parseData)
    
    # convert the pareseData to list of tokens
    tokens = getTokens(parseData)

    # print('############ stop parsing ##########')
    return tokens

def generateXml(readStream):
    ''' this method will generate xml equivalent for the the
        obj-C file.'''
    
    # open a write stream to produce xml
    writeStream = open('default.xml','w')
    writeStream.write('<?xml version=\"1.0\"?>')
    tokens = tokanizeFile(readStream)
    writeStream.close()


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
    # tokanizeFile(readStream)
    generateXml(readStream)
    readStream.close()
