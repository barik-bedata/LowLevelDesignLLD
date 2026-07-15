# Private Constructor and Default Constructor in OOP

অবজেক্ট-ওরিয়েন্টিড প্রোগ্রামিংয়ে (OOP) অবজেক্ট তৈরির প্রক্রিয়া এবং তার অ্যাক্সেস নিয়ন্ত্রণ করার জন্য কন্সট্রাকটর (Constructor) অত্যন্ত গুরুত্বপূর্ণ ভূমিকা পালন করে। নিচে **Default Constructor** এবং **Private Constructor** সম্পর্কে বিস্তারিত আলোচনা করা হলো:

---

## ১. Default Constructor কী? (কন্সট্রাকটর ডিফাইন না করলে কী হয়?)

যদি কোনো ক্লাসের ভেতর আমরা নিজেরা কোনো কন্সট্রাকটর ডিক্লেয়ার বা ডিফাইন না করি, তবে কম্পাইলার স্বয়ংক্রিয়ভাবে ক্লাসটির জন্য একটি প্যারামিটারহীন (Parameterless) এবং পাবলিক কন্সট্রাকটর তৈরি করে দেয়। একেই **Default Constructor** বলে।

### বৈশিষ্ট্য:
* এটি ক্লাসের অবজেক্ট তৈরি করতে সাহায্য করে।
* এটি সাধারণত মেম্বার ভেরিয়েবলগুলোকে তাদের ডিফল্ট মান (যেমন: সংখ্যার জন্য `0`, অবজেক্টের জন্য `null`) দিয়ে ইনিশিয়ালাইজ করে।

```java
// আমরা কোনো কন্সট্রাকটর লিখিনি
public class Student {
    public String name;
}

// কিন্তু কম্পাইলার ব্যাকগ্রাউন্ডে এটি তৈরি করে নিয়েছে:
// public Student() { }

// তাই আমরা সরাসরি অবজেক্ট তৈরি করতে পারি:
Student s = new Student(); 
```

⚠️ **মনে রাখবেন:** যদি আপনি নিজে যেকোনো একটি কন্সট্রাকটর (যেমন: প্যারামিটারসহ কন্সট্রাকটর) তৈরি করেন, তবে কম্পাইলার আর কোনো default কন্সট্রাকটর নিজে থেকে তৈরি করবে না। সেক্ষেত্রে আপনাকে ম্যানুয়ালি প্যারামিটারহীন কন্সট্রাকটর লিখতে হবে যদি আপনি `new Student()` ব্যবহার করতে চান।

---

## ২. Private Constructor কী এবং কীভাবে কাজ করে?

যখন কোনো কন্সট্রাকটরের আগে `private` অ্যাক্সেস মডিফায়ার ব্যবহার করা হয়, তখন তাকে **Private Constructor** বলে।

* **কীভাবে কাজ করে:** কন্সট্রাকটরটি `private` হওয়ার কারণে ক্লাসের বাইরে থেকে সরাসরি `new MyClass()` লিখে ওই ক্লাসের অবজেক্ট তৈরি করা যায় না। অবজেক্ট তৈরির অ্যাক্সেস শুধুমাত্র ওই ক্লাসের ভেতরের মেম্বার বা মেথডগুলোর কাছেই থাকে।

```csharp
public class Utility
{
    // Private Constructor
    private Utility() 
    {
    }

    public static void PrintMessage()
    {
        Console.WriteLine("Hello World!");
    }
}

// বাইরের ক্লাস থেকে অবজেক্ট তৈরি করতে গেলে এরর আসবে:
// Utility util = new Utility(); // Compile Error: 'Utility.Utility()' is inaccessible due to its protection level
```

---

## ৩. কেন এবং কখন Private Constructor ব্যবহার করতে হয়?

বাস্তব ক্ষেত্রে মূলত তিনটি কারণে Private Constructor ব্যবহার করা হয়:

### ক. সিঙ্গেলটন প্যাটার্ন (Singleton Pattern)
যখন আমরা নিশ্চিত করতে চাই যে পুরো অ্যাপ্লিকেশনে একটি ক্লাসের **শুধুমাত্র একটিই অবজেক্ট** থাকবে (যেমন: ডাটাবেজ কানেকশন বা গ্লোবাল কনফিগারেশন ম্যানেজার)।

```csharp
public class DatabaseConnection
{
    private static DatabaseConnection _instance;

    // ১. কন্সট্রাকটর প্রাইভেট করা হয়েছে যাতে বাইরে থেকে কেউ new করতে না পারে
    private DatabaseConnection() 
    {
        // কানেকশন ইনিশিয়ালাইজেশন লজিক
    }

    // ২. একটি স্ট্যাটিক মেথডের মাধ্যমে অবজেক্ট অ্যাক্সেস করা হয়
    public static DatabaseConnection GetInstance()
    {
        if (_instance == null)
        {
            _instance = new DatabaseConnection(); // ক্লাসের ভেতর থেকে অবজেক্ট তৈরি সম্ভব
        }
        return _instance;
    }
}
```

### খ. ইউটিলিটি বা হেল্পার ক্লাস (Utility/Helper Class)
যে ক্লাসগুলোতে শুধুমাত্র `static` মেথড এবং প্রোপার্টি থাকে (যেমন: গাণিতিক হিসাবনিকাশের ক্লাস বা স্ট্রিং ফরম্যাটিং ক্লাস)। এই ক্লাসগুলোর অবজেক্ট তৈরি করার কোনো প্রয়োজন নেই।
*যেমন: Java-এর `Math` ক্লাস। আপনি কখনো `new Math()` তৈরি করতে পারবেন না, কারণ এর কন্সট্রাকটর প্রাইভেট করা।*

### গ. ফ্যাক্টরি মেথড (Factory Method Pattern)
অবজেক্ট তৈরির লজিককে সরাসরি `new` কী-ওয়ার্ড দিয়ে প্রকাশ না করে নির্দিষ্ট মেথডের মাধ্যমে নিয়ন্ত্রণ করতে চাইলে।

```java
public class User {
    private String role;

    // প্রাইভেট কন্সট্রাকটর
    private User(String role) {
        this.role = role;
    }

    // ফ্যাক্টরি মেথড
    public static User createAdmin() {
        return new User("Admin");
    }

    public static User createGuest() {
        return new User("Guest");
    }
}
```

---

## সংক্ষেপে সারমর্ম (Summary)
* **Default Constructor:** আপনি কন্সট্রাকটর না লিখলে কম্পাইলার নিজে থেকে একটি পাবলিক কন্সট্রাকটর তৈরি করে দেয় যাতে অবজেক্ট বানানো যায়।
* **Private Constructor:** এটি ব্যবহার করে ক্লাসের বাইরে থেকে সরাসরি `new` কী-ওয়ার্ড দিয়ে অবজেক্ট তৈরি করা বন্ধ করা হয়। এটি প্রধানত **Singleton Pattern**, **Utility Class**, এবং **Factory Method** এ ব্যবহৃত হয়।
