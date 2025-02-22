# Giả sử: L1 và L2 là các danh sách có độ dài bằng nhau của các số. Viết một hàm để trả về 
# một danh sách chứa L1[i]/L2[i] 
# Sử dụng raise ValueError('get_ratios được gọi với đối số không hợp lệ')
import numpy as np

def tinhtoan(l1,l2):
    result = []
    if len(l1) != len(l2):
        raise ValueError("Hay nhap du lieu dung de")

    for i in range(len(l1)):
        if l2[i] == 0:     
            raise ZeroDivisionError("Dung nhap L2 bang 0")
        result.append(l1[i]/l2[i])
    return result

L1 = [3,5,6,6]
L2=[1,6,1,5]
print(tinhtoan(L1,L2))