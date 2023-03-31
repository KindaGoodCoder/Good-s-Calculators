class LogCal
    {
    static double inputnum(string txt)
    {
        Console.WriteLine(txt);
        txt = Console.ReadLine().Trim().ToLower();
        if (txt == "exit")
        {
            Console.WriteLine("Exiting...");
            throw new InvalidOperationException();
        }
        if (txt == "natural")
        {
            return Math.E
        }

        return Convert.ToDouble(txt);
    }
    static void Main()
    {
        while (true)
        {
            try {
                double constant = inputnum("Constant");
                double var = inputnum("Logarithimic Base");
                if (var < 0 || constant < 0)
                {
                    throw new FormatException();
                }
                Console.WriteLine("> Variable Power: "+Math.Round(Math.Log(constant,var),2)+"\n");
            }
            catch (FormatException) {
                Console.WriteLine("Invalid input, please enter valid positive number\n");
                continue;
            }
            catch (InvalidOperationException) {
                break;
            }
        }
    }
}