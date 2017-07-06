import socket
import os
import socket, fcntl, struct

def get_ip():
    out = os.popen("ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $1}' | head -1").read()
    return str(out)
