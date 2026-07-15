using System;

namespace DesignPrinciples
{
    public class DateHelper
    {
        // ==========================================
        // ❌ BAD: Overcomplicating simple logic (KISS Violation)
        // ==========================================
        public string GetMonthNameBad(int monthNumber)
        {
            // Unnecessarily complex way to return a month name
            string[] months = { "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" };
            
            try
            {
                if (monthNumber >= 1 && monthNumber <= 12)
                {
                    return months[monthNumber - 1];
                }
                else
                {
                    throw new Exception("Invalid month");
                }
            }
            catch (Exception ex)
            {
                return ex.Message;
            }
        }

        // ==========================================
        // ✅ GOOD: Simple and readable (KISS Principle)
        // ==========================================
        public string GetMonthNameGood(int monthNumber)
        {
            // Simple, built-in, easy to read
            if (monthNumber < 1 || monthNumber > 12)
                return "Invalid month";

            return new DateTime(2000, monthNumber, 1).ToString("MMMM");
        }
    }
}
