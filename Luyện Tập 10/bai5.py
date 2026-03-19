import numpy as np
import matplotlib.pyplot as plt

# Tạo dữ liệu
x = np.linspace(0, 10, 100)
y1 = x**2
y2 = np.sqrt(x)

# Tạo figure gồm 1 hàng, 2 cột
plt.figure(figsize=(10, 4))

# Subplot bên trái
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Đồ thị y = x^2")
plt.xlabel("x")
plt.ylabel("y")

# Subplot bên phải
plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Đồ thị y = sqrt(x)")
plt.xlabel("x")
plt.ylabel("y")

# Hiển thị
plt.tight_layout()
plt.show()