using System;

namespace OOP.Encapsulation
{
    // The class encapsulates the data (balance) and methods that operate on it.
    public class BankAccount
    {
        // Private field - data is hidden from outside the class
        private decimal _balance;

        // Constructor
        public BankAccount(decimal initialBalance)
        {
            _balance = initialBalance;
        }

        // Public Property - provides controlled access to the private field
        public decimal Balance
        {
            get { return _balance; } // Read-only from outside (if no set is provided)
            // We omit the 'set' to prevent direct modification of balance.
        }

        // Public method to deposit money safely
        public void Deposit(decimal amount)
        {
            if (amount <= 0)
            {
                Console.WriteLine("Deposit amount must be positive.");
                return;
            }
            
            _balance += amount;
            Console.WriteLine($"Deposited {amount:C}. New balance is {_balance:C}.");
        }

        // Public method to withdraw money safely
        public void Withdraw(decimal amount)
        {
            if (amount <= 0)
            {
                Console.WriteLine("Withdrawal amount must be positive.");
                return;
            }

            if (amount > _balance)
            {
                Console.WriteLine("Insufficient funds!");
                return;
            }

            _balance -= amount;
            Console.WriteLine($"Withdrew {amount:C}. New balance is {_balance:C}.");
        }
    }

    class Program
    {
        static void Main()
        {
            // Create a new bank account with initial balance
            BankAccount account = new BankAccount(1000m);

            Console.WriteLine($"Initial Balance: {account.Balance:C}");

            // We cannot do this: account._balance = 50000; (Error: _balance is inaccessible due to its protection level)
            // We cannot do this either: account.Balance = 50000; (Error: Property cannot be assigned to -- it is read only)

            // We MUST interact through the provided public methods
            account.Deposit(500m);
            account.Withdraw(200m);
            account.Withdraw(2000m); // This will show an error message
        }
    }
}
