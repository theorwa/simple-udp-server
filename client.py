from collections import namedtuple
import pickle # or cPickle, it's faster
import socket

listen_packet_t = namedtuple("listen_packet_t", "magic port_number shell_command")

UDP_IP = "127.0.0.1"
UDP_PORT = 8888
# MESSAGE = "Hello, World!"

tuple_to_send  = listen_packet_t(magic=100, port_number=8888, shell_command="")
print(tuple_to_send)

string_to_send = pickle.dumps(tuple_to_send)
print(string_to_send)

# print("UDP target IP:", UDP_IP)
# print("UDP target port:", UDP_PORT)
# print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(string_to_send, (UDP_IP, UDP_PORT))