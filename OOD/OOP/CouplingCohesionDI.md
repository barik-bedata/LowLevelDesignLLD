# Coupling, Cohesion, and Dependency Injection (DI)

অবজেক্ট-ওরিয়েন্টিড প্রোগ্রামিং (OOP) এবং সফটওয়্যার আর্কিটেকচারে কোডকে মেইনটেইনেবল, টেস্টেবল এবং স্কেলেবল করার জন্য **Coupling**, **Cohesion** এবং **Dependency Injection** অত্যন্ত গুরুত্বপূর্ণ ধারণা।

নিচে বাস্তব উদাহরণসহ এই বিষয়গুলো বিস্তারিত আলোচনা করা হলো:

---

## ১. Cohesion (কোইশন) কী?

**Cohesion** নির্দেশ করে একটি সিঙ্গেল ক্লাস বা মডিউলের ভেতরের মেথড ও ভেরিয়েবলগুলো একে অপরের সাথে কতটা সম্পর্কিত বা নিবিড়ভাবে কাজ করে। 

> **সফটওয়্যার ডিজাইনের গোল:** **High Cohesion (উচ্চ কোইশন)**
> অর্থাৎ, একটি ক্লাসের শুধুমাত্র একটি নির্দিষ্ট দায়িত্ব থাকা উচিত (Single Responsibility Principle)।

### ক. Low Cohesion (খারাপ ডিজাইন):
একটি ক্লাসের ভেতর যখন একাধিক অসম্পর্কিত দায়িত্ব দেওয়া হয়।

```csharp
// এখানে একটি ক্লাসই ডাটাবেজ সেভ করছে, ইমেইল পাঠাচ্ছে এবং ট্যাক্স হিসাব করছে।
public class EmployeeManager
{
    public void SaveEmployee(Employee emp) { /* ডাটাবেজ কোড */ }
    public void CalculateTax(Employee emp) { /* ট্যাক্স হিসাবের লজিক */ }
    public void SendEmail(string message) { /* ইমেইল পাঠানোর কোড */ }
}
```
**সমস্যা:** এখানে কোনো পরিবর্তন করতে গেলে পুরো ক্লাসটি রিস্কের মুখে পড়বে এবং কোড মেইনটেইন করা কঠিন হবে।

### খ. High Cohesion (ভালো ডিজাইন):
প্রতিটি ক্লাসের দায়িত্ব আলাদা এবং সুনির্দিষ্ট।

```csharp
public class EmployeeRepository
{
    public void SaveEmployee(Employee emp) { /* শুধুমাত্র ডাটাবেজ লজিক */ }
}

public class TaxCalculator
{
    public double CalculateTax(Employee emp) { /* শুধুমাত্র ট্যাক্স লজিক */ }
}

public class EmailService
{
    public void SendEmail(string message) { /* শুধুমাত্র ইমেইল লজিক */ }
}
```
**সুবিধা:** প্রতিটি ক্লাস ছোট, পরিষ্কার এবং সহজে রি-ইউজেবল (Reusable)।

---

## ২. Coupling (কপলিং) কী?

**Coupling** নির্দেশ করে দুটি ভিন্ন ক্লাস বা মডিউল একে অপরের ওপর কতটা নির্ভরশীল। 

> **সফটওয়্যার ডিজাইনের গোল:** **Loose Coupling (শিথিল কপলিং)**
> ক্লাসগুলোর মধ্যে নির্ভরশীলতা যত কম হবে, কোড তত সহজে পরিবর্তন ও টেস্ট করা যাবে।

### ক. Tight Coupling (খারাপ ডিজাইন):
যখন একটি ক্লাস সরাসরি অন্য ক্লাসের অবজেক্ট তৈরি করে এবং তার ওপর শক্তভাবে নির্ভরশীল হয়ে পড়ে।

```csharp
public class Car
{
    private Engine _engine;

    public Car()
    {
        // Car সরাসরি Engine ক্লাসের কংক্রিট ইমপ্লিমেন্টেশনের ওপর নির্ভরশীল
        _engine = new Engine(); 
    }

    public void StartCar()
    {
        _engine.Start();
    }
}
```
**সমস্যা:** আপনি যদি ভবিষ্যতে `ElectricEngine` ব্যবহার করতে চান, তবে আপনাকে `Car` ক্লাসের ভেতর ঢুকে কোড পরিবর্তন করতে হবে। এছাড়া, `Car` ক্লাসকে একা ইউনিট টেস্ট করা অসম্ভব (কারণ এটি `Engine` এর ওপর সরাসরি নির্ভরশীল)।

### খ. Loose Coupling (ভালো ডিজাইন):
ইন্টারফেস (Interface) ব্যবহারের মাধ্যমে ক্লাসগুলোর মধ্যকার শক্ত বাঁধন শিথিল করা হয়।

```csharp
public interface IEngine
{
    void Start();
}

public class Car
{
    private IEngine _engine;

    // Car এখন সরাসরি কোনো নির্দিষ্ট Engine এর ওপর নির্ভর করছে না, বরং IEngine ইন্টারফেসের ওপর নির্ভর করছে
    public Car(IEngine engine)
    {
        _engine = engine;
    }

    public void StartCar()
    {
        _engine.Start();
    }
}
```
**সুবিধা:** এখন আপনি `Car` ক্লাসের কোনো পরিবর্তন না করেই `V8Engine` বা `ElectricEngine` পাস করতে পারবেন।

---

## ৩. Dependency Injection (DI) কী?

**Dependency Injection (DI)** হলো একটি ডিজাইন প্যাটার্ন যা **Loose Coupling** অর্জনে সরাসরি সাহায্য করে।

ডিপেন্ডেন্সি (Dependency) মানে হলো কোনো কাজ করার জন্য একটি ক্লাসের যখন অন্য কোনো ক্লাসের অবজেক্টের প্রয়োজন হয় (যেমন: `Car` এর জন্য `Engine` একটি ডিপেন্ডেন্সি)।
আর ইনজেকশন (Injection) মানে হলো সেই প্রয়োজনীয় অবজেক্টটি নিজের ভেতরে `new` দিয়ে তৈরি না করে, **বাইর থেকে সরবরাহ করা বা পাস করে দেওয়া**।

### DI এর প্রকারভেদ:
১. **Constructor Injection:** সবচেয়ে বেশি ব্যবহৃত হয়। কন্সট্রাকটরের মাধ্যমে ডিপেন্ডেন্সি পাস করা হয়।
২. **Property/Setter Injection:** প্রোপার্টি বা সেট মেথডের মাধ্যমে ডিপেন্ডেন্সি পাস করা হয়।
৩. **Method Injection:** সরাসরি কোনো নির্দিষ্ট মেথডের প্যারামিটার হিসেবে ডিপেন্ডেন্সি পাস করা হয়।

### DI এর কোড উদাহরণ (Constructor Injection):

```csharp
// ১. ডিপেন্ডেন্সি ইন্টারফেস
public interface IMessageService
{
    void Send(string message);
}

// ২. কংক্রিট ইমপ্লিমেন্টেশন
public class SmsService : IMessageService
{
    public void Send(string message) => Console.WriteLine($"SMS Sent: {message}");
}

public class EmailService : IMessageService
{
    public void Send(string message) => Console.WriteLine($"Email Sent: {message}");
}

// ৩. ডিপেন্ডেন্ট ক্লাস (যেখানে ইনজেকশন হবে)
public class NotificationManager
{
    private readonly IMessageService _messageService;

    // Constructor Injection: বাইর থেকে IMessageService ইনজেক্ট করা হচ্ছে
    public NotificationManager(IMessageService messageService)
    {
        _messageService = messageService;
    }

    public void Notify(string msg)
    {
        _messageService.Send(msg);
    }
}

// ৪. ব্যবহার (Usage):
class Program
{
    static void Main()
    {
        // আমরা চাইলে SMS দিয়ে নোটিফাই করতে পারি:
        IMessageService sms = new SmsService();
        NotificationManager notification1 = new NotificationManager(sms);
        notification1.Notify("Hello User!");

        // কোড পরিবর্তন না করে সহজেই Email এ পরিবর্তন করা সম্ভব:
        IMessageService email = new EmailService();
        NotificationManager notification2 = new NotificationManager(email);
        notification2.Notify("Hello User!");
    }
}
```

---

## সংক্ষেপে সারমর্ম (Summary)

* **Cohesion:** একটি ক্লাসের অভ্যন্তরীণ কাজের একাগ্রতা। (আমাদের লক্ষ্য: **High Cohesion** বা এক ক্লাসে এক দায়িত্ব)।
* **Coupling:** একাধিক ক্লাসের পারস্পরিক নির্ভরশীলতা। (আমাদের লক্ষ্য: **Loose Coupling** বা ক্লাসগুলোর মধ্যকার ন্যূনতম বাঁধন)।
* **Dependency Injection:** নিজের ডিপেন্ডেন্সি নিজে `new` দিয়ে তৈরি না করে বাইর থেকে ইনজেক্ট করা, যা Loose Coupling নিশ্চিত করে।
