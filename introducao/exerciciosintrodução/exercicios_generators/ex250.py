size = [1024,2048,4096,8129,16384]
megabyte_converter = (s / 1048576 for s in size)
for i in megabyte_converter:
    print(i)