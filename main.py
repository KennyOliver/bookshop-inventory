stats_file = open("stats.txt", 'r')
values = stats_file.split(',')
books_in_stock = values[0]
books_lended = values[1]

def book_return(quantity):
  books_in_stock += quantity
  books_lended -= quantity
#====================
def book_lend(quantity):
  books_in_stock -= quantity
  books_lended += quantity
#====================
def view_stats():
  print(f"Books in stock:\t{books_in_stock}".format(books_in_stock))
  print(f"Books lended:\t{books_lended}".format(books_lended))
#====================
def menu():
  print("Pick action:\n\t[R] Return\n\t[L] Lend\n\t[S] View Stats")
  option = input("--> ").upper()
  
  while option not in ['R','L','S']:
    option = input("--> ").upper()
  
  if option == 'R':
    quantity = int(input("Enter the quantity of books to be returned\n--> "))
    while quantity.
    book_return(quantity)
  elif option == 'L':
    quantity = int(input("Enter the quantity of books to be lended\n--> "))
    while quantity.isnum() is not True:
      quantity = int(input("Enter the quantity of books to be lended\n--> "))
    book_lend(quantity)
  elif option == 'S':
    view_stats()