//You can use this code as guidance but DO NOT COPY/PASTE IT into your proyect, this code has copyrights

class Category:

  def __init__(self, category):
    self.ledger = []
    self.category = category
  
  def deposit(self, *vals):
    
    if vals == None:
      return("")
      
    else:
      if len(vals) ==2:
        self.ledger.append({"amount":vals[0], "description":vals[1]})
      else:
        self.ledger.append({"amount":vals[0], "description":""})
    
  
  def withdraw(self, *vals):
    #print("vals dentro de withdraw: ", vals)
    
    if self.check_funds(vals[0]):
      if len(vals) ==2:
        self.ledger.append({"amount":-vals[0],"description":vals[1]})
        return(True)
      else:
        self.ledger.append({"amount":-vals[0],"description":""})
        return(True)
    else:
      return(False)
  
  def get_balance(self):
    balanceList = []
    for x in self.ledger:
      balanceList.append(x["amount"])
    return(sum(balanceList))
  
  def transfer(self, amount, obj):

    if (self.check_funds(amount)):
      self.ledger.append({"amount":-amount,"description":"Transfer to {}".format(obj.category)})
      obj.ledger.append({"amount":amount,"description":"Transfer from {}".format(self.category)})

      return(True)
    else:
      return(False)

  
  def check_funds(self, amountToTake):
    
    if self.get_balance() >= amountToTake:
      return(True)
      
    else: return(False)

  def __str__(self):
    
    lengthOfCategory = len(self.category)
    
    body,header, auxStr, footer = str(),str(), str(), str()
    
    header = "*"*((30 - lengthOfCategory)//2) + self.category + "*"*((30 - lengthOfCategory)//2) + "\n"
    
    for item in self.ledger:
        if len(item["description"]) < 23:
            spaces = 30-len(item["description"]) - len(str("%.2f" %item["amount"]))
            body += item["description"] +" "*spaces+ str("%.2f" %item["amount"])+"\n"
        else:
            for letter in range(23):
               auxStr += item["description"][letter]
            spaces = 30-23 - len(str("%.2f" %item["amount"]))
            body += auxStr +" "*spaces+ str("%.2f" %item["amount"])+"\n"
            auxStr= str()
    footer = "Total: "+ str("%.2f" %self.get_balance())
    string = header + body + footer
    
    return (string)
    
def create_spend_chart(categories):
  
  totalWithdraws = 0
  listOfCategoriesNames = [] 
  individualWithdraws = []
  
  for cat in categories:
    #listOfCategoriesNames.append(cat.category)
    listOfCategoriesNames.append(cat.category)
    auxCounter = 0
    for item in cat.ledger:
      
      if item["amount"] < 0:
        #print("Category: "+ cat.category +". withdraw amount: "+ str(item["amount"])+ ". description: "+ item["description"])
        totalWithdraws += (abs(item["amount"]))
        auxCounter += (abs(item["amount"]))
    individualWithdraws.append(auxCounter)
    
  #print(totalWithdraws)
  #print(individualWithdraws)
  percents = [int((x/totalWithdraws)*10)*10 for x in individualWithdraws]
  #print(percents)
  longestName = max(listOfCategoriesNames,key=len)

  chartsRow = str()
  categoriesRow = str()
  upperGraph = str()
  lowerGraph = str()
    
  for files in range(11):
    
    spaces = 3-(len(str(100-10*files)))
    percentValue = 100-10*files
    percentsRow = " "*spaces+str(percentValue)+"| "
    
    for x in percents:
        
        if percentValue <= x:
            chartsRow += "o  "
        else:
            chartsRow += "   "
    else: chartsRow +="\n"
        
    divisorLine = " "*4+"-"+"-"*(3*len(percents))
    
    upperGraph += percentsRow+chartsRow
    chartsRow = str()
  upperGraph += divisorLine+"\n"
  #print(upperGraph)
  #------------------ lower grapth: ------------------
  
  for filas in range(len(longestName)):
    
    blanks = " "*5
    
    for itemName in listOfCategoriesNames:
        #print(itemName, len(itemName))
        if filas < len(itemName):
            categoriesRow += itemName[filas]+"  "
            
        else:
            categoriesRow += "   "
    else:
      if filas != len(longestName)-1:
        categoriesRow += "\n"
        
    lowerGraph += blanks + categoriesRow
    categoriesRow = str()
  #print(categoriesRow)
  #print(lowerGraph)
  header = "Percentage spent by category\n"
  totalDisplay = header + upperGraph + lowerGraph
  #print(totalDisplay)
  return(totalDisplay)
      
      
    
