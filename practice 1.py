x = int(input("please enter your first number: "))
y = int(input("please enter your second number: "))
z = int(input("please enter your third number: "))

if x < y+z and y < x+z and z < x+y:
    print("It is a triangle")
else:
    print("It isn't a triangle.")

1.ابتدا اندازه ضلع هرسه مثلث دریافت شود
2.در این شرط بررسی می شود که آیا رهضلع از حاصل جمع دو ضلع دیگر کوچکتر است یا خیر
3.اگر شرط برقرار بود پیغام مثلث است چاپ می شود
4. در غیراینصورت مثلث نیست چاپ میشود
