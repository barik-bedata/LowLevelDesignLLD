using System;

namespace OOP.Inheritance
{
    // Base Class (Parent Class)
    public class Animal
    {
        public string Name { get; set; }

        public Animal(string name)
        {
            Name = name;
        }

        // Virtual method allows derived classes to override it
        public virtual void Speak()
        {
            Console.WriteLine($"{Name} makes a generic animal sound.");
        }

        // Standard method inherited by all derived classes
        public void Eat()
        {
            Console.WriteLine($"{Name} is eating.");
        }
    }

    // Derived Class (Child Class) inheriting from Animal
    public class Dog : Animal
    {
        public string Breed { get; set; }

        // Using 'base' to call the constructor of the parent class
        public Dog(string name, string breed) : base(name)
        {
            Breed = breed;
        }

        // Overriding the virtual method from the parent class
        public override void Speak()
        {
            Console.WriteLine($"{Name} the {Breed} barks: Woof! Woof!");
        }

        public void Fetch()
        {
            Console.WriteLine($"{Name} is fetching the ball.");
        }
    }

    // Another Derived Class
    public class Cat : Animal
    {
        public Cat(string name) : base(name)
        {
        }

        public override void Speak()
        {
            Console.WriteLine($"{Name} meows: Meow~");
        }
    }

    class Program
    {
        static void Main()
        {
            // Creating an object of the derived class 'Dog'
            Dog myDog = new Dog("Buddy", "Golden Retriever");
            
            // Inherited property
            Console.WriteLine($"My dog's name is {myDog.Name}.");
            
            // Inherited method
            myDog.Eat();

            // Overridden method specific to Dog
            myDog.Speak();

            // Method specific to Dog only
            myDog.Fetch();

            Console.WriteLine("-------------------");

            Cat myCat = new Cat("Whiskers");
            myCat.Eat();
            myCat.Speak();
        }
    }
}
