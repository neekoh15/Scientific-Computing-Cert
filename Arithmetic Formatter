//You can use this code as guidance but DO NOT COPY/PASTE IT into your proyect, this code has copyrights


def error1():
  print("Error: Too many problems.")

def error2():
  print("Error: Numbers must only contain digits.")

def error3():
  print("Error: Operator must be '+' or '-'.")

def error4():
  print("Numbers and operators must be seperated with space.")

def error5():
  print("Error: Numbers cannot be more than four digits.")


def arithmetic_arranger(*vals):
  container = list()
  keep_going = True

  if len(vals[0]) >5:
    print("Error: Too many problems.")
    keep_going = False

  for i in vals[0]:
    extractor = i.split()
    if len(extractor) != 3:
      keep_going = False
      error4()
      break

    if len(extractor[0]) > 4:
      keep_going = False
      error5()
      break

    if len(extractor[1]) > 4:
      keep_going = False
      error5()
      break

    if extractor[1] != "+" and extractor[1] != "-":
      keep_going = False
      error3()
      break
      
    for j in extractor[0]:
      try:
        number = int(j)
      except:
        keep_going = False
        error2()
        break
    
    for k in extractor[2]:
      try:
        number = int(k)
      except:
        error2()
        keep_going = False
        break

    if keep_going == True:
      content = (extractor[0],extractor[2],extractor[1])
      container.append(content)

  if keep_going == True:
    if len(vals)>1:
      display(container, vals[1])
    else:
      display(container)


def display(*args):

  helper1 = list()
  helper2 = list()
  helper3 = list()

  upper_numbers = list()
  lower_numbers = list()
  operations = list()
  results = list()

  display_upper_section = str()
  display_lower_section = str()
  display_dashes = str()
  display_results = str()
  display = str()

  space = " "
  dashes = "-"
  
  receiver = args[0]
  

  for i in range(len(receiver)):
    upper_numbers.append(receiver[i][0])


  for i in range(len(receiver)):
    lower_numbers.append(receiver[i][1])


  for i in range(len(receiver)):
    operations.append(receiver[i][2])


  for i in range(len(receiver)):
    if receiver[i][2] == "+":
      results.append(int(receiver[i][0])+int(receiver[i][1]))
    if receiver[i][2] == "-":
      results.append(int(receiver[i][0])-int(receiver[i][1]))


  for i in range(len(receiver)):
    helper1 = max(len(str(upper_numbers[i])),len(str(lower_numbers[i])))
    helper2 = max(len(space*(helper1 -len(upper_numbers[i])+2) + upper_numbers[i]), len(operations[i]+ space + space*(helper1 -len(lower_numbers[i]))+ lower_numbers[i]))
    #helper3 = max(len)
    display_upper_section = display_upper_section + space*(helper1 -len(upper_numbers[i])+2) + upper_numbers[i] + space*4
    display_lower_section = display_lower_section + operations[i]+ space + space*(helper1 -len(lower_numbers[i]))+ lower_numbers[i] + space*4
    display_dashes = display_dashes + dashes*helper2 + space*4
    display_results = display_results + space*(helper1 -len(str(results[i]))+2) + str(results[i]) + space*4

  print(display_upper_section)
  print(display_lower_section)
  print(display_dashes)
  try:
    if args[1] == True:
      print(display_results)
  except:
    print(" ")



arithmetic_arranger(["2 + 3","7 + 2", "442 + 435", "1250 + 9000"], True)
