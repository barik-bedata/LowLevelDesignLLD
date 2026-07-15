using System;

namespace DesignPrinciples
{
    // ==========================================
    // ❌ BAD: Adding features we don't need right now (YAGNI Violation)
    // ==========================================
    public class UserRegistrationBad
    {
        public void RegisterUser(string username, string password)
        {
            Console.WriteLine($"User {username} registered.");
        }

        // We don't have a mobile app yet, but we wrote this just in case.
        // This is a waste of time and adds unnecessary code to maintain.
        public void RegisterUserFromMobileApp(string username, string password, string deviceId)
        {
            Console.WriteLine($"User {username} registered from device {deviceId}.");
        }
    }

    // ==========================================
    // ✅ GOOD: Only building what is required today (YAGNI Principle)
    // ==========================================
    public class UserRegistrationGood
    {
        // The current requirement is only simple registration.
        public void RegisterUser(string username, string password)
        {
            Console.WriteLine($"User {username} registered.");
        }

        // We will add mobile registration later ONLY IF the requirement actually comes.
    }
}
