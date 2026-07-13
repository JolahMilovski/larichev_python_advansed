from functools import wraps


def limit_arg(max_value: int, mode: str):
    def arg_limiter(func):
        @wraps(func)
        def wrapper(*args,**kwarg):
            
            for v in kwarg.values():
                if v == mode:
                    new_arg = tuple(arg if arg <= max_value else max_value for arg in args)
                    result = func(*new_arg)
                    return result                  
                      
            
            for arg in args:
                if arg >= max_value:
                    raise ValueError("Arg value >= 10")
                result = func(*args,**kwarg)
                return result                  
                       
            
        return wrapper
    return arg_limiter
    


@limit_arg(max_value=13, mode="clip")
def multyply(a,b):
    print(f" {a*b}")

multyply(2,4)
multyply(2,30, clip="clip")



"""
decorator - errror handler
"""
import random

def retry(time: int):
    def error_handling(func):
        def wrapper(*args):
            print(f"start trying")
            for attemp in range(time):
                try:
                    unstable = func(*args)
                except Exception as e:
                    print(f" at {attemp} error {e}")
            print(f"After {time} time func stop")
        return wrapper
    
    return error_handling



@retry(3)
def unstable():
    """
    return random value and raise error
    """
    if random.random() < 0.7:
        raise ValueError("Error in random")
    print("Random success")

#nstable()


"""
nested decorator
"""

def repeat(times:int):
    """
    repeat nested func
    """
    def repeat_decocator(func):
        print(f"start repeat decorator")
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            print("stop repeating")
            return result
        return wrapper
    return repeat_decocator



@repeat(2)
def new_say_hello():
    print(f'Hello')

#new_say_hello()

"""
class decorator example

"""
def repr_deco(cls):

    def __repr__(self):
            return f"{cls.__name__} ( {self.__dict__})"
    cls._repr__ = __repr__
    return cls

def log_call(func):
    """add log """
    def wrapper(*args):
        print(f"\ncall {func.__qualname__} args = {args}\n")
        return func(*args)
    return wrapper



@repr_deco
class User:
    """User"""

    def __init__(self,name, age):
        self.name = name
        self.age = age


    @repeat(2)
    @log_call  
    def print_name_n_time(self, time: int):
        print(f"{self.name * time}")
        return f"{self.name * time}"
    


#user = User("Anton", 25)
#print("Start repeat Anton")
#user.print_name_n_time(5)
#print(f"\nnew user {user.name}, {user.age} old\n")

"""
log decorator example

"""

def log_say_hello(func):
    """primary decorator"""
    def wrap():
        print("Before func")
        func()
        print("After func")
    return wrap
     
@log_say_hello
def say_hello():
    """func print Hello"""
    print("Hello")

def log_func(func):
    """log inner func with arg and return result"""
    def wrap(*arg, **kwarg):
        print(f" Run {func.__name__} function with arg {arg} & {kwarg}")
        result = func(*arg,**kwarg)
        print(f" after {func.__name__} ")
        return result
    return wrap

@log_func
def add(a:int, b:int):
    #print(f"sum = {a + b}")
    return a+b

#say_hello()
#res = add(1, 3)
#print(f"{res}")
