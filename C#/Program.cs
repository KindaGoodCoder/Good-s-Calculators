class Program
    {
    static double inputnum(string txt)
    {
        Console.WriteLine(txt);
        txt = Console.ReadLine();
        if (txt == "exit")
        {
            Console.WriteLine("Exiting...");
            throw new InvalidOperationException("pain");
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
                Console.WriteLine("> Variable Power: "+Math.Log(constant,var)+"\n");
            }
            catch (FormatException) {
                Console.WriteLine("HEIL HYDRA\n");
                continue;
            }
            catch (InvalidOperationException) {
                break;
            }
        }
    }
}