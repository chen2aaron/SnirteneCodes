import argparse


def main(count, delay, reget):
    print(count)
    print(delay)
    print(reget)


def parseArguments():
    parser = argparse.ArgumentParser(prog='haha')
    parser.add_argument("-c", help="counts of main", type=int)
    parser.add_argument("-d", help="delay second", type=float, default=0.3)
    parser.add_argument("-a", help="auto repeated", action="store_true", default=False)
    return parser.parse_args()


if __name__ == '__main__':
    args = parseArguments()
    main(args.c, args.d, args.a)

