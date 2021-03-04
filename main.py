from replit import clear
import re

#handle table maker
def table_maker(table_number, count, series):
  if series == 's':
    initial = 1
    end = count+1
    step = 1
  if series == 'i':
    initial = count
    end = 0
    step = -1
  for n in range(initial, end, step):
    print(f"{table_number} x {n} = {table_number*n}")

ending = False
while not ending:
  clear()
  #handle table and count
  series1 = False
  while not series1:
    table_number = input("Enter the number that table you want to print: ")
    table_number_list = re.findall("[1-9]", table_number)
    count = input("Enter the count: ")
    count_list = re.findall("[1-9]", count)    
    if len(table_number_list) > 0 and len(count_list) > 0:
      series1 = True
      table_number = int(''.join(table_number_list))
      count = int(''.join(count_list))
      print(table_number)
      print(count)
    else:
      clear()
      print("You entered the wrong input. Enter non zero number.")



  #handle oriention of table
  series2 = False
  
  while not series2:
    series = input("In which order you want to print table. Type 's' for straight or 'i' for invert: \n").lower()
    series_list = re.findall("i|s", series)  
    if len(series_list) > 0:
      series = ''.join(series_list)
      series2 = True
      clear()
      table_maker(table_number, count, series)
    elif len(series_list) == 0:
      print("You entered the wrong option.")

  #handle table again
  table_again1 = False
  while not table_again1:
    table_again = input("Do you want to print new table. Type 'y' or 'n': ").lower()
    table_again_list = re.findall("y|n", table_again)
    if len(table_again_list) > 0:
      table_again = ''.join(table_again_list)
      if table_again == 'n':
        table_again1 = True
        ending = True
      if table_again == 'y':
        table_again1 = True
    else:
      clear()
      print("You entered the wrong option.")