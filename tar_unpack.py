# METIN Suite II 0.9.2 TAR unpacker
# Better play this than METIN II

import sys
import os

def toint(x):
	return int.from_bytes(x, byteorder='little', signed=False)

if len(sys.argv) < 2:
	print("usage: %s [file]" % (sys.argv[0]))
	sys.exit(0)

current_tar = sys.argv[1]
f = open(current_tar, "rb")
n = toint(f.read(4))
print("tar %s files %u" % (current_tar, n))

os.mkdir(current_tar + "_unpack")

for i in range(n):
	# Header
	undecoded_filename = f.read(32)
	delpos = 0
	for k in range(len(undecoded_filename)):
		if undecoded_filename[k] == 0:
			delpos = k
			break

	undecoded_filename = undecoded_filename[:delpos]
	filename = undecoded_filename.decode('cp949')
	offset = toint(f.read(4))
	size = toint(f.read(4))
	print("file %s (%u/%u) size %u offset %u" % (filename, i + 1, n, size, offset))
	
	if size < 1:
		continue
	
	f.seek(offset, 0)
	sf = open(current_tar + "_unpack" + "/" + filename, "wb")
	sf.write(f.read(size))
	sf.close()
	
	f.seek(4+(i*40), 0)
