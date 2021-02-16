def book_return(books_in_stock,books_lended,quantity):
  new_stock_value = books_in_stock + quantity
  new_lend_value = books_lended - quantity
  vals = [new_stock_value, new_lend_value]
  return vals
#====================
def book_lend(books_in_stock,books_lended,quantity):
  new_stock_value = books_in_stock - quantity
  new_lend_value = books_lended + quantity
  vals = [new_stock_value, new_lend_value]
  return vals
#====================
def view_stats(books_in_stock,books_lended):
  print(f"Books in stock:\t{books_in_stock}".format(books_in_stock))
  print(f"Books lended:\t{books_lended}".format(books_lended))
#====================
def menu(books_in_stock,books_lended):
  print("Pick action:\n\t[R] Return\n\t[L] Lend\n\t[S] View Stats")
  option = input("--> ").upper()
  
  while option not in ['R','L','S']:
    option = input("--> ").upper()
  
  if option == 'R':
    quantity = int(input("Enter the quantity of books to be returned\n--> "))
    while type(quantity) != int:
      quantity = int(input("Enter the quantity of books to be returned\n--> "))
    new_stocking = book_return(books_in_stock,books_lended,quantity)[0]
    new_lending = book_return(books_in_stock,books_lended,quantity)[1]
    write_data(new_stocking,new_lending)

  elif option == 'L':
    quantity = int(input("Enter the quantity of books to be lended\n--> "))
    while type(quantity) != int:
      quantity = int(input("Enter the quantity of books to be lended\n--> "))
    new_stocking = book_lend(books_in_stock,books_lended,quantity)[0]
    new_lending = book_lend(books_in_stock,books_lended,quantity)[1]
    write_data(new_stocking,new_lending)

  elif option == 'S':
    view_stats(books_in_stock,books_lended)
#====================
def write_data(new_stocking,new_lending):
  stats_file = open("stats.txt",'w')
  stats_file.write(str(new_stocking) + ',' + str(new_lending))
  stats_file.close()



# main program
stats_file = open("stats.txt",'r')
for record in stats_file:
  values = record.split(',')
  books_in_stock = int(values[0])
  books_lended = int(values[1])

menu(books_in_stock,books_lended)
stats_file.close()