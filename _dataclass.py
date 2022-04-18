from dataclasses import dataclass, field
from typing import Any, Callable, TypeAlias
from functools import wraps

Function: TypeAlias = Callable[[Any], Any]

def debug(func: Function) -> Function:
  @wraps(func)
  def wrapper(*args: list[Any], **kwargs: dict[Any, Any]) -> Any:
    kw_repr = ", ".join([ f"{k}={v!r}" for k, v in kwargs.items()])
    kw_repr = f", {kw_repr}" if kw_repr else kw_repr
    arg_repr = ", ".join([f"{v!r}" for v in args])
    arguments = f"{arg_repr}{kw_repr}"
    print(f"Calling {func.__name__}({arguments})")
    res = func(*args, **kwargs)
    print(f"{func.__name__} returned: {res}")
    print("End")
    return res
  return wrapper

def loop(max_repeat: int =1) -> Function:
    def decorator(func: Function) -> Function:
      @wraps(func)
      def wrapper(*args: list[Any], **kwargs: dict[Any, Any]) -> list[Any]:
        return [func(*args, **kwargs) for _ in range(max_repeat)]
      return wrapper
    return decorator

@dataclass
class Count:
  func: Function
  num_calls: int = field(init=False, default=0)
  
  def __call__(self, *args: list[Any], **kwargs: dict[Any, Any]) -> Any:
    self.num_calls += 1
    res = self.func(*args, **kwargs)
    print(f"Function {self.func.__name__}() called {'once'if self.num_calls== 1 else f'{self.num_calls} times'} and returned {res}")
    return res

@loop(max_repeat=2)
@Count
@debug
def hello(name: str, **kwargs: dict[str, Any])-> tuple[str, dict[Any, Any]]:
  print(f"Hello {name}")
  return (name, kwargs)
  
  
hello( "Eliam", last_name="LOTONGA", age=1421 )


@dataclass
class Person:
  last_name: str
  first_name: str
  age: int = field(repr=False)
  excludes: list[str] = field(default_factory=list, repr=False, init=False)
  
  
  def __post_init__(self):
    # add some excluded attributes
    self.excludes = [attr.name for attr in self.__dataclass_fields__.values() if not attr.repr]
  
  
  # reproduce the basic repr function
  def string(self):
    str_p = f"{self.__class__.__name__}({', '.join([ f'{k}={v!r}' for k, v in self.__dict__.items() if k not in self.excludes ])})"
    return str_p

  
p = Person("Eliam", "LOTONGA", 1421)
print("--"*10, "Dataclass repr", "--"*10)
print(f"Original repr():\n{p}")
print(f"Custom repr():\n{p.string()}")

assert p.__repr__() == p.string(), f"repr strings not equals:\n{p.__repr__()} != {p.string()}"
