import sys
input = sys.stdin.readline

def grade(a):
    if a == 'S':
        print("Superior")
    elif a == 'A':
        print("Excellent")
    elif a == 'B':
        print("Good")
    elif a == 'C':
        print("Usually")
    elif a == 'D':
        print("Effort")
    else:
        print("Failure")

a = input().strip()

grade(a)