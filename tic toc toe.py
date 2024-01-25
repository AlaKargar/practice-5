#       0      1     2
game = [["-", "-", "-"],  # 0
        ["-", "-", "-"],  # 1
        ["-", "-", "-"]]  # 2

# 0,0  0,1   0,2 افقی
# 1,0  1,1   1,2 افقی
# 2,0  2,1   2,2 افقی

# 0,0  1,0  2,0 عمودی
# 0,1  1,1  2,1 عمودی
# 0,2  1,2  2,2 عمودی

# 0,0 1,1  2,2 مورب
# 0,2  1,1 2,0 مورب

print("Welcome to the tic toc toe game!")


def show():
    for i in range(3):
        for j in range(3):
            print(game[i][j], end="")
        print()


z = False
plyer1 = input("Enter your name please: ")
plyer2 = input("Enter your name please: ")
row = 0
col = 0


def player1():
    print(plyer1)
    row = int(input("satr ra vared konid(0_2): "))
    col = int(input("sotoon ra vared konid(0_2): "))
    # تکراری نبودن انتخاب ها
    if game[row][col] == "x" or game[row][col] == "0":
        print("your choice is Repetitious!")
        print("please enter another numbers: ")
        player1()
    game[row][col] = "x"
    show()


def player2():
    print(plyer2)
    row = int(input("satr ra vared konid(0_2): "))
    col = int(input("sotoon ra vared konid(0_2): "))
    # تکراری نبودن انتخاب ها
    if game[row][col] == "x" or game[row][col] == "0":
        print("your choice is Repetitious!")
        show()
        player2()

    game[row][col] = "0"
    show()


while z == False:
    player1()

    # بررسی شرط های بازی برای بازیکن 1
    if game[0][0] == "x" and game[0][1] == "x" and game[0][2] == "x":
        print(plyer1+" is win!")
        show()

        z = True
    elif game[1][0] == "x" and game[1][1] == "x" and game[1][2] == "x":
        print(plyer1+" is win!")
        show()
        z = True
    elif game[2][0] == "x" and game[2][1] == "x" and game[2][2] == "x":
        print(plyer1+" is win!")
        show()
        z = True

    elif game[0][0] == "x" and game[1][0] == "x" and game[2][0] == "x":
        print(plyer1+" is win!")
        show()
        z = True
    elif game[0][1] == "x" and game[1][1] == "x" and game[2][1] == "x":
        print(plyer1+" is win!")
        show()
        z = True
    elif game[0][2] == "x" and game[1][2] == "x" and game[2][2] == "x":
        print(plyer1+" is win!")
        show()
        z = True

    elif game[0][0] == "x" and game[1][1] == "x" and game[2][2] == "x":
        print(plyer1+" is win!")
        show()
        z = True
    elif game[0][2] == "x" and game[1][1] == "x" and game[2][0] == "x":
        print(plyer1+"is win!")
        show()
        z = True

    player2()
   # بررسی شرط برنده بودن بازیکن 2
    if game[0][0] == "0" and game[0][1] == "0" and game[0][2] == "0":
        print(plyer2+" is win!")
        show()
        z = True
    elif game[1][0] == "0" and game[1][1] == "0" and game[1][2] == "0":
        print(plyer2+" is win!")
        show()
    elif game[2][0] == "0" and game[2][1] == "0" and game[2][2] == "0":
        print(plyer2+" is win!")
        show()
        z = True

    elif game[0][0] == "0" and game[1][0] == "0" and game[2][0] == "0":
        print(plyer2+" is win!")
        show()
        z = True
    elif game[0][1] == "0" and game[1][1] == "0" and game[2][1] == "0":
        print(plyer2+" is win!")
        show()
        z = True
    elif game[0][2] == "0" and game[1][2] == "0" and game[2][2] == "0":
        print(plyer2+" is win!")
        show()
        z = True

    elif game[0][0] == "0" and game[1][1] == "0" and game[2][2] == "0":
        print(plyer2+" is win!")
        show()
        z = True
    elif game[0][2] == "0" and game[1][1] == "0" and game[2][0] == "0":
        print(plyer2+" is win!")
        show()
        z = True
