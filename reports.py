import re

from unittest import result


def count_games(file_name):
    num_lines = open("game_stat.txt").read().count("\n")
    return num_lines


# print(count_games("game_stat.txt"))


def decide(file_name, year):
    with open("game_stat.txt", "r") as f:
        data_file = f.readlines()
        for line in data_file:
            if str(year) in line:
                return True
        return False


# print(decide("game_stat.txt", 2008))


def get_latest(file_name):
    each_line = []
    counter = 0
    with open("game_stat.txt", "r") as f:
        for line in f:
            each_line = [line.strip().split("")]
            each_line.sort(key=lambda x: x[2])
        if lambda x: x[2] == max(counter):
            # each_line[0][2] == max(counter)
            # print(each_line[0][0])
    
            return each_line[0][0]


# print(get_latest("game_stat.txt"))


def count_by_genre(file_name, genre):
    genre_list = []
    with open("game_stat.txt", "r") as f:
        data_file = f.readlines()
        for line in data_file:
            if str(genre_list) in line:
                genre_list.append(line[0])
                print(genre_list)
       
        return len(set(genre_list))


print(count_by_genre("game_stat.txt",""))
    


def get_line_number_by_title(file_name, title):

    with open("game_stat.txt","r") as f:
    counter = 0
    for i in f:
        counter += 1
        if title in i:
            return counter
    raise ValueError('There is no game like this.')


def sort_abc(file_name):
    pass


def get_genres(file_name):
    pass


def when_was_top_sold_fps(file_name):
    pass
