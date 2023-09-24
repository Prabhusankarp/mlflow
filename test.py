import argparse

# for passing any arugument from command line, we use argparser

if __name__ == '__main__':
    # creating the argument object
    args=argparse.ArgumentParser()
    # create the methods
    args.add_argument("--name", "-n", default="sunny", type=str)
    args.add_argument("--age", "-a", default=25.0, type=float)
    parse_args=args.parse_args()
    
    print(parse_args.name,parse_args.age)