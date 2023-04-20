class Program
{
    public delegate void ProgramHandler(double num);
    public event ProgramHandler? Notify;

    public void Sum(double x, double y)
    {
        Notify?.Invoke(x + y);
    }

    public void Dif(double x, double y)
    {
        Notify?.Invoke(x - y);
    }

    public void Multi(double x, double y)
    {
        Notify?.Invoke(x * y);
    }

    public void Div(double x, double y)
    {
        if (y != 0)
        {
            Notify?.Invoke(x / y);
        } else
        {
            Notify?.Invoke(y);
        }
    }

    static void DisplayMessage(double message) => Console.WriteLine(message);

    public static void Main()
    {
        Program program = new Program();
        program.Notify += DisplayMessage;
        double x = Convert.ToDouble(Console.ReadLine()), y = Convert.ToDouble(Console.ReadLine());
        program.Sum(x, y);
        program.Dif(x, y);
        program.Multi(x, y);
        program.Div(x, y);
    }
}
