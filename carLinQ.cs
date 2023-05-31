using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

class Car
{
    public int Id { get; set; }
}

class Driver
{
    public string DriverName { get; set; }
    public string DriverSurename { get; set; }
    public int CarNumber { get; set; }
}

public class Program
{
    static void Main()
    {
        List<Car> cars = new List<Car>
            {
                new Car{Id = 1 },
                new Car{Id = 2 },
                new Car{Id = 3 },
            };
        List<Driver> drivers = new List<Driver>
            {
                new Driver{ DriverName = "Vyacheslav", DriverSurename = "Izengardovich", CarNumber = 3},
                new Driver{ DriverName = "Ivan", DriverSurename = "Ivanov", CarNumber = 1},
                new Driver{ DriverName = "San", DriverSurename = "Sanich", CarNumber = 2},
                new Driver{ DriverName = "Michael", DriverSurename = "Jackeson", CarNumber = 1},
                new Driver{ DriverName = "Janna", DriverSurename = "D'Arck", CarNumber = 3},
            };

        foreach (Driver i in from p in drivers
                          where p.CarNumber == 1
                          select p)
        {
            Console.Write(i.DriverSurename + " ");
        }
        Console.WriteLine();

        foreach (Driver i in from p in drivers
                          where p.DriverSurename == "Izengardovich"
                          select p)
        {
            Console.Write(i.CarNumber + " ");
        }
        Console.WriteLine();

        foreach (Driver i in from p in drivers
                          where p.DriverSurename.StartsWith("I")
                          select p)
        {
            Console.WriteLine(i.DriverName + " " + i.DriverSurename);
        }
        Console.ReadLine();

    }
}
