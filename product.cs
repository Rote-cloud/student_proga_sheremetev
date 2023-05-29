using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.ConstrainedExecution;

class Provider
{
    public int Id { get; set; }
    public string Name { get; set; }
}

class Product
{
    public int Id { get; set; }
    public string Name { get; set; }
}

class SupplyGoods
{
    public Product product { get; set; }
    public string date { get; set; }
    public Provider provider { get; set; }
    public int count { get; set; }
}
public class Program
{
    static void Main()
    {
        List<Product> products = new List<Product>{
                new Product{Id = 1, Name = "car"},
                new Product{Id = 2, Name = "cloth" },
                new Product{Id = 3, Name = "boots" }
            };

        List<Provider> providers = new List<Provider> { 
            new Provider{ Id = 1, Name = "Lada"},
            new Provider{ Id = 2, Name = "Tayota"},
            new Provider{ Id = 3, Name = "H&M"}, 
            new Provider{ Id = 4, Name = "Gucci"},
            new Provider{ Id = 5, Name = "Adidas"},
            new Provider{ Id = 6, Name = "New Balance"}
        };

        List<SupplyGoods> supplies = new List<SupplyGoods>
        {
                new SupplyGoods { product = products[0], date = "20.05.2023", provider = providers[0], count=1000000},
                new SupplyGoods { product = products[0], date = "25.01.2023", provider = providers[1], count=1},
                new SupplyGoods { product = products[1], date = "24.01.2020", provider = providers[2], count=547},
                new SupplyGoods { product = products[1], date = "23.07.2019", provider = providers[3], count=2},
                new SupplyGoods { product = products[2], date = "25.01.2000", provider = providers[4], count=1436},
                new SupplyGoods { product = products[2], date = "20.05.2023", provider = providers[5], count=43543},

            };

        foreach (SupplyGoods i in from p in supplies
                          where p.date == "20.05.2023"
                                  select p)
        {
            Console.Write(i.provider.Name + " " + i.count + "   ");
        }
        Console.WriteLine();

        foreach (SupplyGoods i in from p in supplies
                                  where p.product == products[2]
                                  select p)
        {
            Console.Write(i.provider.Name + " ");
        }
        Console.WriteLine();

        foreach (SupplyGoods i in from p in supplies
                                  where p.provider == providers[1]
                                  select p)
        {
            Console.Write(i.provider.Name + " " + i.product.Name + "   ");
        }
        Console.ReadLine();
    }
}
