import copy
import random


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  expected_count_list = list()
  matches = 0
  count = 0
  for i in range(num_experiments):
    hat_clone = copy.deepcopy(hat)
    expected_clone = copy.deepcopy(expected_balls)
    drawn = hat_clone.draw(num_balls_drawn)

    for key, value in expected_clone.items():
      for i in drawn:
        if i == key:
          count += 1
      expected_count = (count // value)
      expected_count_list.append(expected_count)
      count = 0

    match = min(expected_count_list)
    matches += match
    expected_count_list.clear()

  probability = (matches / num_experiments)

  return probability


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      self.color_name = k
      while v > 0:
        self.contents.append(self.color_name)
        v -= 1
    self.contents_reset = copy.deepcopy(self.contents)

  def draw(self, number):
    if (len(self.contents) - number) >= 0:
      self.selection = random.sample(self.contents, number)
      for i in self.selection:
        try:
          self.contents.remove(i)
        except ValueError:
          pass
      return self.selection
    else:
      return self.contents_reset
