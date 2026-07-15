using System;

namespace DesignPrinciples
{
    // ==========================================
    // ❌ BAD: Repeating the same logic (DRY Violation)
    // ==========================================
    public class ReportGeneratorBad
    {
        public void GeneratePDFReport()
        {
            // Adding Header
            Console.WriteLine("--- Company Header ---");
            Console.WriteLine("Date: " + DateTime.Now);
            
            // Generate PDF logic...
            Console.WriteLine("Generating PDF...");
        }

        public void GenerateExcelReport()
        {
            // Adding Header (Repeated Code)
            Console.WriteLine("--- Company Header ---");
            Console.WriteLine("Date: " + DateTime.Now);
            
            // Generate Excel logic...
            Console.WriteLine("Generating Excel...");
        }
    }

    // ==========================================
    // ✅ GOOD: Reusing logic (DRY Principle)
    // ==========================================
    public class ReportGeneratorGood
    {
        // Extracted common logic to a single place
        private void PrintCompanyHeader()
        {
            Console.WriteLine("--- Company Header ---");
            Console.WriteLine("Date: " + DateTime.Now);
        }

        public void GeneratePDFReport()
        {
            PrintCompanyHeader(); // Reused
            Console.WriteLine("Generating PDF...");
        }

        public void GenerateExcelReport()
        {
            PrintCompanyHeader(); // Reused
            Console.WriteLine("Generating Excel...");
        }
    }
}
