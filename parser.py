import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('objFile',help='file name to parse')
    # parser.add_argument('--source','-s',help='this is echo', dest='echovar')
    parser.add_argument('--header','-hd', dest='header', help='header file for the protocol')
    args = parser.parse_args()
    print('objective c file -- %s' % args.objFile)
    print('header file for protocol -- %s' % args.header)

