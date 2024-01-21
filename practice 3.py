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
1.دریافت ان و ام
2.آی در رنج ام و جی در رنج ان باشد
3.اگر حاصل جمع آی و جی بر 0 بخش پذیر بود، هشتک چاپ شود و در غیراینصورت ستاره چاپ شود.
4.خط 2و 3 در تابع نوشته شود و درنهایتن از تابع استفاده شود.
