
net = [200, 100, 33, 64]
broad = list(net)
brange = 32 - 23
for i in range(brange):
	broad[int(3 - i/8)] = broad[int(3 - i/8)] + (1 << (i % 8))

print("broad: ", broad)
