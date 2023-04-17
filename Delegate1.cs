interface IMath
{
    abstract double Add(double value1, double value2);
    abstract double Subtract(double value1, double value2);
    abstract double Multiplication(double value1, double value2);
    abstract double Division(double value1, double value2);
}

class Program: IMath
{
    public delegate double MathDelegate(double value1, double value2);

    public double Add(double value1, double value2)
    {
        return value1 + value2;
    }
    public double Subtract(double value1, double value2)
    {
        return value1 - value2;
    }
    public double Multiplication(double value1, double value2)
    {
        return value1 * value2;
    }
    public double Division(double value1, double value2)
    {
        return value1 / value2;
    }

    public static void Main()
    {
        while (true)
        {
            Console.WriteLine("Введите два числа");
            double num1 = Convert.ToDouble(Console.ReadLine());
            double num2 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("1.Add \n2.Subtract \n3.Multiplication \n4.Division \n5.Break");
            int n = Convert.ToInt32(Console.ReadLine());
            Program prog = new Program();
            if (n == 1)
            {
                MathDelegate mathDelegate = prog.Add;
                var result = mathDelegate(num1, num2);
                Console.WriteLine(result);
            }
            if (n == 2)
            {
                MathDelegate mathDelegate = prog.Subtract;
                var result = mathDelegate(num1, num2);
                Console.WriteLine(result);
            }
            if (n == 3)
            {
                MathDelegate mathDelegate = prog.Multiplication;
                var result = mathDelegate(num1, num2);
                Console.WriteLine(result);
            }
            if (n == 4)
            {
                MathDelegate mathDelegate = prog.Division;
                var result = mathDelegate(num1, num2);
                Console.WriteLine(result);
            }
            if (n == 5)
            {
                break
            }
        }
    }
}
