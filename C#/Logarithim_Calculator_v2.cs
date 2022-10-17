class LogCal
    {
    static double inputnum(string txt)
    {
        Console.WriteLine(txt);
        txt = Console.ReadLine();
        if (txt == "exit")
        {
            Console.WriteLine("Exiting...");
            throw new InvalidOperationException();
        }

        return Convert.ToDouble(txt);
    }
    static void Main()
    {
        while (true)
        {
            try {
                double constant = inputnum("Constant");
                double var = inputnum("Variable Base");
                if (var < 2)
                {
                    throw new FormatException();
                }
                Console.WriteLine("> Variable Power: "+Math.Round(Math.Log(constant,var),2)+"\n");
            }
            catch (FormatException) {
                Console.WriteLine("Invalid number, please enter valid positive number\n");
                continue;
            }
            catch (InvalidOperationException) {
                break;
            }
        }
    }
}