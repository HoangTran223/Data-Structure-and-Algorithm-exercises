import math
# TÌm trọng lượng lớn nhất của dãy con
# VD1: cách trực tiếp
max_sum = 0
n = int(input())
a=[]
for i in range(n):  # CÁCH NÀY NHẬP PHẦN TỬ THEO HÀNG DỌC
    a.append(float(input(f"Nhập phần tử thứ {i+1}:" )))
for i in range (0,n):
    for j in range(i,n):
        sum = 0
        for k in range(i,j):
            sum += a[k]
        if max_sum < sum:
            max_sum = sum
print(max_sum)

#VD1: C1
max_sum = 0
n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += a[j]
        if max_sum<sum:
            max_sum = sum
print(max_sum)

#VD1: Sử dụng chia để trị
def MaxLeft(a,i,j):
    max_sum = -math.inf 
    sum = 0
    for k in range(j,i-1,-1):  
        sum = sum + a[k]
        max_sum = max(sum, max_sum)
    return max_sum
def MaxRight(a,i,j):
    max_sum = -math.inf
    sum = 0
    for k in range(i,j+1):
        sum += a[k]
        max_sum = max(sum, max_sum)
    return max_sum
def MaxSub(a,i,j):
    if i == j: return a[i]
    else:
        m = int((i+j)/2)
        wL = MaxLeft(a,i,m)
        wR = MaxRight(a,m+1,j)
        wM = MaxLeft(a,i,m)+ MaxRight(a,m+1,j)
        return max(wL, wR, wM)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(MaxSub(a,0,n-1))

#VD1: Sử dụng Quy hoạch động
""" Ta duyệt từ đầu,tới vị trị nào có tổng nhỏ hơn 0 thì ta bỏ luôn dãy con 
từ vị trí đó và tính lại tổng từ ptu tiếp theo tại vị trí đó trở đi. Bởi vì
nếu đoạn trước đó đã < 0 thì cộng vào cho đoạn sau sẽ chỉ nhỏ đi nên ta cắt luôn từ vtri đó """
vitri = 0
def QHĐ(a,n):
    global vitri
    sum =0; max_sum =0
    for i in range(n):
        if sum + a[i] < 0 :
            sum = 0
        if sum+a[i]>=0 :
            sum += a[i]
        if sum > max_sum:
            max_sum = sum
            vitri = i
    return max_sum
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
sum = QHĐ(a,n)
print(sum)
while (sum >0): #Vì ta chỉ lưu vtri dãy con kết thúc nên ta duyệt từ vị trí đó
                 # ngược lại, trừ dần đi phần tử đến khi nào sum = 0 thì tức là tổng ta tính từ đoạn đó trở đi
    print(a[int(vitri)], end=' ')
    sum -= a[int(vitri)]
    vitri = vitri - 1




# Thuật toán Binary Search:
def Binary_Search (a,l,r,x):      # Xem trong x có mặt trong a[] kích thước n không
                                  # l là vị trí bắt đầu, r là kết thúc
                                  # Bắt buộc dãy nhập vào phải là dãy không giảm
    if r>= l:
        mid = l + (r-l)//2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            return Binary_Search(a, l, mid-1, x)
        else:
            return Binary_Search(a, mid+1, r, x)
    else:
        return -1
n = int(input())
a=[]
x = int(input())
for i in range(n):
    a.append(int(input()))
result = Binary_Search(a,0,len(a)-1,x)
if result != -1:
    print(f"{x} ở vị trí {result+1}")
else:
    print(f"Không có {x} ở dãy")





# Thuật toán Pigeonhole Sort: độ phức tạp O( n+ |max-min| )
# Chỉ hoạt động với số nguyên ko âm
def pigeonhole_sort(a):
    sort_min = min(a)
    sort_max = max(a)
    size = sort_max - sort_min + 1
    holes = [0]*size
    for x in a:
        assert type(x) is int       # Ktra điều kiện, sai báo lỗi, đúng thì tiếp tục chạy sau đó
        holes[x - sort_min] += 1    # Cái này chỉ để cho ko vượt quá phạm vi list        
    i = 0 
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1 
            a[i] = count + sort_min
            i += 1
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
pigeonhole_sort(a)
for i in range(0,len(a)):
    print(a[i], end = ' ')




# Thuật toán Bubble Sort (Sắp xếp bọt): độ phức tạp O(n^2), được với cả số âm
def bubble_sort(a):
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if  a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if(swapped == False):               # Tức dãy ko có sự thay đổi
            break
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
bubble_sort_sort(a)
for i in range(0,len(a)):
    print(a[i], end = ' ')




# Thuật toán Counting Sort: độ phức tạp O(N+M)
# N: size input_array, M: size count_array
""" Làm việc nhanh trong TH giá trị đầu vào nhỏ, nhưng không
thực hiện dc với số thập phân, phải tạo thêm dãy, code này chỉ cho số ko âm """
def counting_sort(input_array):
    M = max(input_array)
    count_array = [0]*(M+1)
    for i in input_array:
        count_array[i] += 1
    for i in range(1, M+1):
        count_array[i] += count_array[i-1]
    output_array = [0]*(len(input_array))
    for j in range(len(output_array) - 1, -1, -1):
        output_array[count_array[input_array[j]]-1] = input_array[j]
        count_array[input_array[j]] -= 1
    return output_array
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = [0]*(n+1)
b = counting_sort(a)
for i in range(0,len(b)):
    print(b[i], end = ' ')




# Thuật toán Quick Sort: độ phức tạp trung bình O(nlogn)
# Thuật toán chia để trị, hiệu quả trên tập dữ liệu lớn
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1          # Trả về vị trí của pivot
    # Thuật toán này sẽ chia dãy thành 2 nửa, nửa nhỏ hơn pivot và nửa > pivot
def quick_sort(array, low, high):
    if low < high:
        piv = partition(array, low, high)
        quick_sort(array, low, piv - 1)
        quick_sort(array, piv + 1, high)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
quick_sort(a, 0, n-1)
for i in range(0,len(a)):
    print(a[i], end =' ')




# Thuật toán Merge Sort: độ phức tạp O(nlogn)
def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        Left_array = array[:mid]
        Right_array = array[mid:]
        merge_sort(Left_array)
        merge_sort(Right_array)
        i = j = k = 0
        while i < len(Left_array) and j < len(Right_array):
            if Left_array[i] <= Right_array[j]:
                array[k] = Left_array[i]
                i += 1
            else:
                array[k] = Right_array[j]
                j += 1
            k += 1
        while i < len(Left_array):
            array[k] = Left_array[i]
            i, k = i+1, k+1
        while j < len(Right_array):
            array[k] = Right_array[j]
            j, k = j+1, k+1
n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
merge_sort(a)
for i in range(len(a)):
    print(a[i], end =' ')




# Thuật toán Heap Sort:
import heapq
n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
heapq.heapify(a)
n = len(a)
while n > 0:
    print(heapq.heappop(a), end = ' ')
    n -= 1
    

# Bài toán xếp Hậu sử dụng quay lui:
import numpy as np
n = int(input())
a = np.zeros((n,n))             # Tạo mảng nxn toàn số 0
def xuat_mang (mang):
    for i in mang:
        for j in i:
            print(j, end = " ")
        print()

def solve(mang):
    l = len(mang)
    for hang in range(l):
        for cot in range(l):
            if mang[hang][cot] == 0:                    
                if check(mang, hang, cot) == True:              # Nếu True, cho phần tử đó là 1, rồi gọi hàm để làm tiếp 
                    mang[hang][cot] = 1
                    solve(mang)
                if sum(sum(a) for a in mang) == l:              # Nếu bảng đủ số 1 rồi thì dừng
                    return mang
                else:                                           # Đây chính là quay lui, khi k tìm đc cách xếp hợp lệ, cần đưa a[i][j] về lại 0, thay vì đang là 1
                    mang[hang][cot] = 0
    return mang

def check(mang, dong, cot):
    l = len(mang)
    for i in range(l):              # Check cột
        if mang[i][cot] == 1:
            return False
    for i in range(l):              # Check hàng
        if mang[dong][i] == 1:
            return False
    for i in range(l):              # Check đường chéo
        for j in range(l):
            if mang[i][j] == 1:
                if abs(cot - j) == abs (dong - i):
                    return False
    return True
solve(a)
xuat_mang(a)




# Bài toán mã đi tuần sử dụng đệ quy:
import numpy as np
def solve_knight_move(n, hang, cot):
    a = [[0 for i in range(n)] for j in range(n)]
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)]
    def valid_move(x, y):
        if x < 0 or y < 0 or x >= n  or y >=n:      # Đi quá bàn cờ
            return False
        if a[x][y] != 0:                            # Đã đi qua ô này
            return False
        return True
    def ma_di_tuan(x, y, count):
        if count == n**2:
            return True
        for move in moves:
            next_move_x = x + move[0]               # next_x = x + 2 lượt đầu     
            next_move_y = y + move[1]               # next_y = y + 1 lượt đầu
            if valid_move(next_move_x, next_move_y):
                a[next_move_x][next_move_y] = count + 1
                if ma_di_tuan(next_move_x, next_move_y, count + 1):
                    return True
                else:
                    a[next_move_x][next_move_y] = 0
        return False
    a[hang][cot] = 1
    if ma_di_tuan(hang, cot, 1):
        for row in a:
            print(row)
        return True
    else:
        print("Không có đường đi hợp lệ")
        return False
n = int(input())
hang = int(input())
cot = int(input())
solve_knight_move(n, hang, cot)




# Bài toán Josephus:
def josephus(n, m):
    vongtron = list(range(1, n+1))
    i = 0
    while len(vongtron) > 1:
        i = (i + m -1) % len(vongtron)          # Tính toán vị trí cần xóa
        vongtron.pop(i)
    print(vongtron[0])
n = int(input())
k = int(input())
josephus(n, k)



# Bài toán Rob_Cutting sử dụng quy hoạch động:
def cut_rod(price, n):
    # Khởi tạo mảng để lưu giá trị tối ưu cho từng chiều dài
    r = [0] * (n + 1)

    # Tính toán giá trị tối ưu từ chiều dài 1 đến n
    for i in range(1, n + 1):
        max_val = -1
        for j in range(1, i + 1):
            max_val = max(max_val, price[j - 1] + r[i - j])
        r[i] = max_val

    return r[n]

# Bảng giá trị cho mỗi chiều dài
price = [1, 5, 8, 9, 10, 17, 17, 20]
n = len(price)
print("Giá trị tối ưu của việc cắt thanh gỗ là:", cut_rod(price, n))




# NGĂN XẾP (stack):
stack = []
def is_full(dodai):
    if top >= dodai -1:
        return True
    else:
        return False
def is_empty():                 # Kiểm tra có rỗng ko
    return len(stack) == 0
def push(stack, value, dodai):                 # Thêm phần tử vào đầu stack
    if is_full(dodai) == True:
        print("Stack full")
    else:
        stack.append(value)
def pop(stack, value, dodai ):   # Tương tự stack[-1], lấy phần tử trên đầu danh sách, xóa nó
    if is_empty():
        return "Ngăn xếp trống"
    else:
        return stack.pop()

    
# Ứng dụng 1: Bài toán đổi cơ số:
n = int(input())
b = int(input())
n1 = n
convert = []
while(n > 0):
    convert.append(n % b)
    n = n // b
print(f"Số {n1} được chuyển về hệ {b} có biểu diễn là:", end=' ')
for i in range(len(convert)):
    print(convert[-i-1], end='')




# Ứng dụng 2: Bài toán Perentheses matching:
def solve(s):
    stack = []
    if len(s) % 2 == 1:             # Dãy độ dài lẻ thì ko thỏa mãn
        return False
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(')')
        elif s[i] == '[':
            stack.append(']')
        elif s[i] == '{':
            stack.append('}')
        elif len(stack) == 0 or stack.pop() != s[i]:            # ban đầu stack = 0 tức phần tử đầu là đóng, nên sai
                                                                # Nếu là ngoặc đóng, thì phải giống cái top của ngăn xếp
            return False
    return True
s = "{{[[(})]]}}"
if solve(s) == True:
    print("Correct")
else:
    print("Incorrect")


# Ứng dụng 3: Cho n dãy số nguyên dương. Với mỗi vị trí i, tìm vị trí j gần nhất về 
              # bên trái thỏa mãn ai< aj
""" Xét tập b "UCV" thể hiện vị trí trong dãy a: bi < bj và a(bi) > a(bj) với mọi i < j
- Với mỗi vị trí i, ta loại hết UCV j ở cuối tập mà aj < ai 
- Xét tập UCV, UCV cuối cùng là vị trí cần tìm, tập rỗng thì ko tồn tại, in ra -1
- Đẩy vị trí i vào cuối tập """

""" VÍ DỤ a = 2, 1, 3, 2, 8, 5, 7
- Đầu tiên i = 0, tập UCV rỗng, nên in ra -1, UCV = {0}
- Xét i = 1, UCV có 1 đề cử là j = 0. Do {0} thỏa mãn nên in ra {0}, và UCV = {0,1}
- Xét i = 2, xét UCV từ phải sang trái. Do tất cả các vị trí i về sau đều tìm về vị trí gần nhất bên trái
nên nếu tồn tại i > j mà ai > aj, thì vị trí j sẽ ko bao giờ dc chọn. Thật vậy, giả sử tồn tại vị trí k nhận j 
làm kết quả mà ko nhận i là kqua (j < i < k), ta có aj > ak và ak > ai, nên aj > ai (trái giả sử).
- Vì vật loại {1}, rồi {0} ra khỏi UCV, UCV rỗng, in -1 và UCV = {2}
- Xét i = 3, do có a[2] > a[3], nên 2 ko đc chọn, nên UCV rỗng, in -1 và UCV = {3}
- Xét i = 4, do j = 3 thỏa mãn, in ra {3}, UCV = {3,4}. Làm tương tự đến hết """





# HÀNG ĐỢI (Queue):
from collections import deque       # deque là sự kết hợp giữa stack và queue, dùng nào tùy mục đích

q = deque()
q.append(5)
q.append(10)
q.append(15)           # deque([5, 10, 15])
q.appendleft(0)        # deque([0, 5, 10, 15])
q.pop()                # deque([0, 5, 10])
q.popleft()            # deque([5, 10])
print(len(q))          # In ra 2
print(q.count(7))      # In ra 0
print(q[0])            # In ra 5, tương tự popleft()
print(q[-1])           # In ra 10, tương tự pop()
print(q)
q1 = deque()
q1.extend([1, 2, 3, 4])
q1.extendleft([-1, 0]) # In ra 0, -1, 1, 2, 3, 4
q1.rotate(-2)          # In ra 1, 2, 3, 4, 0, -1        # âm thì quay dịch sang trái
q1.reverse()           # In ra -1, 0, 4, 3, 2, 1
print(q1)


# Ứng dụng 1: đếm số lượng số nhị phân không vượt quá n ( tức vd 101 < 102 = n)
""" Ta sẽ sinh ra các số nhị phân lớn hơn dựa vào các số nhị phân nhỏ hơn.
Ban đầu hàng đợi chỉ có số 1. Với mỗi số np t lấy từ hàng đợi, 2 số 10t và 10t + 1 cũng là số np """
from collections import deque
n = int(input())
queue = deque()
queue.append(1)
result = 0
while len(queue) > 0:
    a = queue[0]
    queue.popleft()
    if a <=n:
        result += 1
        queue.append(a*10)
        queue.append(a*10+1)
print(result)


# ứng dụng 2: kiểm tra 1 xâu có phải xâu palindrome không:
from collections import deque
s = str(input())
queue = deque(s)
stack = []
for i in range(len(s)):
    stack.append(s[i])
result = 1
for i in range(len(s)):
    if queue[0] != stack[-1]:
        result = 0
        break
    else:
        queue.popleft()
        stack.pop()
if result == 1:
    print("Là xâu Palidromes")
else:
    print("Không là xâu Palidromes")

" Cách khác để giải:"
def is_palindrome(s):
    return s == s[::-1]
s = str(input())
s_palindrome = is_palindrome(s)
if s_palindrome:
    print("Yess")
else:
    print("No")


# THUẬT TOÁN TÌM KIẾM:


# Nhắc lại về Binary Search (chương I là theo gọi hàm đệ qui):
import numpy
def binary_search(array, start, end, target):           # Bắt buộc dãy nhập vào phải là dãy không giảm, 
                                                        
    while start <= end:
        mid = (start + end)//2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1
n = int(input())
a=[]
x = int(input())
for i in range(n):
    a.append(int(input()))
result = binary_search(a,0,len(a)-1,x)
if result != -1:
    print(f"{x} ở vị trí {result+1}")
else:
    print(f"Không có {x} ở dãy")


# Kiểm tra 1 dãy nguyên có phải dãy cấp 3 hay không, và in ra bộ cấp 3 "nhỏ nhất" :
def mergesort_array (a):                # Độ phức tạp O(n^2.logn)
    if len(a) > 1:
        mid = len(a)//2
        left_a =  a[:mid]
        right_a = a[mid:]
        mergesort_array(left_a)
        mergesort_array(right_a)

        i = j = k = 0
        while i < len(left_a) and j < len(right_a):
            if  left_a[i] < right_a[j]:
                a[k] = left_a[i]
                i += 1
            else:
                a[k] = right_a[j]
                j += 1
            k += 1
        while i < len(left_a):
            a[k] = left_a[i]
            i, k = i+1, k+1
        while j < len(right_a):
            a[k] = right_a[j]
            j, k = j+1, k+1
def binary_search(array, start, end, target):           
    while start <= end:
        mid = (start + end)//2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
count = 0
mergesort_array(array)
for i in range(n):
    for j in range(i+1,n):
        result = binary_search(array, j, n - 1, 2*array[j] - array[i])
        if result != -1:
            count += 1
            print(f"Là dãy cấp 3, có 1 bộ ba đầu tiên là {array[i], array[j], array[result]}")
            break
    if count == 1:
        break
if count == 0:
    print("Không phải dãy cấp 3")



# Cho N cây, M gỗ cần cắt, và N chiều cao cây, 1 số H. Cắt: thu được gỗ là phần ngọn của các cây cao hơn H. Tìm H để tiết kiệm gỗ bị cắt nhất
def sum_of_wood(a,h):
    result = 0
    for i in range(n):
        if a[i] > h:
            result += a[i] - h
    return result

n = int(input())
m = int(input())
a = []
for i in range(n):
    a.append(int(input()))
min_a = 0
max_a = max(a)
while max_a - min_a > 1:
    mid = (min_a + max_a)//2
    if sum_of_wood(a,mid) >= m :
        min_a = mid
    else:
        max_a = mid
print(min_a)


""" Nhị phân số thực: có N bánh tròn: bánh i có ri và chiều cao = 1. Cần cắt N bánh thành (F+1) miếng.
Mỗi miếng thuộc về đúng 1 bánh, mỗi miếng đều có lượng bánh như nhau(tức cùng diện tích). Tìm lượng bánh lớn nhất thỏa mãn"""

import numpy as np
def func(x, s):
    if x == 0:
        return 0
    numbers_of_people = 0
    for i in range(n):          # Duyệt qua từng chiếc bánh có diện tích S[i]
        numbers_of_people += (int)(s[i]/x)
    if numbers_of_people >= f+1:
        return 1
    else:
        return 0
# Ta tìm x lớn nhất để hàm func trả về 1
def binary_search_float(s):
    low = 0
    high = s[n-1]
    while high - low > 1e-8:
        mid = (low + high)/2
        if func(mid,s) == 1:
            low = mid
        else:
            high = mid
    return low

n = int(input())
f = int(input())
r = []
s = np.zeros(n)
pi = 3.1415
for i in range(n):
    r.append(int(input()))
r.sort()                        # Chỉ dùng được khi danh sách là số nguyên
for i in range(n):              
    s[i] = pi*r[i]*r[i]         # Dãy s đã được sắp xêp tăng dần 
print(binary_search_float(s))   # Giá trị có thể ko đúng

