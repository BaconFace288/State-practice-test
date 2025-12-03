def main():
    Teams = {} 
    Years = {} 
    
    current_year = 1903
    
    try:
        with open('WorldSeriesWinners.txt', 'r') as input_file:
            winners = input_file.readlines()
            
            for team in winners:
                team_name = team.strip()
                
                if current_year == 1904:
                    current_year += 1
                if current_year == 2021:
                    current_year += 1
                
                Years[current_year] = team_name
                
                if team_name in Teams:
                    Teams[team_name] += 1
                else:
                    Teams[team_name] = 1
                
                current_year += 1

        search_year = int(input("Enter a year between 1903 and 2021: "))
        
        if search_year == 1904 or search_year == 1994:
            print(f"The World Series was not played in {search_year}.")
            
        elif search_year < 1903 or search_year > 2021:
            print("The year entered is out of the valid range (1903-2021).")
            
        elif search_year in Years:
            winner = Years[search_year]
            total_wins = Teams[winner]
            
            print(f"The team that won the World Series in {search_year} is the {winner}.")
            print(f"They have won the World Series {total_wins} times.")
        else:
            print(f"No data available for {search_year}.")

    except FileNotFoundError:
        print("Error: The file 'WorldSeriesWinners.txt' was not found.")
    except ValueError:
        print("Error: Please enter a valid numeric year.")

if __name__ == "__main__":
    main()