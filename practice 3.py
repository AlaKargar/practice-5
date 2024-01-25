m = int(input("please enter m: "))
n = int(input("please enter n: "))


def print_nm():

    for i in range(m):
        for j in range(n):
            if (i+j) % 2 == 0:
                print("#", end="")
            else:
                print("*", end="")


print_nm()
