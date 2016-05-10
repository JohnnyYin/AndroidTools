import os
import sys
import struct

def is_png(data):
    return (data[:8] == '\211PNG\r\n\032\n'and (data[12:16] == 'IHDR'))

def get_image_info(data):
    if is_png(data):
        w, h = struct.unpack('>LL', data[16:24])
        width = int(w)
        height = int(h)
    else:
        raise Exception('not a png image')
    return (width, height)

def main():
	def walk_cb(arg, dirname, fnames):
		for f in fnames:
			if f.endswith('.jpg') or f.endswith('png'):
				data = open(dirname + '/' + f, 'rb').read()
				try:
					width, height = get_image_info(data)
					if width <= 1 or height <= 1:
						print dirname + '/' + f + " [" + str(width) + ", " + str(height) + ']'
				except Exception, e:
					print e
					pass
	os.path.walk('res', walk_cb, None)

if __name__ == '__main__':
    main()