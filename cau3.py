filename ="data.txt"

try:
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Ghi du lieu mau\n")
        print("Da ghi!")
    
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Khong tim thay file")
except IOError:
    print("Khong doc duoc file")
finally:
    print("Dong tep")


