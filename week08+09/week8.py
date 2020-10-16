#作业一：
#容器序列：list、tuple、collections.deque
#扁平序列：str
#可变序列：list、dict
#不可变序列：tuple、str

#作业二：
import time
from typing import Callable, Iterable

def home_brew_map(func: Callable, iterable: Iterable):
  klass = iterable.__class__
  empty = klass()
  for item in iterable:
    empty += klass([func(item)])
  return empty

#作业三：
def timer(func):
  def inner(*args, **kwargs):
    start = time.time()
    ret = func(*args, **kwargs)
    elapsed = time.time() - start
    print(elapsed)
    return ret
  return inner


@timer
def long_run_func(*args, **kwargs):
  print(args)
  print(kwargs)
  time.sleep(1)


def main():
  long_run_func(1, 2, 3, arg1='foobar', arg2=1)
  print(home_brew_map(lambda x: x ** x, [1, 2, 3, 4, 5]))
  print(home_brew_map(lambda x: x ** x, (1, 2, 3, 4, 5)))


if __name__ == '__main__':
  main()