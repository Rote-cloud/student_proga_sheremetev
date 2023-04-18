import datetime as dt
import os
import copy

class System:
    def __init__(self):
        self.cinema = {}
        self.found_sessions = {}
        self.sessions = {}

    def add_cinema(self, name_cinema):
        if name_cinema not in self.cinema:
            self.cinema[name_cinema] = Cinema(name_cinema)
        else:
            print(f"Кинотеатр {name_cinema} уже есть в системе")

    def add_hall(self, name_cinema, height, wigth):
        if name_cinema in self.cinema:
            if height > 0 and wigth > 0:
                self.cinema[name_cinema].add_hall(wigth, height)
            else:
                print("Количество рядов и мест должно быть больше 0")
        else:
            print(f"Добавьте сначала кинотеатр {name_cinema} в систему")

    def add_sessions(self, name_movie, name_cinema, num_hall):
        print("Введите дату сеанса в формате: 22-05-2017 12:30")
        date = input()
        print("Введите сколько будет длиться фильм в формате: 1:30")
        duration = [int(i) for i in input().split(":")]
        date = dt.datetime.strptime(date, '%d-%m-%Y %H:%M')
        duration = dt.time(hour=duration[0], minute=duration[1])
        self.cinema[name_cinema].get_hall()[num_hall].add_sessions(name_movie, date, duration)

    def search_movie(self, name_movie):
        self.found_sessions = {}
        for cinema in self.cinema.values():
            for num, hall in cinema.get_hall().items():
                sessions = hall.search_movie(name_movie)
                for date_ses, ses in sessions.items():
                    self.found_sessions[date_ses] = [cinema.get_name_cinema(), num, ses]
        if len(self.found_sessions) > 0:
            next_ses = min(self.found_sessions.keys())
            self.found_sessions = {next_ses: self.found_sessions[next_ses]}
            print(f"Кинотеатр: {self.found_sessions[next_ses][0]}, Зал: {self.found_sessions[next_ses][1]}, Дата и время сеанса: {next_ses},  длительность фильма: {self.found_sessions[next_ses][2].get_duration()}")
            self.seat_reservation()
        else:
            print("Данного фильма либо не существует, либо нет достаточного количества свободных мест")

    def seat_reservation(self):
        ses_value = list(self.found_sessions.values())[0][2]
        print(ses_value.get_hall(), "\n_ - это занятые места")
        print("Выберете подходящие место")
        ses_value.choice_of_location(input())

    def get_names_cinema(self):
        return list(self.cinema.keys())


class Cinema:
    def __init__(self, name_cinema):
        self.name_cinema = name_cinema
        self.hall = {}

    def add_hall(self, wigth, height):
        len_hall = len(self.hall) + 1
        self.hall[len_hall] = Hall()
        self.hall[len_hall].add_seat_configuration(wigth, height)

    def get_hall(self):
        return self.hall

    def get_name_cinema(self):
        return self.name_cinema


class Hall:
    def __init__(self):
        self.seat_configuration = []
        self.sessions = {}
        self.number_of_seats = 0

    def add_seat_configuration(self, width, height):
        self.number_of_seats = width * height
        for i in range(height):
            self.seat_configuration.append([])
            for j in range(width):
                self.seat_configuration[i].append(f"{i + 1}-{j + 1}")

    def add_sessions(self, name_movie, date, duration):
        self.sessions[date] = Movie(date, duration, name_movie)
        self.sessions[date].set_hall(self.seat_configuration)
        self.sessions[date].set_free_places(self.number_of_seats)

    def search_movie(self, name):
        sessions = {}
        for date_ses, ses in self.sessions.items():
            if ses.get_name_movie() == name and ses.get_free_places():
                sessions[date_ses] = ses
        return sessions

    def get_sessions(self):
        return self.sessions

    def get_seat_configuration(self):
        return self.seat_configuration

class Movie:
    def __init__(self, date, duration, name_movie):
        self.date = date
        self.duration = duration
        self.name_movie = name_movie
        self.hall = []
        self.free_places = 0

    def choice_of_location(self, location):
        row, col = [int(i) - 1 for i in location.split("-")]
        self.hall[row][col] = "_"
        self.free_places -= 1

    def get_duration(self):
        return self.duration

    def get_name_movie(self):
        return self.name_movie

    def get_hall(self):
        return self.hall

    def get_date(self):
        return self.date

    def get_free_places(self):
        if self.free_places > 0:
            return True
        return False

    def set_hall(self, hall):
        self.hall = copy.deepcopy(hall)

    def set_free_places(self, free_places):
        self.free_places = free_places

def clear():
    os.system('cls')

def main():
    system = System()
    while True:
        clear()
        print("1. Добавить кинотеатр \n2. Добавить зал в кинотеатре "
              "\n3. Создать сеанс фильма \n4. Поиск ближайшего сеанса фильма \n5. Выход из системы")
        n = input()
        if n == "1":
            clear()
            print("Введите имя кинотеатра:")
            name_cinema = input()
            system.add_cinema(name_cinema)
        elif n == "2":
            clear()
            print(f"Все кинотеатры доступные системе: {system.get_names_cinema()}")
            print("Введите имя кинотеатра с количеством рядов и мест в каждом ряде в 1 строчку")
            inp = input().split(" ")
            system.add_hall(inp[0], int(inp[1]), int(inp[2]))
        elif n == "3":
            clear()
            print("Введите название фильма, имя кинотеатра в котором будет проходить кино и номер зала")
            inp = input().split(" ")
            system.add_sessions(inp[0], inp[1], int(inp[2]))
        elif n == "4":
            clear()
            print("Введите название фильма")
            inp = input()
            system.search_movie(inp)
        elif n == "5":
            break

main()
