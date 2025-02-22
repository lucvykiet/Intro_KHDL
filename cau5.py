class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None
    
    # 5.1 Thêm vào cuối danh sách
    def Add_tail(self, el):
        try:
            new_node = Node(el)
            if not self.head:  # Nếu danh sách rỗng, đặt head là node mới
                self.head = new_node
                return
            temp = self.head
            while temp.next:  # Duyệt đến node cuối cùng
                temp = temp.next
            temp.next = new_node  # Gán node mới vào cuối
            new_node.prev = temp  # Gán liên kết ngược
        except Exception as e:
            print(f"Lỗi khi thêm vào cuối danh sách: {e}")

    # 5.2 Thêm vào một node có giá trị el ở đầu danh sách liên kết
    def Add_prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        new_node.next = self.head 
        self.head.prev = new_node
        self.head = new_node

    #5.3 Thêm vào một node có giá trị el ở vị trí pos trong danh sách
    def Add_pos (self, data, pos):
        new_node = Node(data)
        temp = self.head
        if pos < 0:
            raise ValueError("Vi tri phai lon hon 0")
        elif pos == 0:
            self.Add_prepend(data)
        for _ in range(pos-1):
            if temp is None:
                raise ValueError("Pos vuot qua gioi han")
            temp = temp.next
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp
   
    # 5.4 Đếm số phần tử trong danh sách 
    def count(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    # 5.5 Xóa 1 phần tử ở đầu danh sách
    def delete_first(self):
        try:
            if not self.head:
                raise Exception("List is empty")
            if self.head.next:
                self.head = self.head.next
            if self.head:
                self.head.prev = None
        except Exception as e:
            print("Error delete!")

    # 5.6 Xóa 1 phần tử ở cuối danh sách 
    def delete_tail(self):
        try:
            if not self.head:
                raise Exception("Ham nay rong")
            temp = self.head
            #chạy tới phần tử cuối cùng
            while temp.next:
                temp = temp.next
            #check nếu mà trước cái temp mình muốn có tồn tại
            #thì mình cho cái típ theo của cái trước là none
            if temp.prev:
                temp.prev.next = None
            else:
                self.head = None
        except Exception as s:
            print(f"Lỗi khi nhập phần tử cuối cùng: {s}")

    def remove_pos(self, pos):
        temp = self.head
        try:
            if self.isEmpty():
                raise ValueError("Chuỗi trống không có gì")
            if pos <0:
                raise ValueError("Vi tri phia lon hon 0")
            elif pos == 0:
                self.delete_first()
            else:
                for _ in range(pos):
                    if temp is None:
                        raise ValueError("Vượt quá giới hạn của chuỗi")
                    temp = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp.prev:
                    temp.prev.next = temp.next
        except Exception as e:
            print(f"Lỗi {e}")
    #Tìm một phần tử có giá trị el và trả về vị trí của phần tử trong danh sách, nếu không có trả về giá trị -1 
    def search(self, el):
        try:
            count = 0
            temp = self.head
            if not self.head:
                raise Exception("Hàm rỗng không có gì")
            while temp:
                if temp.data == el:
                    return count
                temp = temp.next
                count +=1
            return -1
        except Exception as e:
            print(f"Lỗi {e}")

    #Tìm một phần tử ở vị trí pos trong danh sách và trả về giá trị của nó 
    def search_data_pos(self, pos):
        try:
            if self.isEmpty():
                raise Exception("Hàm rỗng không có gì")
            temp = self.head
            if pos < 0:
                raise ValueError("Vị trí pó phải lớn hơn 0")
            elif pos == 0:
                return self.head 
            else:
                for _ in range(pos):
                    if temp is None:
                        raise ValueError("Vượt qua giới hạn")
                    temp = temp.next
                if temp:
                    return temp.data
        except Exception as e:
            print(f"Lỗi {e}")
            return None
    #In danh sách
    def print_list(self):
        try:
            if not self.head:
                raise Exception("Hàm rỗng")
            temp = self.head
            while temp.next:
                print(f"{temp.data} ", end="->")
                temp = temp.next
            print(f"{temp.data}")
        except Exception as e:
            print("Lỗi in {e}")
        
    #Sắp xếp danh sách theo giải thuật Selection Sort và in ra kết quả 
    def selection_sort(self):
        try:
            if not self.head:
                return
            temp = self.head
            while temp:
                min_node = temp
                runner = temp.next
                while runner:
                    if runner.data < min_node.data:
                        min_node = runner
                    runner = runner.next
                temp.data, min_node.data = min_node.data, temp.data
                temp = temp.next
        except Exception as e:
            print(f"Lỗi khi sắp xếp danh sách: {e}")

dl = DoubleLinkList()
dl.Add_tail(1)
dl.Add_tail(4)
dl.Add_tail(2)
dl.Add_tail(5)

dl.Add_prepend(0)

dl.Add_pos(5,2)

print(dl.count())
dl.print_list()

dl.delete_first()
dl.print_list()

dl.delete_tail()
dl.print_list()

print(dl.search(2))
print(dl.search_data_pos(2))
dl.selection_sort()
dl.print_list()