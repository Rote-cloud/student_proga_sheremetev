class Program
{
    public delegate double MathDelegate(double[] arr);
    MathDelegate max = (double[] arr) => arr.Max();
    MathDelegate min = (double[] arr) => arr.Min();
    MathDelegate sum = (double[] arr) => arr.Sum();
    MathDelegate multi = (double[] arr) => arr[0] * arr[1] * arr[2];
    MathDelegate average = (double[] arr) => arr.Average();
    
    public static void Main()
    {
            Program prog = new Program();
            Console.WriteLine("Введите три числа");
            double num1 = Convert.ToDouble(Console.ReadLine());
            double num2 = Convert.ToDouble(Console.ReadLine());
            double num3 = Convert.ToDouble(Console.ReadLine());
            double[] arr = {num1, num2, num3};
            Console.WriteLine("Min: " + prog.min(arr));
            Console.WriteLine("Max: " + prog.max(arr));
            Console.WriteLine("Sum: " + prog.sum(arr));
            Console.WriteLine("Multi: " + prog.multi(arr));
            Console.WriteLine("Average: " + prog.average(arr));
    }
}
