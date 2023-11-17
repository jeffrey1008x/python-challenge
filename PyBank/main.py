from pathlib import Path
import csv

def main():
    csv_path = Path("Resources/budget_data.csv")
    out_path = Path("analysis/output.txt")

    # Header was not need for my calculations but it was asked to be stored from the 'Requirements' part.
    with open(csv_path) as file:
        headers = list(list(csv.DictReader(file, delimiter=','))[0].keys())

    with open(csv_path) as csv_file:

        # Read the csv file with each row as a dictionary.
        csv_reader = csv.DictReader(csv_file, delimiter=',')

        max_change = 0
        max_date = None
        min_change = 0
        min_date = None
        months = 0
        total = 0
        previous = 0
        changes = []

        # Loop through each row.
        for row in csv_reader:
            
            # Adds up the total profit/loss.
            total += int(row['Profit/Losses'])
            
            # Find the max and min change in profit/loss.
            if months > 0:
                change = int(row['Profit/Losses']) - previous
                changes.append(change)
                if change > max_change:
                    max_change = change
                    max_date = row['Date']
                if change < min_change:
                    min_change = change
                    min_date = row['Date']
                previous = int(row['Profit/Losses'])
            else:
                previous = int(row['Profit/Losses'])

            months += 1

        # Calculates the total changes in profit/loss.
        total_changes = 0
        for c in changes:
            total_changes += c

        # Prepare the required output strings.
        s1 = 'Financial Analysis\n'
        s2 = '----------------------------\n'
        s3 = f'Total Months: {months}\n'
        s4 = f'Total: {total}\n'
        s5 = f'Average Change: ${int(total_changes/len(changes))}\n'
        s6 = f'Greatest Increase in Profits: {max_date} (${max_change})\n'
        s7 = f'Greatest Decrease in Profits: {min_date} (${min_change})\n'

        # Print the analysis.
        print(s1)
        print(s2)
        print(s3)
        print(s4)
        print(s5)
        print(s6)
        print(s7)

        # Export the result into output.txt in the analysis/ folder.
        f = open(out_path, "w")
        f.write(s1)
        f.write(s2)
        f.write(s3)
        f.write(s4)
        f.write(s5)
        f.write(s6)
        f.write(s7)
        f.close()


if __name__ == "__main__":
    main()