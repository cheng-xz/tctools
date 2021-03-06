# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _JMQSTestLib
else:
    import _JMQSTestLib

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _JMQSTestLib.delete_SwigPyIterator

    def value(self):
        return _JMQSTestLib.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _JMQSTestLib.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _JMQSTestLib.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _JMQSTestLib.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _JMQSTestLib.SwigPyIterator_equal(self, x)

    def copy(self):
        return _JMQSTestLib.SwigPyIterator_copy(self)

    def next(self):
        return _JMQSTestLib.SwigPyIterator_next(self)

    def __next__(self):
        return _JMQSTestLib.SwigPyIterator___next__(self)

    def previous(self):
        return _JMQSTestLib.SwigPyIterator_previous(self)

    def advance(self, n):
        return _JMQSTestLib.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _JMQSTestLib.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _JMQSTestLib.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _JMQSTestLib.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _JMQSTestLib.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _JMQSTestLib.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _JMQSTestLib.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _JMQSTestLib:
_JMQSTestLib.SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _JMQSTestLib.SHARED_PTR_DISOWN
class JMQSTest(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _JMQSTestLib.JMQSTest_swiginit(self, _JMQSTestLib.new_JMQSTest(*args))
    __swig_destroy__ = _JMQSTestLib.delete_JMQSTest

    def push_msg(self, strRid):
        return _JMQSTestLib.JMQSTest_push_msg(self, strRid)

    def pull_msg(self, strRid, maxFetch, maxWaitSeconds=1):
        return _JMQSTestLib.JMQSTest_pull_msg(self, strRid, maxFetch, maxWaitSeconds)

    def pull_msg_async(self, strRid, maxFetch):
        return _JMQSTestLib.JMQSTest_pull_msg_async(self, strRid, maxFetch)

    def pull_msg_direct(self, strRid, maxFetch):
        return _JMQSTestLib.JMQSTest_pull_msg_direct(self, strRid, maxFetch)

    def product_msg(self, strRid, msgs, etype=0):
        return _JMQSTestLib.JMQSTest_product_msg(self, strRid, msgs, etype)

    def product_msg_async(self, strRid, msgs, etype=0):
        return _JMQSTestLib.JMQSTest_product_msg_async(self, strRid, msgs, etype)

    def genMsg(self, *args):
        return _JMQSTestLib.JMQSTest_genMsg(self, *args)

    def async_get(self):
        return _JMQSTestLib.JMQSTest_async_get(self)

    def async_set(self, *args):
        return _JMQSTestLib.JMQSTest_async_set(self, *args)

    def async_clean(self):
        return _JMQSTestLib.JMQSTest_async_clean(self)

# Register JMQSTest in _JMQSTestLib:
_JMQSTestLib.JMQSTest_swigregister(JMQSTest)


def ConsumerCb(cookie, rid, sid, imsg):
    return _JMQSTestLib.ConsumerCb(cookie, rid, sid, imsg)

def PullConsumerCb(rid, sid, cstatus, cookie):
    return _JMQSTestLib.PullConsumerCb(rid, sid, cstatus, cookie)

def ProductCb(ret, cookie):
    return _JMQSTestLib.ProductCb(ret, cookie)
class IntVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _JMQSTestLib.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _JMQSTestLib.IntVector___nonzero__(self)

    def __bool__(self):
        return _JMQSTestLib.IntVector___bool__(self)

    def __len__(self):
        return _JMQSTestLib.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _JMQSTestLib.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _JMQSTestLib.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _JMQSTestLib.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _JMQSTestLib.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _JMQSTestLib.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _JMQSTestLib.IntVector___setitem__(self, *args)

    def pop(self):
        return _JMQSTestLib.IntVector_pop(self)

    def append(self, x):
        return _JMQSTestLib.IntVector_append(self, x)

    def empty(self):
        return _JMQSTestLib.IntVector_empty(self)

    def size(self):
        return _JMQSTestLib.IntVector_size(self)

    def swap(self, v):
        return _JMQSTestLib.IntVector_swap(self, v)

    def begin(self):
        return _JMQSTestLib.IntVector_begin(self)

    def end(self):
        return _JMQSTestLib.IntVector_end(self)

    def rbegin(self):
        return _JMQSTestLib.IntVector_rbegin(self)

    def rend(self):
        return _JMQSTestLib.IntVector_rend(self)

    def clear(self):
        return _JMQSTestLib.IntVector_clear(self)

    def get_allocator(self):
        return _JMQSTestLib.IntVector_get_allocator(self)

    def pop_back(self):
        return _JMQSTestLib.IntVector_pop_back(self)

    def erase(self, *args):
        return _JMQSTestLib.IntVector_erase(self, *args)

    def __init__(self, *args):
        _JMQSTestLib.IntVector_swiginit(self, _JMQSTestLib.new_IntVector(*args))

    def push_back(self, x):
        return _JMQSTestLib.IntVector_push_back(self, x)

    def front(self):
        return _JMQSTestLib.IntVector_front(self)

    def back(self):
        return _JMQSTestLib.IntVector_back(self)

    def assign(self, n, x):
        return _JMQSTestLib.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _JMQSTestLib.IntVector_resize(self, *args)

    def insert(self, *args):
        return _JMQSTestLib.IntVector_insert(self, *args)

    def reserve(self, n):
        return _JMQSTestLib.IntVector_reserve(self, n)

    def capacity(self):
        return _JMQSTestLib.IntVector_capacity(self)
    __swig_destroy__ = _JMQSTestLib.delete_IntVector

# Register IntVector in _JMQSTestLib:
_JMQSTestLib.IntVector_swigregister(IntVector)

class DoubleVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _JMQSTestLib.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _JMQSTestLib.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _JMQSTestLib.DoubleVector___bool__(self)

    def __len__(self):
        return _JMQSTestLib.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _JMQSTestLib.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _JMQSTestLib.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _JMQSTestLib.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _JMQSTestLib.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _JMQSTestLib.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _JMQSTestLib.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _JMQSTestLib.DoubleVector_pop(self)

    def append(self, x):
        return _JMQSTestLib.DoubleVector_append(self, x)

    def empty(self):
        return _JMQSTestLib.DoubleVector_empty(self)

    def size(self):
        return _JMQSTestLib.DoubleVector_size(self)

    def swap(self, v):
        return _JMQSTestLib.DoubleVector_swap(self, v)

    def begin(self):
        return _JMQSTestLib.DoubleVector_begin(self)

    def end(self):
        return _JMQSTestLib.DoubleVector_end(self)

    def rbegin(self):
        return _JMQSTestLib.DoubleVector_rbegin(self)

    def rend(self):
        return _JMQSTestLib.DoubleVector_rend(self)

    def clear(self):
        return _JMQSTestLib.DoubleVector_clear(self)

    def get_allocator(self):
        return _JMQSTestLib.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _JMQSTestLib.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _JMQSTestLib.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        _JMQSTestLib.DoubleVector_swiginit(self, _JMQSTestLib.new_DoubleVector(*args))

    def push_back(self, x):
        return _JMQSTestLib.DoubleVector_push_back(self, x)

    def front(self):
        return _JMQSTestLib.DoubleVector_front(self)

    def back(self):
        return _JMQSTestLib.DoubleVector_back(self)

    def assign(self, n, x):
        return _JMQSTestLib.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _JMQSTestLib.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _JMQSTestLib.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _JMQSTestLib.DoubleVector_reserve(self, n)

    def capacity(self):
        return _JMQSTestLib.DoubleVector_capacity(self)
    __swig_destroy__ = _JMQSTestLib.delete_DoubleVector

# Register DoubleVector in _JMQSTestLib:
_JMQSTestLib.DoubleVector_swigregister(DoubleVector)

class StringVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _JMQSTestLib.StringVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _JMQSTestLib.StringVector___nonzero__(self)

    def __bool__(self):
        return _JMQSTestLib.StringVector___bool__(self)

    def __len__(self):
        return _JMQSTestLib.StringVector___len__(self)

    def __getslice__(self, i, j):
        return _JMQSTestLib.StringVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _JMQSTestLib.StringVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _JMQSTestLib.StringVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _JMQSTestLib.StringVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _JMQSTestLib.StringVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _JMQSTestLib.StringVector___setitem__(self, *args)

    def pop(self):
        return _JMQSTestLib.StringVector_pop(self)

    def append(self, x):
        return _JMQSTestLib.StringVector_append(self, x)

    def empty(self):
        return _JMQSTestLib.StringVector_empty(self)

    def size(self):
        return _JMQSTestLib.StringVector_size(self)

    def swap(self, v):
        return _JMQSTestLib.StringVector_swap(self, v)

    def begin(self):
        return _JMQSTestLib.StringVector_begin(self)

    def end(self):
        return _JMQSTestLib.StringVector_end(self)

    def rbegin(self):
        return _JMQSTestLib.StringVector_rbegin(self)

    def rend(self):
        return _JMQSTestLib.StringVector_rend(self)

    def clear(self):
        return _JMQSTestLib.StringVector_clear(self)

    def get_allocator(self):
        return _JMQSTestLib.StringVector_get_allocator(self)

    def pop_back(self):
        return _JMQSTestLib.StringVector_pop_back(self)

    def erase(self, *args):
        return _JMQSTestLib.StringVector_erase(self, *args)

    def __init__(self, *args):
        _JMQSTestLib.StringVector_swiginit(self, _JMQSTestLib.new_StringVector(*args))

    def push_back(self, x):
        return _JMQSTestLib.StringVector_push_back(self, x)

    def front(self):
        return _JMQSTestLib.StringVector_front(self)

    def back(self):
        return _JMQSTestLib.StringVector_back(self)

    def assign(self, n, x):
        return _JMQSTestLib.StringVector_assign(self, n, x)

    def resize(self, *args):
        return _JMQSTestLib.StringVector_resize(self, *args)

    def insert(self, *args):
        return _JMQSTestLib.StringVector_insert(self, *args)

    def reserve(self, n):
        return _JMQSTestLib.StringVector_reserve(self, n)

    def capacity(self):
        return _JMQSTestLib.StringVector_capacity(self)
    __swig_destroy__ = _JMQSTestLib.delete_StringVector

# Register StringVector in _JMQSTestLib:
_JMQSTestLib.StringVector_swigregister(StringVector)



