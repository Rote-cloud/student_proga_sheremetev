using System;
using System.Collections;
using System.Collections.Generic;

class Teacher {
    private string FIO;
    private List<String> stud_dol = new List<String>();
    private Dictionary<string, List<string>> items = new Dictionary<string, List<string>>();
    public Teacher(string FIO) {
        this.FIO = FIO;
    }
    public void Items() {
        Console.WriteLine("Какие предметы ведёт преподаватель(через пробел)?");
        while (true) {
            string item = Console.ReadLine();
            if (item.Equals("")) {
                break;
            }  else {
                foreach (string i in item.Split(" ")) {
                    Console.WriteLine("Введите группы по предмету " + i +  "(через пробел)");
                    List<string> gr = new List<string>();
                    gr.AddRange(Console.ReadLine().Split(" "));
                    items.Add(i, gr);
                }
            }
        }
    }
    public void Stud_dol(String stud) {
        this.stud_dol.Add(stud);
    }
    public String getFIO() {
        return this.FIO;
    }
    public List<String> getDolg() {
        return this.stud_dol;
    }
    public Dictionary<string, List<string>> getItems() {
        return this.items;
    }

}

class Student {
    private string FIO, group;
    private Dictionary<string, string> debts;
    public Student(string FIO, string group) {
        this.FIO = FIO;
        this.group = group;
    }
    public void Debts(String nameTea, String deb) {
        this.debts.Add(nameTea, deb); //предметы долгов
    }
    public String getFIO() {
        return this.FIO;
    }
    public Dictionary<String, String> getDebts() {
        return this.debts;
    }
}

class Order {
    private String orderNumber, group, FIO;
    
    public Order(string FIO, string orderNumber, string group) {
        this.orderNumber = orderNumber;
        this.group = group;
        this.FIO = FIO;
    }
    public String getOrder() {
        return this.orderNumber;
    }
    public String getGroup() {
        return this.group;
    }
}

public class Program
    {
    static void Main() {
        List<Student> array_stud = new List<Student>();
        List<Teacher> array_tea = new List<Teacher>();
        List<String> array_fio = new List<string>();
        List<Order> array_order = new List<Order>();
        while(true) {
            Console.Clear();
            Console.WriteLine("1. Добавление студента");
            Console.WriteLine("2. Добавление преподователя");
            Console.WriteLine("3. Долги студента и какой преподователь их принимает");
            Console.WriteLine("4. Студенты должнеки у преподователя");
            Console.WriteLine("5. Добавление приказа");
            Console.WriteLine("6. Вывести приказы для нужной группы");
            Console.WriteLine("7. Выход");

            int n = Convert.ToInt32(Console.ReadLine());
            if (n == 1) {
                Console.Clear();
                Console.WriteLine("Если захотите выйти нажмите q");
                Console.WriteLine("Введите фио, группа");
                while (true) {
                    String str = Console.ReadLine();
                    if (str.Equals("q") || str.Equals("Q")) {
                        break;
                    } else {
                        String[] stud_info = str.Split(" ");
                        string fio = stud_info[0] + " " + stud_info[1] + " " + stud_info[2];
                        Student stud = new Student(fio, stud_info[3]);
                        array_stud.Add(stud);
                        Console.WriteLine("Есть ли долги у студента?(Да или Нет)");
                        str = Console.ReadLine();
                        if (str.Equals("Да") || str.Equals("да")) {
                            Console.WriteLine("Введите сколько долгов");
                            int num = Convert.ToInt32(Console.ReadLine());
                            Console.WriteLine("Введите предметы по которым долги и преподователь, который из принимает");
                            for (int i = 0; i < num; i++) {
                                String[] dolgi = Console.ReadLine().Split(" ");
                                stud.Debts(dolgi[0], dolgi[1]);
                                if (array_fio.Contains(dolgi[0])) {
                                    foreach (Teacher tea in array_tea) {
                                        if (tea.getFIO().Equals(dolgi[0])) {
                                            tea.Stud_dol(fio);
                                            break;
                                        }
                                    }
                                } else {
                                    array_tea.Add(new Teacher(dolgi[0]));
                                }
                            }
                            break;
                        }
                    }
                }
            }
            
            if (n == 2) {
                Console.Clear();
                Console.WriteLine("Если захотите выйти нажмите q");
                Console.WriteLine("Введите фио");
                while (true) {
                    String str = Console.ReadLine();
                    if (str.Equals("q") || str.Equals("Q")) {
                        break;
                    } else {
                        Teacher tea = new Teacher(str);
                        array_tea.Add(tea);
                        array_fio.Add(str);
                        tea.Items();
                    }
                }
            }

            if (n == 3) {
                foreach(Student stud in array_stud) {
                    Console.WriteLine(stud.getFIO());
                    Dictionary<String, String> studDebts = stud.getDebts();
                    if (studDebts.Count > 0) {
                        foreach(var i in studDebts) {
                            Console.WriteLine(i.Key + " " + i.Value);
                        }
                    }

                }
            }
            
            if (n == 4) {
                foreach(Teacher tea in array_tea) {
                    Console.WriteLine(tea.getFIO());
                    List<String> studDebts = tea.getDolg();
                    if (studDebts.Count > 0) {
                        foreach(String i in studDebts) {
                            Console.WriteLine(i);
                        }
                    }
                }
            }
            
            if (n == 5) {
                Console.WriteLine("Введите ФИО, номер приказа и группу");
                String[] order = Console.ReadLine().Split(" ");
                array_order.Add(new Order(order[0], order[1], order[2]));
            }
            
            if (n == 6) {
                Console.WriteLine("Введите приказы студентов, преподавателей, вспомогательного персонала или всех");
                String str = Console.ReadLine();
                foreach(Order order in array_order) {
                    if (str.Equals(order.getGroup())) {
                        Console.WriteLine(order.getOrder());
                    }
                }
            }
            
            if (n == 7) {
                break;
            }
        }
        }
}
