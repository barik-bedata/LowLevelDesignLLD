# Default vs Internal Class (Package/Assembly Level Access)

অবজেক্ট-ওরিয়েন্টিড প্রোগ্রামিংয়ে কোডের নিরাপত্তা ও মডুলারিটি বজায় রাখার জন্য অ্যাক্সেস মডিফায়ার (Access Modifier) ব্যবহার করা হয়। Java-তে **Default** (Package-Private) এবং C#-এ **Internal** প্রায় একই ধরণের ভূমিকা পালন করে, তবে তাদের কাজের স্কোপ বা পরিধি ভিন্ন।

---

## ১. Java-তে `default` (Package-Private) ক্লাস কী?

Java-তে কোনো ক্লাসের আগে যদি কোনো অ্যাক্সেস মডিফায়ার (`public`, `private`, `protected`) না লেখা হয়, তবে কম্পাইলার স্বয়ংক্রিয়ভাবে সেটিকে **Default** বা **Package-Private** হিসেবে ধরে নেয়।

### অ্যাক্সেস লিমিট (Who can use it?):
* শুধুমাত্র **একই প্যাকেজের (Package)** অধীনে থাকা অন্যান্য ক্লাসগুলো এই ক্লাসটিকে দেখতে পাবে এবং ব্যবহার করতে পারবে।
* প্যাকেজের বাইরের কোনো ক্লাস একে দেখতে বা ব্যবহার করতে পারবে না।

### Java Example:
ধরা যাক আমাদের `com.study.shapes` প্যাকেজে একটি ক্লাস আছে:
```java
package com.study.shapes;

// কোনো public/private নেই, তাই এটি default class
class CircleHelper {
    void drawCircle() {
        System.out.println("Drawing circle...");
    }
}
```
একই প্যাকেজের আরেকটি ক্লাস `Circle` এটি ব্যবহার করতে পারবে:
```java
package com.study.shapes;

public class Circle {
    public void render() {
        CircleHelper helper = new CircleHelper(); // সফলভাবে কাজ করবে
        helper.drawCircle();
    }
}
```
কিন্তু যদি প্যাকেজটি ভিন্ন হয় (যেমন: `com.study.main`), তবে সেখানে `CircleHelper` ব্যবহার করা যাবে না:
```java
package com.study.main;

import com.study.shapes.CircleHelper; // Compile Error! CircleHelper ইম্পোর্ট করা যাবে না।
```

---

## ২. C#-এ `internal` ক্লাস কী?

C#-এ `internal` একটি অ্যাক্সেস মডিফায়ার। যখন কোনো ক্লাসকে `internal class MyClass` হিসেবে ঘোষণা করা হয়, তখন এর অ্যাক্সেস একই **Assembly**-র ভেতরে সীমাবদ্ধ থাকে।

> **Assembly কী?**
> C#-এ অ্যাসেম্বলি হলো একটি কম্পাইলড প্রজেক্ট ফাইল (যেমন: `.dll` বা `.exe` ফাইল)। একটি সল্যুশনে (Solution) একাধিক প্রজেক্ট থাকতে পারে, যার প্রতিটি আলাদা অ্যাসেম্বলি।

### অ্যাক্সেস লিমিট (Who can use it?):
* শুধুমাত্র **একই প্রজেক্ট বা অ্যাসেম্বলির** ভেতরের যেকোনো কোড এই ক্লাসটিকে ব্যবহার করতে পারবে।
* অন্য কোনো প্রজেক্ট যদি এই প্রজেক্টের রেফারেন্সও নেয়, তবুও সে এই `internal` ক্লাসটি দেখতে পাবে না।

### C# Example:
ধরা যাক একটি ডাটাবেজ লাইব্রেরি প্রজেক্টে (`DatabaseConnector.csproj`) একটি ক্লাস আছে:
```csharp
namespace DatabaseConnector
{
    // Internal Class
    internal class ConnectionDecryptor
    {
        public string Decrypt(string encryptedString)
        {
            return "decrypted_connection_string";
        }
    }
}
```
এই প্রজেক্টের ভেতরে থাকা অন্য যেকোনো ক্লাস (যেমন: `DbConnection`) এই `ConnectionDecryptor` ব্যবহার করতে পারবে:
```csharp
namespace DatabaseConnector
{
    public class DbConnection
    {
        public void Connect()
        {
            var decryptor = new ConnectionDecryptor(); // সফলভাবে কাজ করবে
            string connectionString = decryptor.Decrypt("secret");
        }
    }
}
```
কিন্তু যদি বাইরের কোনো প্রজেক্ট (যেমন: `MyConsoleApp.csproj`) এই `DatabaseConnector` প্রজেক্টটি রেফারেন্স হিসেবে ব্যবহার করে, তবুও তারা সরাসরি `ConnectionDecryptor` অ্যাক্সেস করতে পারবে না:
```csharp
using DatabaseConnector;

namespace MyConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // compile error: ConnectionDecryptor is inaccessible due to its protection level
            var decryptor = new ConnectionDecryptor(); 
        }
    }
}
```

---

## কেন এবং কখন এগুলো ব্যবহার করবেন? (Use Cases & Advantages)

১. **অভ্যন্তরীণ কাজের লজিক লুকিয়ে রাখা (Implementation Hiding):**
   ধরা যাক আপনি একটি লাইব্রেরি বা মডিউল বানাচ্ছেন যা অন্য ডেভেলপাররা ব্যবহার করবেন। আপনি চান ব্যবহারকারীরা শুধুমাত্র নির্দিষ্ট কিছু `public` ক্লাস ব্যবহার করুক এবং ভেতরের জটিল বা সিকিউর মেকানিজমগুলো (`default` বা `internal` ক্লাস দিয়ে তৈরি) তাদের আড়ালে থাকুক।
   
২. **নিরাপত্তা ও কনফিডেন্সিয়ালিটি:**
   যেমন ডাটাবেজ পাসওয়ার্ড ডিক্রিপ্ট করা বা কোনো জটিল অ্যালগরিদম যা বাইরের কারো অ্যাক্সেস করার দরকার নেই, সেগুলো `internal` বা `default` ক্লাসে রাখা নিরাপদ।

৩. **মডুলার আর্কিটেকচার:**
   কোডকে ছোট ছোট মডিউলে ভাগ করতে সাহায্য করে এবং নিশ্চিত করে যে একটি মডিউলের অভ্যন্তরীণ কোড অন্য মডিউলের সাথে শক্তভাবে লেগে থাকবে না (Low Coupling)।
