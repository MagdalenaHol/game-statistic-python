from http.client import GATEWAY_TIMEOUT
import re
from unittest import result


def count_games(file_name):
    num_lines = open("game_stat.txt").read().count("\n")
    num_lines.close()
    return num_lines


# print(count_games("game_stat.txt"))


def decide(file_name, year):
    with open("game_stat.txt", "r") as f:
        data_file = f.readlines()
        for line in data_file:
            if str(year) in line:
                return True
        return False


# print(decide("game_stat.txt", 2004))


def get_latest(file_name):
    line = " "
    game_name = " "
    each_line = []
    last_game = 0
    with open("game_stat.txt", "r") as f:
        while len(line):
            line = f.readline()
            if len(line) > 0:
                each_line = line.split("\t")
                # print(each_line)
            if int(each_line[2]) > last_game:
                last_game = int(each_line[2])
                game_name = each_line[0]

        return game_name

# print(get_latest("game_stat.txt"))


def count_by_genre(file_name, genre):
    each_line = []
    genre_list = []
    count_genere = 0 
    data_file = ""

    with open("game_stat.txt", "r") as f:
        data_file = f.read()
        each_line = data_file.split("\n")
        for item in range(0, len(each_line)-1):
            genre_list = each_line[item].split("\t")
            # print(each_line, item)
            if genre_list[3] == genre:
                count_genere += 1
        return count_genere


# print(count_by_genre("game_stat.txt","First-person shooter"))
    


def get_line_number_by_title(file_name, title):
    # line_num = 0
    each_line = []
    get_first_item = []

    with open("game_stat.txt","r") as f:
        data_file = f.read()
        each_line = data_file.split("\n")
        # print(each_line)
        for i in range(0, len(each_line)-1):
            get_first_item = each_line[i].split("\t")
            if get_first_item[0] == title:
                return i + 1
        raise ValueError('There is no game like this.')


# print(get_line_number_by_title("game_stat.txt", "StarCraft"))


def sort_abc(file_name):
    each_line = []
    title_by_alphabet = []

    with open("game_stat.txt","r") as f:
        data_file = f.read()
        each_line = data_file.split("\n")
        for i in range(len(each_line)-1):
            title_by_alphabet.append(each_line[i].split("\t")[0])

        print(title_by_alphabet.sort())
        return title_by_alphabet
        

# print(sort_abc("game_stat.txt"))


def get_genres(file_name):
    each_line = []
    each_genre = []

    with open("game_stat.txt","r") as f:
        data_file = f.read()
        each_line = data_file.split("\n")
        for i in range(len(each_line)-1):
            each_genre.append(each_line[i].split("\t")[3])
        each_genre =  list(set(each_genre))
        each_genre.sort()
        return each_genre
        
    
# print(get_genres("game_stat.txt"))


def when_was_top_sold_fps(file_name):
    each_line = []
    game = []
    sold = 0

    with open("game_stat.txt","r") as f:
        data_file = f.read()
        each_line = data_file.split("\n")
    for i in range(len(each_line)-1):
        game = each_line[i].split("\t")
        print(game)
        if game[3] == "First-person shooter" and float(game[1]) > sold:
            sold = float(game[1])
            year = game[2]
    if sold:
        return int(year)
    else:
        raise ValueError


print(when_was_top_sold_fps("game_stat.txt"))