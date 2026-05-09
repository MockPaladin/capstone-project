from __future__ import annotations
import math
from typing import Literal, Self, Tuple


class Vector:
    
  def __init__(self, values: Tuple[int, ...]) -> None:
        
    self.v = values
    self.d = len(self.v)
        
  def checkVector(self, other: Vector) -> bool:

    if self.d == other.d:
      return True
            
    else:  
      raise ValueError("Vector " + str(self) + " does not have same dimension as Vector " + str(other) + ".")
    
  def cross(self, other: Vector) -> Vector | int | ValueError: # type: ignore
        
    if self.checkVector(other):
            
      if self.d == 3:
                
        vec = (self.v[1]*other.v[2] - self.v[2]*other.v[1],
               self.v[2]*other.v[0] - self.v[0]*other.v[2],
               self.v[0]*other.v[1] - self.v[1]*other.v[0])  
        return Vector(vec)
                
      elif self.d == 2:
        vec = self.v[0] * other.v[1] - self.v[1] * other.v[0]
        return vec
            
      else:       
        raise ValueError("Vector " + str(self) + " with dimension " + str(self.d) + " does not have a dimension of 2 or 3, which are the only two dimensions supported for the cross() function.")
        
    def __str__(self: Self) -> str:
        
        _str = ""
        
        for i in range(self.d):
            
            _str += str(self.v[i])
            if i < self.d - 1: _str += ", "
        
        return "⟨" + _str + "⟩"
    
    def __add__(self: Self, other):
        
        if not self.checkVector(other):
            
            return False
        
        new_vec = [self.v[i] + other.v[i] for i in range(self.d)]
            
        return Vector(new_vec)
    
    def __sub__(self: Self, other: Vector) -> Vector | Literal[False]:
        
        if not self.checkVector(other):
            
            return False
        
        new_vec = [self.v[i] - other.v[i] for i in range(self.d)]
        
        return Vector(new_vec)
    
    def __abs__(self: Self) -> float:
        
        magnitude = math.hypot(*self.v) # needed a variable name ok
        
        return magnitude
    
    def __gt__(self, other):
        
        return abs(self) > abs(other)
    
    def __lt__(self, other):
        
        return abs(self) < abs(other)
    
    def __eq__(self: Self, other):
        
        return self.v == other.v
    
    def __mul__(self: Self, other: Vector) -> Vector:
        
        if self.checkVector(other):
            vec = Vector([self.v[i] * other.v[i] for i in range(self.d)])
                         
        elif isinstance(other, float) or isinstance(other, int):
            vec = Vector([self.v[i] * other for i in range(self.d)])
                         
        return vec
    
    def __rmul__(self, other: Vector) -> Vector:
        return self.__mul__(other)