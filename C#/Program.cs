class Program
    {
    static double inputnum()
    {
        Console.WriteLine("Constant");
        return 5.9;
    }
    static void Main()
    {
        while (true)
        {
            inputnum();
            double constant = Convert.ToDouble((Console.ReadLine()));
            Console.WriteLine("Variable Base");
            double var = Convert.ToDouble((Console.ReadLine()));
            Console.WriteLine("> Variable Power: "+Math.Log(constant,var));
            Console.WriteLine();
        }
    }
}