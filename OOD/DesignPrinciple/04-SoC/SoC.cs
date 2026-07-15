using System;

namespace DesignPrinciples
{
    // ==========================================
    // ❌ BAD: Mixing everything together (SoC Violation)
    // ==========================================
    public class OrderProcessorBad
    {
        public void ProcessOrder()
        {
            // 1. Validation Logic
            Console.WriteLine("Validating order...");
            
            // 2. Database Logic
            Console.WriteLine("Saving order to database...");

            // 3. Email Notification Logic
            Console.WriteLine("Sending confirmation email...");
        }
    }

    // ==========================================
    // ✅ GOOD: Separating the concerns (SoC Principle)
    // ==========================================
    
    public class OrderValidator
    {
        public void Validate() => Console.WriteLine("Validating order...");
    }

    public class OrderRepository
    {
        public void Save() => Console.WriteLine("Saving order to database...");
    }

    public class EmailService
    {
        public void SendEmail() => Console.WriteLine("Sending confirmation email...");
    }

    public class OrderProcessorGood
    {
        private OrderValidator _validator = new OrderValidator();
        private OrderRepository _repository = new OrderRepository();
        private EmailService _emailService = new EmailService();

        public void ProcessOrder()
        {
            // The processor now only coordinates, each class does its own specific job.
            _validator.Validate();
            _repository.Save();
            _emailService.SendEmail();
        }
    }
}
