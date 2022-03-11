import sys

if __name__ == "__main__":
    try:
        CORRECT = [0.75, 0.66, 0.13]
        answer = list(map(float, sys.argv[1:]))
        if all([answer[i] == CORRECT[i] for i in range(len(CORRECT))]):
            print("Correct! Well Done!")
        else:
            print("Something is wrong. Try again")
    except Exception as e:
        print("Something went wrong. It you change a cell, try to undo it or try to revert back to the previous state.")