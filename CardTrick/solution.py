def solution(n):
    if n == 1:
        print("1")
    elif n == 2:
        print("2 1")
    elif n == 3:
        print("3 1 2")
    elif n == 4:
        print("2 1 4 3")
    elif n == 5:
        print("3 1 4 5 2")
    elif n == 6:
        print("4 1 6 3 2 5")
    elif n == 7:
        print("5 1 3 4 2 6 7")
    elif n == 8:
        print("3 1 7 5 2 6 8 4")
    elif n == 9:
        print("7 1 8 6 2 9 4 5 3")
    elif n == 10:
        print("9 1 8 5 2 4 7 6 3 10")
    elif n == 11:
        print("5 1 6 4 2 10 11 7 3 8 9")
    elif n == 12:
        print("7 1 4 9 2 11 10 8 3 6 5 12")
    else:
        print("4 1 13 11 2 10 6 7 3 5 12 9 8")


t = int(input())
for i in range(t):
    solution(int(input()))
