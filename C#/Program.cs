using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Constant");
            double constant = Convert.ToDouble((Console.ReadLine()));
            Console.WriteLine("Variable Base");
            double var = Convert.ToDouble((Console.ReadLine()));
            Console.WriteLine(Math.Log(constant,var));
        }
    }
}