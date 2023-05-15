using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class Program
{
    static void Main()
    {
        int[] arr = { 1, 2, 5, -1, -3, -4 };

        int count = 0;

        foreach (int i in from p in arr
                          where p < 0
                          select p)
        {
            count++;
        }
        Console.WriteLine(count);
        count = 0;

        foreach (int i in from p in arr
                          where p > 0
                          select p)
        {
            count += i;
        }
        Console.WriteLine(count);
        count = 1;

        foreach (int i in from p in arr
                          where p % 2 == 0
                          select p)
        {
            count *= i;
        }
        Console.WriteLine(count);
    }
}

