
# ----------------------------------------------------------------
# What is memory?
# Memory is an important component of your computer.
# Memory can be checked via Computer Task Manager - my laptop has a memory size of 16GB
# 16GB = 16,000 MB = 16,000,000 KB = 16,000,000,000 bytes
# 1 byte = 8 bits
# 1 bit can be either 0 or 1
#
# 1 byte is one basic unit in your memory
# ---------------------------------------------------------------

# each int / float / bool / str variable takes spaces

import sys

int_a = 0
print(f"variable int_a takes {sys.getsizeof(int_a)} bytes in memory")

bool_a = True
print(f"variable bool_a takes {sys.getsizeof(bool_a)} bytes in memory")

float_a = 0.1
print(f"variable float_a takes {sys.getsizeof(float_a)} bytes in memory")

str_a = 'Python is very fun!'
print(f"variable str_a takes {sys.getsizeof(str_a)} bytes in memory")

list_a = list(range(100))
print(f"variable list_a takes {sys.getsizeof(list_a)} bytes in memory")
