products = []
menu = []
mymeals = {
  "sushi" : ["rice", "fish", "wasabi"],
  "salmon soup" :["salmon", "potato", "cream"],
  "pizza" : ["egg", "dough", "cheez"]
}
print("I can create a list of meals. What products do you have?\n\
      Enter all of them one by one. And 'q' for the result")
name = input()
products.append(name)
while name != "q":
  name = input()
  products.append(name)
for meal in mymeals.keys():
    counter = 0
    for product in products:
        for value in mymeals.values():
            if product == value:
                counter += 1
            if counter == 3:
               print(meal)
#for i in menu:
    #try:
#        print("Boun appetito! Cook " + menu)
    #except NameError:
    #    print("Non existing product is defined")