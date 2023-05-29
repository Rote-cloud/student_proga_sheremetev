using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

class Car
{
    public int Id { get; set; } 
    public string DriverName { get; set; }
    public string DriverSurename { get; set; }
}

public class Program
{
    static void Main()
    {
        List<Car> drivers = new List<Car>
            {
                new Car{ DriverName = "Vyacheslav", DriverSurename = "Izengardovich", Id = 3},
                new Car{ DriverName = "Ivan", DriverSurename = "Ivanov", Id = 1},
                new Car{ DriverName = "San", DriverSurename = "Sanich", Id = 2},
                new Car{ DriverName = "Michael", DriverSurename = "Jackeson", Id = 1},
                new Car{ DriverName = "Janna", DriverSurename = "D'Arck", Id = 3}
            };

        foreach (Car i in from p in drivers
                          where p.Id == 1
                          select p)
        {
            Console.Write(i.DriverSurename + " ");
        }
        Console.WriteLine();

        foreach (Car i in from p in drivers
                          where p.DriverSurename == "Izengardovich"
                          select p)
        {
            Console.Write(i.Id + " ");
        }
        Console.WriteLine();

        foreach (Car i in from p in drivers
                          where p.DriverSurename.StartsWith("I")
                          select p)
        {
            Console.WriteLine(i.DriverName + " " + i.DriverSurename);
        }
        Console.ReadLine();
        
    }
}
