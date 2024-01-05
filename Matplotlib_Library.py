import matplotlib
import numpy as np
from matplotlib import pyplot as plt 

""" Hàm plot: vẽ đt từ điểm này đến điểm kia """
xpoints = np.array([1, 10, 13])
ypoints = np.array([4, 12, 5])
plt.plot(xpoints, ypoints)               # Gấp khúc đi từ (1, 10) đến (4, 12), rồi (13, 5)
#plt.show()

plt.plot(xpoints, ypoints, 'o')          # Chỉ 2 điểm (1, 10) và (4, 12)
#plt.show()

plt.plot(xpoints)                        # Chỉ nhập 1 cái, mặc định đó là tung độ, còn tọa độ lấy từ 0, 1, 2,...
#plt.show()


""" Cú pháp marker|line|color: tô đậm điểm | dạng đt(liền, chấm) | màu """
plt.plot(xpoints, ypoints, 'o--y', ms = 20, mfc = 'b', mec = 'r', linewidth = 8)            # ms : thay đổi kích thước chấm
                                                                                            # mfc : tô bên trong chấm
                                                                                            # mec : tô vành ngoài chấm
plt.show()                                                                                  # linewidth : độ rộng của đường thẳng 



xpoints = np.array([80, 85, 70, 95, 15, 105, 300, 115, 120, 10])
ypoints = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
font1 ={'family': 'serif', 'color':'blue', 'size': 20}                          # Cỡ chữ - màu - kích cỡ
plt.title(" Điền tiêu đề của đồ thị", loc ='left')                              # Vị trí tiêu đề: trái
plt.xlabel("Điền chú thích ở Ox")
plt.ylabel("Điền chú thích ở Oy", fontdict = font1)
plt.plot(xpoints, ypoints)

plt.grid(axis = 'x', color ='green', linewidth = 2.5, linestyle = '--')                      # Vẽ lưới cho đồ thị                                          
plt.show()



""" Sử dụng hàm subplot() để vẽ nhiều đồ thị trên 1 hình: """
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2, 1)                        # 2 hàng, rồi đến 2 cột, đồ thị này ở vị trí 1
plt.plot(x,y)
plt.title("4 đồ thị điền được 4 title")

x = np.array([0, 1, 6, 3])
y = np.array([10, 70, 30, 40])
plt.subplot(2, 2, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 2, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 2, 4)
plt.plot(x,y)
plt.suptitle("Title chung cho cả 4 hình")
plt.show()



""" Vẽ các điểm phân tán """
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, c = 'pink', s = sizes)

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, c = 'blue')

plt.show()



""" Vẽ biểu đồ cột """
x = np.array(["A", "B", "C", "D", "E"])
y = np.array([3, 8, 1, 10, 22])

plt.bar(x,y, color = 'blue', width = 0.4)
plt.show()