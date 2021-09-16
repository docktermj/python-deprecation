#! /usr/bin/env python3

import functools
import warnings

SENZING_PRODUCT_ID = "5027"  # See https://github.com/Senzing/knowledge-base/blob/master/lists/senzing-product-ids.md

def deprecated(instance):
    def the_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.simplefilter('always', DeprecationWarning)  # turn off filter
            warnings.warn(
                "senzing-{0}{1:04d}W Call to deprecated function {2}.".format(SENZING_PRODUCT_ID, instance, func.__name__),
                category=DeprecationWarning,
                stacklevel=2)
            warnings.simplefilter('default', DeprecationWarning)  # reset filter
            return func(*args, **kwargs)
        return wrapper
    return the_decorator

# -- Example functions and classes -------------------------------------------

@deprecated(7001)
def some_old_function(x, y):
    return x + y

class SomeClass:
    @deprecated(7002)
    def some_old_method(self, x, y):
        return x + y

# -- Main ---------------------------------------------------------------------

if __name__ == "__main__":

    some_old_function(1,2)

    my_class = SomeClass()
    my_class.some_old_method(3,4)
