import datetime as dt
import os

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
                self.cinema[name_cinema].add_seat_configuration(wigth, height)
            else:
                print("Количество рядов и мест должно быть больше 0")
        else:
            print(f"Добавьте сначала кинотеатр {name_cinema} в систему")

    def add_sessions(self, name_movie, name_cinema, num_hall):
        print("Введите дату сеанса в формате: 05-22-2017 12:30")
        date = input()
        print("Введите сколько будет длиться фильм в формате: 1:30")
        duration = input()
        date = dt.datetime.strptime(date, '%Y-%m-%d %H:%M')
        duration = dt.datetime.strptime(duration, '%H:%M')
        self.cinema[name_cinema].get_hall()[num_hall].add_sessions(name_movie, date, duration)

    def search_movie(self, name_movie, number_of_seats):
        self.found_sessions = {}
        for cinema in self.cinema.values():
            for num, hall in cinema.get_hall().items():
                sessions = hall.search_movie(name_movie, number_of_seats)
                for date_ses, ses in sessions.items():
                    self.found_sessions[date_ses] = [cinema.get_name_cinema(), num, ses]
        if len(self.found_sessions) > 0:
            next_ses = min(self.found_sessions.keys())
            self.found_sessions = {next_ses: self.found_sessions[next_ses]}
            print(f"Кинотеатр: {self.found_sessions[next_ses][0]}, Зал: {self.found_sessions[next_ses][1]}, Дата и время сеанса: {next_ses},  длительность фильма: {self.found_sessions[next_ses][2].get_duration()}")
            self.seat_reservation(number_of_seats)
        else:
            print("Данного фильма либо не существует, либо нет достаточного количества свободных мест")

    def seat_reservation(self, number_of_seats):
        print(self.found_sessions.values()[2].get_hall())
        print("Выберете подходящие места по одному за раз")
        for i in range(number_of_seats):
            self.found_sessions.values()[2].choice_of_location(input())

    def get_names_cinema(self):
        return list(self.cinema.keys())

class Cinema:
    def __init__(self, name_cinema):
        self.name_cinema = name_cinema
        self.hall = {}

    def add_hall(self, wigth, height):
        self.hall[len(self.hall) + 1] = Hall()
        self.hall[-1].add_seat_configuration(wigth, height)

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
        self.sessions[date] = Movie(duration, name_movie)
        self.sessions[date].set_hall(self.seat_configuration)
        self.sessions[date].set_free_places(self.number_of_seats)

    def search_movie(self, name, number_of_seats):
        sessions = {}
        for date_ses, ses in self.sessions.items():
            if ses.get_name_movie() == name and ses.get_hall().get_free_places(number_of_seats):
                sessions[date_ses] = ses.get_duration()
                #print(f"Дата и время сеанса: {date_seas},  длительность фильма: {seas.get_duration()}")
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

    def choice_of_location(self, location):
        row, col = [int(i) - 1 for i in location.split("-")]
        self.hall[row, col] = "_"

    def get_duration(self):
        return self.duration

    def get_name_movie(self):
        return self.name_movie

    def get_hall(self):
        return self.hall

    def get_date(self):
        return self.date

    def get_free_places(self, number_of_seats):
        try:
            for i in range(len(self.hall)):
                for j in range(len(i) - number_of_seats):
                    if "_" not in self.hall[i][j : j + number_of_seats]:
                        return True
            return False
        except Exception:
            return False

    def set_hall(self, hall):
        self.hall = hall

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
            print("Введите название фильма и общее количество людей которые пойдут на фильм")
            inp = input().split(" ")
            system.search_movie(inp[0], int(inp[1]))
        elif n == "5":
            break

main()
