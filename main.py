import sys

import map


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python main.py maze1.txt greedy")
    input = sys.argv[2]
    myMap = map.Map(sys.argv[1])
    print()

    if input == "astar":
        myMap.astar()
    elif input == "greedy":
        myMap.greedy()

    print()
    myMap.print()


main()
