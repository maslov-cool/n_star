import tkinter
import math
window = tkinter.Tk()
canvas = tkinter.Canvas(window, bg='white', height=1000, width=1000)
canvas.pack()

r = 300

while not ((n := input()).isdigit() and int(n) > 1):
    print('Некорректный ввод')
n = int(n)

for k in range(1, n + 1):
    k1 = k + math.ceil(n / 2)
    if k1 > n:
        k1 -= n
    x_y_0 = (400 + r * math.cos(2 * math.pi * k / n), 400 + r * math.sin(2 * math.pi * k / n))
    x_y_1 = (400 + r * math.cos(2 * math.pi * k1 / n), 400 + r * math.sin(2 * math.pi * k1 / n))
    canvas.create_line(x_y_0, x_y_1, fill='red')

window.mainloop()
