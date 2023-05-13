using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class Program
{
    static void Main()
    {
        int[] arr = { 1, 2, 5, -1, -3, -4 };

        int count = arr.Count(s => s < 0);
        Console.WriteLine("Количество отрицательных элементов в массиве: " + count);

        int sum = arr.Sum(x => x > 0 ? x : 0);
        Console.WriteLine("Сумма положительных чисел: " + sum);

        int product = arr.Where(x => x % 2 == 0).Aggregate((y, x) => y * x);
        Console.WriteLine("Произведение чётных чисел: " + product);
    }
}
