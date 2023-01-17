#import csv dependency
import csv

#store the file path into csvpath
csvpath = "Resources/budget_data.csv"

#open the file to read its information
with open(csvpath) as csvfile:
    # this generates information and temperoraily stores them in csvreader
    csvreader = csv.reader(csvfile,delimiter=',')

    # skips the header row
    csv_header = next(csvreader)

    # iterates through the generated rows and stores them permanently so they can be iterated through more than once
    csvreader = [row for row in csvreader]

    # isolates the first column in the file into a list
    months = [row[0] for row in csvreader]

    # isolates the second column in the file into a list 
    profits_and_losses = [int(row[1]) for row in csvreader]

    # calculates the sum of all the values in profits_and_losses
    total = sum(profits_and_losses)

    # declares an empty list
    monthly_change = []

    # iterates through profits_and_losses to create the monthly change list
    # If one is not subtracted from the length of months then it will throw an "out of bounds" error
    for index in range(len(months)-1):

        # appends the difference of the profits from a certain month and the previous month
        monthly_change.append(profits_and_losses[index+1]-profits_and_losses[index])

    # calculates the average of all the monthly changes
    average_change = sum(monthly_change)/len(monthly_change)

    # calculates the maximum increase in monthly change
    greatest_increase = max(monthly_change)

    # calculates the maximum decrease in monthly change
    greatest_decrease = min(monthly_change)

    # calculates the index of the greatest increase and decrease
    # 1 is added to the end because the length of monthly change is 1 less than that of the length of the months
    greatest_increase_index = monthly_change.index(greatest_increase)+1
    greatest_decrease_index = monthly_change.index(greatest_decrease)+1

    #print the final results
    print("Financial Analysis")
    print("------------------------------")    
    print(f"Total Months: {len(months)}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round(average_change,2)}")
    print(f"Greatest Increase in Profits: {months[greatest_increase_index]} ({greatest_increase})")
    print(f"Greatest Decrease in Profits: {months[greatest_decrease_index]} ({greatest_decrease})")

# declare the path of the file to write to
output = "analysis/budget_data_analysis.txt"

# open the file as writable
with open(output,"w") as fileoutput:

    # write statements
    fileoutput.write("Financial Analysis\n")
    fileoutput.write("------------------------------\n")    
    fileoutput.write(f"Total Months: {len(months)}\n")
    fileoutput.write(f"Total: ${total}")
    fileoutput.write(f"Average Change: ${round(average_change,2)}\n")
    fileoutput.write(f"Greatest Increase in Profits: {months[greatest_increase_index]} ({greatest_increase})\n")
    fileoutput.write(f"Greatest Decrease in Profits: {months[greatest_decrease_index]} ({greatest_decrease})\n")

