#!/usr/bin/env python3
import socket
import sys

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    s.bind(("0.0.0.0", 8888))
except OSError as exc:
    print(f"Port 8888 unavailable: {exc}", file=sys.stderr)
    sys.exit(1)
finally:
    s.close()
