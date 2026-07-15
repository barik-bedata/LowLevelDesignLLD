# Sealed Class vs Final Class in OOP

অবজেক্ট-ওরিয়েন্টিড প্রোগ্রামিংয়ে (OOP) ইনহেরিটেন্স বা উত্তরাধিকার নিয়ন্ত্রণ করার জন্য **Sealed Class** এবং **Final Class** ব্যবহার করা হয়। এই কী-ওয়ার্ডগুলো মূলত কোনো ক্লাসের ইনহেরিট করার ক্ষমতা সীমিত বা বন্ধ করে দেয়।

ল্যাঙ্গুয়েজ ভেদে (যেমন C# এবং Java) এগুলোর নামের পার্থক্য রয়েছে, এবং আধুনিক সংস্করণে এদের ধারণায় কিছুটা ভিন্নতা এসেছে। নিচে বিস্তারিত আলোচনা করা হলো:

---

## ১. Java-তে `final` ক্লাস এবং C#-এ `sealed` ক্লাস

এই দুটি কী-ওয়ার্ডের মূল কাজ একই—**ইনহেরিটেন্স সম্পূর্ণ বন্ধ করা**। যদি কোনো ক্লাসকে `final` (Java) বা `sealed` (C#) হিসেবে ঘোষণা করা হয়, তবে অন্য কোনো ক্লাস সেটিকে ইনহেরিট বা এক্সটেন্ড (Extend) করতে পারবে না। 


### C# Example (`sealed`):
```csharp
public sealed class DatabaseConfig
{
    public string ConnectionString { get; set; }
}

// এটি কম্পাইল এরর দেবে!
public class CustomConfig : DatabaseConfig 
{
    // Error: 'CustomConfig': cannot derive from sealed type 'DatabaseConfig'
}
```

### Java Example (`final`):
```java
public final class StringHelper {
    public static String reverse(String input) {
        return new StringBuilder(input).reverse().toString();
    }
}

// এটি কম্পাইল এরর দেবে!
public class CustomStringHelper extends StringHelper {
    // Error: cannot inherit from final StringHelper
}
```

---

## ২. Java 17+ এবং Kotlin-এ `sealed` ক্লাস (সীমিত উত্তরাধিকার)

আধুনিক Java (Java 17+) এবং Kotlin-এ `sealed` ক্লাস একটি নতুন ধারণা নিয়ে এসেছে। এখানে ইনহেরিটেন্স সম্পূর্ণ বন্ধ করা হয় না, বরং **নিয়ন্ত্রিত** করা হয়। 

একটি `sealed` ক্লাস অনুমতি দেয় যে, শুধুমাত্র নির্দিষ্ট কয়েকটি ক্লাসই তাকে ইনহেরিট করতে পারবে এবং অন্য কোনো ক্লাস তা পারবে না।

### Java 17+ Example:
```java
// শুধুমাত্র Car এবং Truck ক্লাসই Vehicle-কে ইনহেরিট করতে পারবে
public sealed class Vehicle permits Car, Truck {
    // ...
}

public final class Car extends Vehicle {
    // সফলভাবে ইনহেরিট করবে
}

public final class Truck extends Vehicle {
    // সফলভাবে ইনহেরিট করবে
}

// এটি কম্পাইল এরর দেবে!
public class Bicycle extends Vehicle {
    // Error: class is not allowed in the permits list
}
```

---

## কেন এবং কখন এগুলো ব্যবহার করবেন? (Use Cases & Benefits)

১. **নিরাপত্তা নিশ্চিত করা (Security):**
   সিস্টেমের কিছু গুরুত্বপূর্ণ মেকানিজম বা ডাটা ক্লাসকে আমরা চাই না কেউ ইনহেরিট করে তার মেথডগুলোকে ওভাররাইড (Override) করুক। 
   *যেমন: Java ও C# এর বিল্ট-ইন `String` ক্লাসটি `final/sealed` করা থাকে, যাতে কেউ কাস্টম স্ট্রিং ক্লাস বানিয়ে মেমরিতে ডেঞ্জারাস কোনো আচরণ তৈরি করতে না পারে।*

২. **পারফরম্যান্স অপ্টিমাইজেশন (Performance):**
   কম্পাইলার যখন দেখে কোনো ক্লাস `final` বা `sealed`, তখন সে নিশ্চিত হয় যে এই ক্লাসের কোনো চাইল্ড ক্লাস নেই। ফলে কম্পাইলার রানটাইমে মেথড রেজোলিউশন দ্রুত করতে পারে (যাকে *devirtualization* বলা হয়)।

৩. **এপিআই ডিজাইন এবং ডোমেইন কন্ট্রোল:**
   আপনি যদি কোনো লাইব্রেরি তৈরি করেন, এবং চান ব্যবহারকারীরা আপনার নির্দিষ্ট করা ফ্রেমওয়ার্কের বাইরে ক্লাসগুলোকে ইনহেরিট না করুক, তখন এটি দরকারি।

---

## সংক্ষেপে তুলনা (At a Glance)

| ল্যাঙ্গুয়েজ | কী-ওয়ার্ড | ইনহেরিটেন্সের নিয়ম |
| :--- | :--- | :--- |
| **Java** | `final` | কোনোভাবেই ইনহেরিট করা যাবে না। |
| **Java 17+** | `sealed` | শুধুমাত্র `permits` তালিকায় থাকা ক্লাসগুলোই ইনহেরিট করতে পারবে। |
| **C#** | `sealed` | কোনোভাবেই ইনহেরিট করা যাবে না। |
| **Kotlin** | `sealed` | একই ফাইলের/মডিউলের নির্দিষ্ট সাবক্লাস ছাড়া অন্য কেউ ইনহেরিট করতে পারবে না। |
