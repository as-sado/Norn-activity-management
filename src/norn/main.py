from norn.cli.parser import get_argument

def main():
    parser = get_argument()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
    
