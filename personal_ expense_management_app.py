# ------------------------------------------------------------------------------------------
# Project..: Personal Expense Management Application
# Date.....: December/2025 
# Author...: Dalvolinda
# Language.: Python
# ------------------------------------------------------------------------------------------

from datetime import datetime;
import os, locale;
import pandas as pd;

# # available categories in lowercase
categories = (
    "groceries", 
    "transportation",  
    "entertainment",   
    "health",          
    "education",       
    "maintenance",     
    "fitness",         
    "housing",         
    "travel",          
    "miscellaneous"    
)

expenses = []  # list of expenses

def addNewExpense(): # option 1
    while True:
        try:
            os.system('cls') # clear the screen
            
            # gets current date/time and formats as yyyy-mm-dd
            datenow = datetime.now()
            date = datenow.strftime("%Y-%m-%d")
            
            # requests information from the user
            print ('-' * 28)
            print (f"{'Enter expense details':^28}")
            print ('-' * 28)
            
           # converts decimals with comma to dot and rounds to 2 decimal places
            amount_str = input('\nAmount or <0> to quit...: ')
            amount = float(amount_str.replace(",", "."))
            amount = round(amount, 2)
                                                                 
            if amount == 0:
               return
            
            description = input('Description.............: ')
            
            # converts category letters to lowercase
            category = (input('Category................: ')).lower()
           
            if amount < 0:
               input ('\nInvalid amount! Re-enter the details.')
            elif not description:
               input ('\nDescription not provided! Re-enter the details.')
            elif not category:
               input ('\nCategory not provided! Re-enter the details.')
            elif category in categories:
                
               expense = {
               'date': date, 
               'category': category,
               'amount': amount, 
               'description': description
               }
            
               expenses.append(expense)
               input('\n==> Expense saved! Press any key to continue.')
            else:  
               input(f'\nCategory {category} is invalid! Re-enter the details.')  
                   
        except ValueError:
               input('\nInvalid amount! Re-enter the details.')
                
        continue
                      
def viewCategories(): # option 2                              
    os.system('cls') # clear the screen
                          
    # generates the listing header                     
    print ('')
    print ('-' * 23)
    print (f"{'List of categories':^23}")
    print ("-" * 23)
    
    cat_sort = tuple(sorted(categories)) # sorted categories

    for c in cat_sort:
        # lists the sorted categories                                                 
        print(c)                      
                        
    input (f'\n==> Listing completed! Press any key to return.')  

def showExpensesPeriod(): # option 3
    while True:
        try:
            os.system('cls') # clear the screen
            
            # gets current date/time and formats as yyyy-mm-dd
            datenow = datetime.now()
            current_date = datenow.strftime("%Y-%m-%d")
            
            # requests start and end dates from the user 
            print ('-' * 60)
            print (f"{'Enter the date range (yyyy-mm-dd) to list expenses':^60}")
            print ('-' * 60)
            
            start_date = input('\nStart date or <enter> to exit...: ') 
            if start_date == "":
               return
                                  
            end_date = input('End date........................: ')             
            
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
       
            if start_date > current_date or end_date > current_date :
               input ('\nStart date or end date is later than current date! Enter a valid date.')
            elif start_date > end_date:
               input('\nStart date is later than end date! Enter a valid date.')
            else:                      
               # generates the header and the list of expenses for the requested period                     
               print ('')
               print ('-' * 60)
               print (f"{'Expense list between ' + str(start_date) + ' and ' + str(end_date):^60}")

               print ('-' * 60)               
               print (f"{'Date':<14}{'Category':<17}{'Amount':<12}{'Description'}")
               print ("-" * 60)
                              
               # converts start and end date to integer
               start_date_num = int(start_date.replace("-", ""))
               end_date_num = int(end_date.replace("-", ""))
                  
               found = False
     
               for d in expenses:
                   # gets date from dictionary and converts to integer                    
                   date_dict = d['date']
                   date_dict_num = int(date_dict.replace("-", ""))

                   if start_date_num <= date_dict_num <= end_date_num:                                
                      print(f"{d['date']:<14}{d['category']:<17}{d['amount']:<12.2f}{d['description']}")                      
                      found = True                     
                         
               if found:
                  input (f'\n==> Listing finished! Press any key to return.')
               else:
                  input (f'\n==> No expenses in the specified period! Press any key.')
                   
               return   
                   
        except ValueError:
               input('\nInvalid date! Re-enter the date in the format yyyy-mm-dd.')
                
        continue
     
def totalSpendingCategory(): # option 4
    os.system('cls') # clear the screen
               
    print ('')  # generates the header  
    print ('-' * 41)
    print (f"{'List of total expenses per category':^41}")
    print ("-" * 41) 
    print (f"{'Category':<20}{'Amount':<12}")
    print ("-" * 41) 
    
    # groups by category and sums values
    df = pd.DataFrame(expenses)
    totals = df.groupby("category")["amount"].sum().reset_index()

    # lists total by category
    for _, row in totals.iterrows():
        print(f"{row['category']:<20}{row['amount']:<12.2f}")                     
                        
    input (f'\n==> Listing completed! Press any key to return.')

def generateMonthlyReport(): # option 5
    while True:
        try:   
            os.system('cls') # clear the screen
                          
            # gets current date/time and formats as yyyy-mm-dd
            datenow = datetime.now()
            current_date = datenow.strftime("%Y-%m")
            
            # request year/month of the report
            print ('-' * 58) 
            print (f"{'Enter the period (yyyy-mm) for the expense report':^58}")
            print ('-' * 58)
            
            year_month = input('\nYear/Month or <enter> to exit...: ')                  
            if year_month == "":
               return
                           
            # set local to Brazil and format month in full in Portuguese
            #locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
            #dt = datetime.strptime(year_month, "%Y-%m")
            #month_year_string = dt.strftime("%B de %Y")
            
            # format month in full in English
            dt = datetime.strptime(year_month, "%Y-%m")
            month_year_string = dt.strftime("%B %Y")
       
            if year_month > current_date:
               input ('\nYear/Month is later than the current date! Enter the correct Year/Month.')
            else:                      
               # generates the report header                    
               print ('')
               print ('-' * 58)
               print (f"{'Monthly expense report for ' + str(month_year_string):^58}")

               print ('-' * 58)               
               print (f"{'Date':<14}{'Category':<17}{'Amount':<12}{'Description'}")
               print ("-" * 58)
                                           
               found = False
     
               for d in expenses:
                   # gets date from dictionary                  
                   date_dict = d['date'] 
                                     
                   if date_dict[:7] == year_month:                                 
                      print(f"{d['date']:<14}{d['category']:<17}{d['amount']:<12.2f}{d['description']}")                      
                      found = True                    
                         
               if found:
                  input (f'\n==> Report finished! Press any key to return.')
               else:
                  input (f'\n==> No expenses in the specified period! Press any key.')
                   
               return   
                   
        except ValueError:
               input ('\nInvalid date! Re-enter the date in the format yyyy-mm.')
                
        continue
    
def categoryHighestSpending(): # option 6
    os.system('cls') # clear the screen
                        
    # groups by category and sums values
    df = pd.DataFrame(expenses)
    totals = df.groupby("category")["amount"].sum().reset_index()

    # locate the row with the highest value
    max_expense = totals.loc[totals["amount"].idxmax()]
    
    # generates the header
    print ("-" * 75) 
    print(f"{'The category with the highest expense is ' + max_expense['category'] + ' totaling $ ' + format(max_expense['amount'], '.2f'):^75}")
    print ("-" * 75) 
    print (f"{'Date':<14}{'Category':<17}{'Amount':<12}{'Description'}")
    print ("-" * 75)
    
    for d in expenses:
        # lists expenses of the category with the highest spending                    
        if d['category'] == max_expense['category']:                                
            print(f"{d['date']:<14}{d['category']:<17}{d['amount']:<12.2f}{d['description']}")                                      
                        
    input (f'\n==> Category expenses listed! Press any key to return.')

def exportExpenseReport(): # option 7
    os.system('cls') # clear the screen
       
    df = pd.DataFrame(expenses)   
    # generates a .csv file
    df.to_csv("expenses.csv", index=False, sep=";")
    input (f'\n==> Expenses successfully exported to expenses.csv! Press any key to return.')
            
def main (): # main screen
    while True:
        try:
            os.system('cls') # clear the screen
            
            print ('')
            print ('-' * 39)
            print (f"{'Personal Expense Management Application':^39}")
            print ('-' * 39)
            print('[1] Add a new expense')
            print('[2] View categories')
            print('[3] Show expenses by period')
            print('[4] See total spending by category')
            print('[5] Generate monthly report')
            print('[6] Find category with highest spending')
            print('[7] Export expense report')
            print('[0] Quit')         
            print ('-' * 39)
            
            option = int(input('\nSelect an option: '))
       
            if not expenses:
               if 2 < option < 8: 
                  input (f'\n==> No expenses recorded! Press any key to continue.')
                  continue
                            
            match option:
                case 1:
                    addNewExpense()
                case 2:
                    if not categories:
                       input (f'\n==> No categories available! Press any key to continue.')
                       continue
                    else:
                       viewCategories()
                case 3:
                    showExpensesPeriod()
                case 4:
                    totalSpendingCategory()
                case 5:
                    generateMonthlyReport()
                case 6:
                    categoryHighestSpending()
                case 7:
                    exportExpenseReport()
                case 0:
                    print ('\nFinishing ...\n')
                    break  
                case _:
                    input ('\nInvalid option! Press any key to continue.')
                        
        except ValueError:
            input ('\nInvalid option! Press any key to continue.')
    
main()
