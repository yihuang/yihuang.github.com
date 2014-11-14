from libc.stdlib cimport atoi

cdef extern const char* c_getenv "getenv"(const char*)

def getenv(s):
    return atoi(c_getenv(<const char*>s))

def f1(double x):
    return x**2-x
def f2(x):
    return x**2-x

cdef int i
for i in range(10):
    pass
for j in range(10):
    pass
