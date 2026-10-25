import argparse
from src.messages import welcome


def main():
    parser = argparse.ArgumentParser(description="Print a welcome message")
    parser.add_argument("name", help="name to greet")
    args = parser.parse_args()
    print(welcome(args.name))


if __name__ == "__main__":
    main()