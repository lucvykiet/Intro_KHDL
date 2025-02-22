filename = "data.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except  FileExistsError:
    print("Khong tim thay file")
except IOError:
    print(f"Khong doc duoc file {filename}")