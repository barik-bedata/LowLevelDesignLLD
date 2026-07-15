# Upcasting and Downcasting in OOP

অবজেক্ট-ওরিয়েন্টিড প্রোগ্রামিংয়ে (OOP) ইনহেরিটেন্সের (Inheritance) ক্ষেত্রে এক ধরণের অবজেক্টকে অন্য টাইপে রূপান্তর করার প্রক্রিয়াকে **Type Casting** বলে। এটি মূলত দুই প্রকার:
1. **Upcasting** (চাইল্ড থেকে প্যারেন্ট টাইপে রূপান্তর)
2. **Downcasting** (প্যারেন্ট থেকে চাইল্ড টাইপে রূপান্তর)

---

## ১. Upcasting কী এবং কেন ব্যবহার করা হয়?

**Upcasting** হলো চাইল্ড (Child/Derived) ক্লাসের অবজেক্টকে তার প্যারেন্ট (Parent/Base) ক্লাসের রেফারেন্সে রূপান্তর করা।

* **কীভাবে কাজ করে:** এটি স্বয়ংক্রিয়ভাবে ঘটে (Implicitly)। এর জন্য আলাদা কোনো কাস্টিং ব্র্যাকেট বা কোড লিখতে হয় না।
* **কেন ব্যবহার করা হয়:** পলিমরফিজম (Polymorphism) এবং জেনারেলাইজেশন অর্জনের জন্য। এটি দিয়ে আমরা একাধিক ভিন্ন ভিন্ন চাইল্ড অবজেক্টকে একটি সাধারণ প্যারেন্ট টাইপ হিসেবে ট্রিট করতে পারি।

### Upcasting Example (C# / Java):
ধরা যাক আমাদের একটি প্যারেন্ট ক্লাস `Animal` এবং একটি চাইল্ড ক্লাস `Dog` আছে।

```csharp
public class Animal 
{
    public virtual void MakeSound() 
    {
        Console.WriteLine("Animal makes a sound.");
    }
}

public class Dog : Animal 
{
    public override void MakeSound() 
    {
        Console.WriteLine("Dog barks: Woof! Woof!");
    }

    public void PlayFetch() 
    {
        Console.WriteLine("Dog is playing fetch.");
    }
}
```

আমরা এভাবে Upcasting করতে পারি:
```csharp
Dog myDog = new Dog();
Animal myAnimal = myDog; // Upcasting (Implicit)

myAnimal.MakeSound(); // আউটপুট হবে: Dog barks: Woof! Woof! (Polymorphism)
```

⚠️ **সীমাবদ্ধতা (Limitation of Upcasting):**
Upcasting করার পর, প্যারেন্ট রেফারেন্স (`myAnimal`) দিয়ে চাইল্ড ক্লাসের নিজস্ব বিশেষ কোনো মেথড (যেমন `PlayFetch()`) কল করা যাবে না। 
```csharp
myAnimal.PlayFetch(); // Compile Error! Animal ক্লাসে PlayFetch() নেই।
```

---

## ২. Downcasting কী এবং কেন ব্যবহার করা হয়?

**Downcasting** হলো প্যারেন্ট ক্লাসের রেফারেন্সকে পুনরায় তার নির্দিষ্ট চাইল্ড ক্লাসের রেফারেন্সে রূপান্তর করা।

* **কীভাবে কাজ করে:** এটি নিজে নিজে হয় না, একে ম্যানুয়ালি করতে হয় (Explicitly)।
* **কেন ব্যবহার করা হয়:** Upcast করা কোনো অবজেক্টের চাইল্ড ক্লাসের নিজস্ব ইউনিক মেথড বা প্রোপার্টি (যা প্যারেন্ট ক্লাসে নেই) ব্যবহার করার জন্য।

### Downcasting Example:
```csharp
Animal myAnimal = new Dog(); // Upcast করা অবজেক্ট

// Downcasting (Explicit)
Dog myDog = (Dog)myAnimal; 
myDog.PlayFetch(); // সফলভাবে কাজ করবে। আউটপুট: Dog is playing fetch.
```

### 🚨 Downcasting এর ঝুঁকি ও সমাধান:
যদি আমরা এমন কোনো অবজেক্টকে ডাউনকাস্ট করার চেষ্টা করি যা আসলে ওই চাইল্ড ক্লাসের অবজেক্ট নয়, তবে রানটাইমে এরর আসবে (`ClassCastException` / `InvalidCastException`)।

```csharp
Animal catAnimal = new Cat(); // Cat ক্লাস আরেকটি চাইল্ড ক্লাস
Dog dog = (Dog)catAnimal; // Runtime Error! Cat-কে Dog এ কাস্ট করা যাবে না।
```

#### সমাধান (Safe Downcasting):
ডাউনকাস্ট করার আগে সবসময় অবজেক্টের সঠিক টাইপ চেক করে নেওয়া নিরাপদ।

**Java-তে সমাধান (`instanceof` ব্যবহার করে):**
```java
if (myAnimal instanceof Dog) {
    Dog myDog = (Dog) myAnimal;
    myDog.playFetch();
}
```

**C#-এ সমাধান (`is` অথবা `as` অপারেটর ব্যবহার করে):**
```csharp
// 'is' ব্যবহার করে:
if (myAnimal is Dog myDog) 
{
    myDog.PlayFetch();
}

// অথবা 'as' ব্যবহার করে:
Dog dog = myAnimal as Dog;
if (dog != null) 
{
    dog.PlayFetch();
}
```

---

## সংক্ষেপে পার্থক্য (Summary)

| বৈশিষ্ট্য | Upcasting | Downcasting |
| :--- | :--- | :--- |
| **দিক** | Child ➡️ Parent | Parent ➡️ Child |
| **কাস্টিং টাইপ** | Implicit (স্বয়ংক্রিয়) | Explicit (ম্যানুয়াল) |
| **নিরাপত্তা** | ১০০% নিরাপদ (সর্বদা সফল হয়) | ঝুঁকিপূর্ণ (টাইপ না মিললে রানটাইম ক্র্যাশ হতে পারে) |
| **উদ্দেশ্য** | পলিমরফিজম ও কোড জেনারেলাইজেশন | চাইল্ড ক্লাসের নিজস্ব মেথড অ্যাক্সেস করা |
