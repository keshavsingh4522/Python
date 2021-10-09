import copy
import random


class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
        self.contents += [k] * int(v)
  
  def draw(self,amount):
      draw_list = []
      if amount >= len(self.contents):
          return self.contents
      for i in range(amount):
          name=self.contents.pop(random.randrange(len(self.contents)))
          draw_list.append(name)
      return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colors_gotten = hat_copy.draw(num_balls_drawn)
    for color in colors_gotten:
      if(color in expected_copy):
        expected_copy[color]-=1
    
    if(all(x <= 0 for x in expected_copy.values())):
      count += 1

  return count / num_experiments