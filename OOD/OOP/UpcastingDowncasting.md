# Upcasting and Downcasting in C#

আপনার রিকোয়ারমেন্ট অনুযায়ী C# এ সম্পূর্ণ কোড এবং বিস্তারিত ব্যাখ্যা (কমেন্টস সহ) নিচে দেওয়া হলো:

```csharp
using System;

// ১. Parent Class
public class Animal
{
    public void Eat()
    {
        Console.WriteLine("Animal is eating.");
    }
}

// ২. Child Class
public class Dog : Animal
{
    public void Bark()
    {
        Console.WriteLine("Dog is barking.");
    }
}

class Program
{
    static void Main(string[] args)
    {
        // ==========================================
        // UPCASTING
        // ==========================================
        
        // "A child is a parent, but parent is not a child" - Global Rule:
        // এর মানে হলো, একটা Dog সবসময়ই একটা Animal (Child is a parent)। 
        // তাই Dog-এর অবজেক্টকে Animal-এর রেফারেন্সে রাখা সম্পূর্ণ সেইফ এবং লজিক্যাল।
        // কিন্তু সব Animal তো Dog না (যেমন Cat, Cow হতে পারে), তাই Parent is not a child.
        
        Animal animRef1 = new Dog(); // Upcasting (Implicit)
        
        // ---------------------------------------------------------
        // Memory Level & Visibility (Upcasting):
        // ---------------------------------------------------------
        // Heap Memory: [ Eat() | Bark() ] -> মেমোরিতে পুরো Dog অবজেক্ট তৈরি হয়েছে।
        // Stack Reference: animRef1 (Type: Animal)
        // 
        // Visibility: 
        // animRef1 রেফারেন্সটি Animal টাইপের। 
        // তাই মেমোরিতে পুরো Dog অবজেক্ট থাকলেও, animRef1 শুধুমাত্র Animal এর অংশটুকুই (Eat) দেখতে পাবে। 
        // Bark() মেমোরিতে আছে ঠিকই, কিন্তু animRef1 এর কাছে তা Invisible (অদৃশ্য)।
        // ---------------------------------------------------------
        
        animRef1.Eat(); // Valid
        // animRef1.Bark(); // Invalid! Compile time error. animRef1 Bark() কে চিনে না।


        // ==========================================
        // DOWNCASTING
        // ==========================================
        
        Dog realDog = (Dog)animRef1; // Downcasting (Explicit)
        
        // ---------------------------------------------------------
        // Memory Level & Visibility (Downcasting):
        // ---------------------------------------------------------
        // Heap Memory: [ Eat() | Bark() ] -> মেমোরিতে সেই একই Dog অবজেক্টটিই আছে।
        // Stack Reference: realDog (Type: Dog)
        // 
        // Visibility: 
        // এখন realDog রেফারেন্সটি Dog টাইপের, তাই তার লেন্স বড় হয়ে গেছে! 
        // সে এখন মেমোরির পুরো অবজেক্টটাই দেখতে পাবে। Eat() এবং Bark() দুটোই তার কাছে Visible।
        // ---------------------------------------------------------
        
        realDog.Eat();  // Valid
        realDog.Bark(); // Valid


        // ==========================================
        // (Obj) Casting vs 'as' Keyword (Difference)
        // ==========================================
        
        // ১. Direct Casting `(Dog)animRef1`:
        // - এটা জোর করে টাইপ কাস্ট করে।
        // - যদি কাস্টিং ফেইল করে (ধরেন animRef1 এর ভেতর আসলে Cat এর অবজেক্ট আছে), 
        //   তাহলে সাথে সাথে Runtime Error (InvalidCastException) থ্রো করবে এবং প্রোগ্রাম ক্র্যাশ করবে।

        // ২. 'as' Keyword `animRef1 as Dog`:
        // - এটা সাবধানে কাস্ট করার চেষ্টা করে (Safe Casting)। 
        // - যদি কাস্টিং ফেইল করে, তাহলে এক্সেপশন থ্রো না করে null রিটার্ন করে। 
        // - এতে প্রোগ্রাম ক্র্যাশ করে না, আমরা null চেক করে সেফলি কাজ করতে পারি।


        // ==========================================
        // EXCEPTION CASE (Why this throws error?)
        // ==========================================
        
        /*
        Animal a = new Animal();
        Dog d = (Dog) a; // InvalidCastException (Runtime Error)
        
        ---------------------------------------------------------
        Memory Level Explanation (কেন এক্সেপশন দেয়?):
        ---------------------------------------------------------
        ১. "new Animal()" মেমোরিতে শুধুমাত্র [ Eat() ] তৈরি করে। এখানে Bark() এর কোনো অস্তিত্বই নেই।
        ২. "a" রেফারেন্স এই [ Eat() ] কে পয়েন্ট করে আছে।
        ৩. এখন আমরা যখন "Dog d = (Dog) a;" করছি, আমরা কম্পাইলারকে জোর করে বলছি, 
           "তুমি a কে Dog হিসেবে কাস্ট করো।" 
        ৪. কম্পাইলার আমাদের কথা শুনে Compile time এ কোনো error দেয় না। 
        ৫. কিন্তু রানটাইমে যখন "d" রেফারেন্স মেমোরির কাছে গিয়ে Bark() কে খুঁজতে যায়, 
           তখন সে দেখে সেখানে Bark() নেই! কারণ মেমোরিতে তো শুধুমাত্র Animal তৈরি হয়েছিল। 
           
        যেহেতু মেমোরিতে Dog এর বৈশিষ্ট্যগুলো নেই, তাই একটা Animal কে জোর করে Dog বানানো সম্ভব না। 
        এজন্যই প্রোগ্রাম রানটাইমে InvalidCastException থ্রো করে। 
        এটাই প্রমান করে যে: "Parent is not a child" (Animal কে Dog বানানো যায় না)।
        */
    }
}
```
