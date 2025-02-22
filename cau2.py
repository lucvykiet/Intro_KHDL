while True:
    try:
        number = int(input("Hay nhap so nguyen: "))
        test = 1 / number
        print(test)
        break
    except ValueError:
        print("Khong duoc nhap chu")
    except ZeroDivisionError:
        print("Khong duoc nhap so 0")