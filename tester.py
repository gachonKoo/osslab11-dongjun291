import sys
from geo.utils import circle_area, rect_area, tri_area

def main():
    data = sys.stdin.read().strip().split()

    shape = data[0]

    if shape == "circle":
        r = float(data[1])
        print(circle_area(r))

    elif shape == "rect":
        w = float(data[1])
        h = float(data[2])
        print(rect_area(w, h))

    elif shape == "tri":
        w = float(data[1])
        h = float(data[2])
        print(tri_area(w, h))

if __name__ == "__main__":
    main()
