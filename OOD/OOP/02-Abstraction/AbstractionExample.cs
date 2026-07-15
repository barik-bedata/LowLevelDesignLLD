using System;

namespace OOP.Abstraction
{
    // Abstract Class - cannot be instantiated
    public abstract class Shape
    {
        public string Color { get; set; }

        public Shape(string color)
        {
            Color = color;
        }

        // Abstract method - no implementation here, must be overridden
        public abstract double CalculateArea();

        // Non-abstract method - has implementation
        public void DisplayColor()
        {
            Console.WriteLine($"The shape color is {Color}.");
        }
    }

    // Concrete Class - inherits from Shape and provides implementation
    public class Circle : Shape
    {
        private double _radius;

        public Circle(string color, double radius) : base(color)
        {
            _radius = radius;
        }

        // Overriding the abstract method
        public override double CalculateArea()
        {
            return Math.PI * _radius * _radius;
        }
    }

    // Concrete Class
    public class Rectangle : Shape
    {
        private double _width;
        private double _height;

        public Rectangle(string color, double width, double height) : base(color)
        {
            _width = width;
            _height = height;
        }

        // Overriding the abstract method
        public override double CalculateArea()
        {
            return _width * _height;
        }
    }

    class Program
    {
        static void Main()
        {
            // Shape myShape = new Shape("Red"); // Error: Cannot create an instance of the abstract type 'Shape'

            // We interact with the abstract concept of a 'Shape'
            Shape myCircle = new Circle("Red", 5.0);
            Shape myRectangle = new Rectangle("Blue", 4.0, 6.0);

            myCircle.DisplayColor();
            Console.WriteLine($"Circle Area: {myCircle.CalculateArea():F2}");

            myRectangle.DisplayColor();
            Console.WriteLine($"Rectangle Area: {myRectangle.CalculateArea():F2}");
        }
    }
}
