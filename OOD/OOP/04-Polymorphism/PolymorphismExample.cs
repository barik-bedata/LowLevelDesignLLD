using System;

namespace OOP.Polymorphism
{
    // --- 1. COMPILE-TIME POLYMORPHISM (Method Overloading) ---
    public class MathOperations
    {
        // Add two integers
        public int Add(int a, int b)
        {
            return a + b;
        }

        // Add three integers (Overloaded by number of parameters)
        public int Add(int a, int b, int c)
        {
            return a + b + c;
        }

        // Add two doubles (Overloaded by parameter type)
        public double Add(double a, double b)
        {
            return a + b;
        }
    }

    // --- 2. RUN-TIME POLYMORPHISM (Method Overriding) ---
    public class Animal
    {
        // Virtual method allows it to be overridden in derived classes
        public virtual void Move()
        {
            Console.WriteLine("The animal moves.");
        }
    }

    public class Bird : Animal
    {
        // Overriding the base class method
        public override void Move()
        {
            Console.WriteLine("The bird flies in the sky.");
        }
    }

    public class Fish : Animal
    {
        // Overriding the base class method
        public override void Move()
        {
            Console.WriteLine("The fish swims in the water.");
        }
    }

    class Program
    {
        static void Main()
        {
            Console.WriteLine("--- Compile-time Polymorphism (Overloading) ---");
            MathOperations math = new MathOperations();
            Console.WriteLine($"2 + 3 = {math.Add(2, 3)}");
            Console.WriteLine($"2 + 3 + 4 = {math.Add(2, 3, 4)}");
            Console.WriteLine($"2.5 + 3.2 = {math.Add(2.5, 3.2)}");

            Console.WriteLine("\n--- Run-time Polymorphism (Overriding) ---");
            
            // Polymorphism in action: Reference type is 'Animal', but object type varies
            Animal myAnimal = new Animal();
            Animal myBird = new Bird();
            Animal myFish = new Fish();

            // The correct 'Move' method is called based on the ACTUAL object type at runtime
            myAnimal.Move(); // Output: The animal moves.
            myBird.Move();   // Output: The bird flies in the sky.
            myFish.Move();   // Output: The fish swims in the water.
        }
    }
}
