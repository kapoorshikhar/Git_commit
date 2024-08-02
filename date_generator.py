from datetime import datetime, timedelta

count = 0
def list_dates(start_date_str):
    # Parse the input start date
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    # Get today's date
    today = datetime.today()
    # Create a list to store the dates
    date_list = []
    
    # Loop through the range of dates from start_date to today

    while start_date <= today:
        date_list.append(start_date.strftime("%Y-%m-%d"))
        start_date += timedelta(days=1)
        global count
        count+= 1
  
    return date_list

# Example usage
start_date = input("Enter the start date in the format YYYY-MM-DD: ")
# start_date = "2024-08-01"
def main():
    
    print(list_dates(start_date))
    print(count)
main()




