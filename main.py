width = 36
height = 18
speed = 8

import os, time
from random import randint

os.system("stty cbreak -echo min 0")
os.write(0, "\x1b[2J\x1b[?25l")

f = [[-9] * width] + [[-9] + [0] * (width - 2) + [-9] for _ in range(height - 2)] + [[-9] * width]
x = width / 2
y = height / 2
u = v = 0
l = 0
dx = 1
dy = 0
key = ""
f[y][x + 1] = -2

try:
	while "q" not in key:

		os.write(0, "\x1b[1;1H")
		q = p = [0] * width

		for r in f + [q]:
			print "".join(("|"*(abs(x - y) > 1) or " _"[abs(y - x) < 2 > abs(a - z) and abs(x-a) > 1]) + "_ "[abs(y - z) < 2] for x, y, z, a in zip([0] + p, p + [0], r + [0], [0] + r))[:-1]
			p=r
		time.sleep(1.0 / speed)

		key = os.read(1, 9)

		if "A" in key: dx = 0; dy = -1
		if "B" in key: dx = 0; dy = 1
		if "C" in key: dx = 1; dy = 0
		if "D" in key: dx = -1; dy = 0
		x += dx
		y += dy
		if x < 0: x += width
		if x == width: x = 0
		if y < 0: y += height
		if y == height: y = 0

		f = [[[c, c <= l and c + 1][c > 0] for c in row] for row in f]
		if f[y][x]:
			if f[y][x] == -2:
				l += 1
				while f[v][u]:
					u = randint(1, width - 2)
					v = randint(1, height - 2)
				f[v][u] = -2
			else: key = "q"
		f[y][x] = 2

except KeyboardInterrupt: pass
os.system("stty sane")
print "\x1b[?25hLength:", l

