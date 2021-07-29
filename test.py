import time

scale = 50

print('start to simulate....\n')

start_time = time.perf_counter()
for i in range(scale+1):
	a = '*'*i
	b = "."*(scale - i)
	c = (i/scale)*100
	dur = time.perf_counter()-start_time
	print('\r {:3.0f}%[{}->{}]{:.2f}s'.format(c, a, b, dur), end='  ')
	time.sleep(0.1)

print('\n\n game is over! \n')

