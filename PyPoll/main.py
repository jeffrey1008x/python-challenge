from pathlib import Path
import csv

def main():
    csv_path = Path("Resources/election_data.csv")
    out_path = Path("analysis/output.txt")

    votes_summary = {}

    # Header was not need for my calculations but it was asked to be stored from the 'Requirements' part.
    with open(csv_path) as file:
        headers = list(list(csv.DictReader(file, delimiter=','))[0].keys())

    with open(csv_path) as csv_file:

        # Read the csv file with each row as a dictionary.
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        
        max_count = 0
        total = 0
        winner = None

        # Loop through each row and count the votes for each candidate and store the votes in a dictionary.
        for row in csv_reader:
            total += 1
            votes_summary[row['Candidate']] = votes_summary.get(row['Candidate'], 0) + 1

        # Prepare the required output strings.
        s1 = 'Election Results\n'
        s2 = '-------------------------\n'
        s3 = f'Total Votes: {total}\n'
        s4 = '-------------------------\n'
        s_summary = ''
        for k in votes_summary.keys():
            s_summary += f'{k}: {round(votes_summary[k]/total * 100, 3)}% ({votes_summary[k]})\n'
            if votes_summary[k] > max_count:
                max_count = votes_summary[k]
                winner = k
        s5 = '-------------------------\n'
        s6 = f'Winner: {winner}\n'
        s7 = '-------------------------\n'

        # Print the analysis.
        print(s1)
        print(s2)
        print(s3)
        print(s4)
        print(s_summary)
        print(s5)
        print(s6)
        print(s7)

        # Export the result into output.txt in the analysis/ folder.
        f = open(out_path, "w")
        f.write(s1)
        f.write(s2)
        f.write(s3)
        f.write(s4)
        f.write(s_summary)
        f.write(s5)
        f.write(s6)
        f.write(s7)
        f.close()
        
if __name__ == "__main__":
    main()