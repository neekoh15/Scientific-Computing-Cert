//You can use this code as guidance but DO NOT COPY/PASTE IT into your proyect, this code has copyrights

import copy
import random
# Consider using the modules imported above.


class Hat:
  def __init__(self, yellow=0,red=0,green=0,blue=0,test=0):
    self.contents = []
    
    for x in range(yellow):
      self.contents.append("yellow")

    for x in range(red):
      self.contents.append("red")

    for x in range(green):
      self.contents.append("green")

    for x in range(blue):
      self.contents.append("blue")

    for x in range(test):
      self.contents.append("test")

  def draw(self,value):
    aux = list()
    for x in range(value):
      aux.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
      
    return(aux)
      
      


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  expected = []
  index = 0
  asserts = 0
  
  for x in expected_balls.values():
    for i in range(x):
        expected.append(list(expected_balls)[index])
    index+= 1
  #Aca ya tengo armada la lista expected

  #ahora a armar la lista results
  for x in range(num_experiments):
    
    if num_balls_drawn >= len(hat.contents):
        results = hat.contents.copy()
    else:
        results = random.choices(hat.contents, k= num_balls_drawn)
    copy_of_results = results.copy()

    for element in expected:
        if element in results: results.remove(element)
          
    if (len(results) == (len(copy_of_results)-len(expected))):  asserts +=1
      
  return(asserts/num_experiments)


prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
