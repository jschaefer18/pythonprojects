import csv
import pytest

file = 'nbastats.csv'

def main():
    print('Welcome to NBA Stats Analysis Software!')
    print('''Controls:
    quit: exits the program
    oneplayer: gets the stats of a singular player based on the inputed name
    ranked: return top 100 of inputed stat
    avg: gets the average of a statline in the nba''')
    while True:
        action = input('What would you like to do? ')
        if action.lower() == 'oneplayer':
            player_name = input('What is your player\'s name? ')
            get_player_stats(file, player_name)
        elif action.lower() == 'quit':
            quit()
        elif action.lower() == 'ranked':
            hi = input('Would you like to know the references? (y/n) ').lower()
            if hi == 'y':
                print_references()
            stat = input('What stat would you like to rank by? ')
            ranked_stats(file,stat)
        elif action == 'avg':
            hi = input('Would you like to know the references? (y/n) ').lower()
            if hi == 'y':
                print_references()
            stat = input('What stat would you like the average of? ')
            print(avg_stat(file,stat))
        else:
            print("Invalid input. Please try again.")


def read_compound_list(filename):
    compound_list = []
    with open(filename, "rt", encoding='latin-1') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        next(reader)
        for row in reader:
            compound_list.append(row)
    return compound_list


def get_player_stats(filename, player_name):
    player_info = None
    compound_list = read_compound_list(filename)
    for element in compound_list:
        if element['Player'].lower() == player_name.lower():
            player_info = element
            break
    
    if not player_info:
        print(f"No stats found for player '{player_name}'.")
        return
    
    player = player_info['Player']
    pos = player_info['Pos']
    age = player_info['Age']
    tm = player_info['Tm']
    g = player_info['G']
    gs = player_info['GS']
    mp = player_info['MP']
    fg = player_info['FG']
    fga = player_info['FGA']
    fg_percent = player_info['FG%']
    three_p = player_info['3P']
    three_pa = player_info['3PA']
    three_percent = player_info['3P%']
    two_p = player_info['2P']
    two_pa = player_info['2PA']
    two_percent = player_info['2P%']
    efg_percent = player_info['eFG%']
    ft = player_info['FT']
    fta = player_info['FTA']
    ft_percent = player_info['FT%']
    orb = player_info['ORB']
    drb = player_info['DRB']
    trb = player_info['TRB']
    ast = player_info['AST']
    stl = player_info['STL']
    blk = player_info['BLK']
    tov = player_info['TOV']
    pf = player_info['PF']
    pts = player_info['PTS']
    
    print()
    print(f'Name: {player}')
    print(f'Position: {pos}')
    print(f'Age: {age}')
    print(f'Team: {tm}')
    print(f'Points Per Game: {pts}')
    print(f'Assists Per Game: {ast}')
    print(f'Rebounds Per Game: {trb}')
    print(f'Steals Per Game: {stl}')
    print(f'Blocks Per Game: {blk}')
    print()
    ans = input('Would you like to see advanced stats? (y/n) ')
    if ans.lower() == 'y':
        print(f'Games Played: {g}')
        print(f'Games Started: {gs}')
        print(f'Minutes Per Game: {mp}')
        print(f'Field Goals Per Game: {fg}')
        print(f'Field Goal Attempts Per Game: {fga}')
        print(f'Field Goal Percentage: {fg_percent}')
        print(f'3-Point Field Goals Per Game: {three_p}')
        print(f'3-Point Field Goal Attempts Per Game: {three_pa}')
        print(f'3-Point Field Goal Percentage: {three_percent}')
        print(f'2-Point Field Goals Per Game: {two_p}')
        print(f'2-Point Field Goal Attempts Per Game: {two_pa}')
        print(f'2-Point Field Goal Percentage: {two_percent}')
        print(f'Effective Field Goal Percentage: {efg_percent}')
        print(f'Free Throws Per Game: {ft}')
        print(f'Free Throw Attempts Per Game: {fta}')
        print(f'Free Throw Percentage: {ft_percent}')
        print(f'Offensive Rebounds Per Game: {orb}')
        print(f'Defensive Rebounds Per Game: {drb}')
        print(f'Total Rebounds Per Game: {trb}')
        print(f'Turnovers Per Game: {tov}')
        print(f'Personal Fouls Per Game: {pf}')
        print()
    else:
        print('Okay, no problem.')
        print()




def ranked_stats(filename, stat_name):
    compound_list = read_compound_list(filename)
    sorted_players = sorted(compound_list, key=lambda x: float(x[stat_name]), reverse=True)
    top_100_players = sorted_players[:100]
    for i, player in enumerate(top_100_players, start=1):
        print(f"{i}. {player['Player']}: {player[stat_name]} {stat_name}")



def avg_stat(filename, stat_name):
    compound_list = read_compound_list(filename)
    stat_values = []
    result = get_value_type(filename,stat_name)
    if result == 'str':
        print('String is invalid for the average function.')
        return None
    for player in compound_list:
        stat_values.extend([float(num) for num in player[stat_name].split()])
    
    avg = round(sum(stat_values) / len(stat_values), 2)
    return avg




def get_value_type(filename, value):
    compound_list = read_compound_list(filename)
    for element in compound_list:
        try:
            converted_value = int(element[value])
            return "int"
        except ValueError:
            try:
                converted_value = float(element[value])
                return "float"
            except ValueError:
                pass
    return "str"
def print_references():
        print('''References: 
        Rk : Rank
        Player : Player's name
        Pos : Position
        Age : Player's age
        Tm : Team
        G : Games played
        GS : Games started
        MP : Minutes played per game
        FG : Field goals per game
        FGA : Field goal attempts per game
        FG% : Field goal percentage
        3P : 3-point field goals per game
        3PA : 3-point field goal attempts per game
        3P% : 3-point field goal percentage
        2P : 2-point field goals per game
        2PA : 2-point field goal attempts per game
        2P% : 2-point field goal percentage
        eFG% : Effective field goal percentage
        FT : Free throws per game
        FTA : Free throw attempts per game
        FT% : Free throw percentage
        ORB : Offensive rebounds per game
        DRB : Defensive rebounds per game
        TRB : Total rebounds per game
        AST : Assists per game
        STL : Steals per game
        BLK : Blocks per game
        TOV : Turnovers per game
        PF : Personal fouls per game
        PTS : Points per game''')


main()













