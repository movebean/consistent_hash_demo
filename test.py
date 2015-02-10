import memcache
import hash_ring

SERVER_LIST = ['localhost:11211', 'localhost:11212']
SERVER_DICT = {}
for server in SERVER_LIST:
  SERVER_DICT[server] = memcache.Client([server])

HASH_OBJ = hash_ring.HashRing(SERVER_LIST)

def TestAddValue(key, value):
  server = HASH_OBJ.get_node(key)
  print server
  SERVER_DICT[server].set(key, value)
  print SERVER_DICT[server].get(key)

TestAddValue('hello', 'world')
TestAddValue('hello1', 'world1')
