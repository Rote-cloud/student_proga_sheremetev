using System;
using System.Collections;
using System.Collections.Generic;
public class Program
    {
        
    static void Main() {
        List<Student> array = new List<Student>();
        while(true) {
            Console.Clear();
            Console.WriteLine("1. Добавление студента");
            Console.WriteLine("2. Студенты которые учатся в заданной группе");
            Console.WriteLine("3. Студенты должнеки");
            Console.WriteLine("4. Студенты отличники");
            Console.WriteLine("5. Студенты моложе 20 лет");
            Console.WriteLine("6. Выход");
            
            int n = Convert.ToInt32(Console.ReadLine());
            if (n == 1) {
                Console.Clear();
                Console.WriteLine("Если захотите выйти нажмите q");
                Console.WriteLine("Введите фио, дату рождения(числа указывать через пробелы), группа, имя предмета и оценка(если есть)");
                while (true) {
                    String str = Console.ReadLine();
                    if (str.Equals("q") || str.Equals("Q")) {
                        break;
                    } else {
                        String[] stud = str.Split(" ");
                        if (stud.Length == 8) {
                            Array.Resize(ref stud, 9);
                            stud[8] = "0";
                        }
                        bool t = false;
                        for (int i = 0; i < array.Count; i++) {
                            if (array[i].getName().Equals(stud[0])) {
                                array[i].setArr(stud[7], Convert.ToInt32(stud[8]));
                                t = true; 
                                break;
                            }
                        }
                        if (t == false) {
                            array.Add(new Student(stud[0], stud[1], stud[2], Convert.ToInt32(stud[3]), Convert.ToInt32(stud[4]), Convert.ToInt32(stud[5]), stud[6], stud[7], Convert.ToInt32(stud[8])));
                        }
                    }
                }
            }

            if (n == 2) {
                Console.Clear();
                Console.WriteLine("Введите номер группы");
                String str = Console.ReadLine();
                if (array.Count == 0) {
                    Console.WriteLine("Студенты пропали");
                } else {
                    int num = 0;
                    for (int i = 0; i < array.Count; i++) {
                        if (array[i].getGroup().Equals(str)) {
                            Console.WriteLine(array[i].getFIO());
                            num += 1;
                        }
                    }
                    if (num == 0 ) {
                        Console.WriteLine("Нет студентов из данной группы");
                    }
                }
                Console.WriteLine("Нажмите любую клавишу");
                str = Console.ReadLine();
            }

            if (n == 3) {
                Console.Clear();
                Console.WriteLine("Студенты должнеки");
                int num = 0;
                for (int i = 0; i < array.Count; i++) {
                        if (array[i].getGrape() == 0) {
                            Console.WriteLine(array[i].getFIO());
                            num += 1;
                        }
                }
                if (num == 0 ) {
                        Console.WriteLine("Нет таких студентов");
                }
                
                Console.WriteLine("Нажмите любую клавишу");
                String str = Console.ReadLine();
            }

            if (n == 4) {
                Console.Clear();
                Console.WriteLine("Студенты отличники");
                int num = 0;
                for (int i = 0; i < array.Count; i++) {
                        if (array[i].getGrape() == 5) {
                            Console.WriteLine(array[i].getFIO());
                            num += 1;
                        }
                }
                if (num == 0 ) {
                        Console.WriteLine("Нет таких студентов");
                }
                
                Console.WriteLine("Нажмите любую клавишу");
                String str = Console.ReadLine();
            }

            if (n == 5) {
                Console.Clear();
                Console.WriteLine("Студенты моложе 20 лет");
                int num = 0;
                for (int i = 0; i < array.Count; i++) {
                        if (array[i].getYear() < 20) {
                            Console.WriteLine(array[i].getFIO());
                            num += 1;
                        }
                }
                if (num == 0 ) {
                        Console.WriteLine("Нет таких студентов");
                }
                
                Console.WriteLine("Нажмите любую клавишу");
                String str = Console.ReadLine();
            }

            if (n == 6) {
                break;
            }
        }
        }
}

class Student {
        private String name, nameitem, group, getname;
        private DateTime date;
        private int  grade, year;
        private Dictionary<string, int> item_grade = new Dictionary<string, int>();
        public Student(String surname, String otchestvo, String name, int year, int month, int day, String group, String nameitem, int grade = 0) {
            this.name = surname + " " + otchestvo + " " + name;
            this.date = new DateTime(year, month, day);
            this.group = group;
            this.getname = name;
            this.grade = grade;
            this.year = year;
            item_grade.Add(nameitem, grade);
        }

        public string getName() {
            return getname;
        }
        public string getFIO() {
            return name;
        }
        public string getGroup() {
            return group;
        }
        public int getGrape() {
            return grade;
        }
        public int getYear() {
            return DateTime.Now.Year - year;
        }

        public int setArr(String nameitem, int grade) {
            item_grade.Add(nameitem, grade);
            return 0;
        }
}
