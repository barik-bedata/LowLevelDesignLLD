# Private Class

অবজেক্ট-ওরিয়েন্টিড প্রোগ্রামিং (OOP) এ **Private Class** হলো এমন একটি ক্লাস যার অ্যাক্সেসিবিলিটি শুধুমাত্র তার প্যারেন্ট বা আউটার (Outer) ক্লাসের ভেতরেই সীমাবদ্ধ থাকে। 

সাধারণত Java বা C# এর মতো প্রোগ্রামিং ল্যাঙ্গুয়েজে সরাসরি কোনো ফাইলের ভেতরে বা টপ-লেভেলে (Top-level) কোনো ক্লাসকে `private` করা যায় না। তবে একটি ক্লাসের ভেতরে অন্য আরেকটি ক্লাস ডিক্লেয়ার করলে (যাকে **Nested Class** বা **Inner Class** বলা হয়), সেটিকে `private` করা সম্ভব।

---

## কিভাবে ডিক্লেয়ার করা হয়? (Syntax & Examples)

### C# Example:
```csharp
public class Car 
{
    // Private Nested Class
    private class Engine 
    {
        public void Start() 
        {
            Console.WriteLine("Engine started...");
        }
    }

    private Engine _engine;

    public Car() 
    {
        _engine = new Engine(); // শুধুমাত্র Car ক্লাসই Engine ক্লাসটি ব্যবহার করতে পারবে
    }

    public void Drive() 
    {
        _engine.Start();
        Console.WriteLine("Car is moving...");
    }
}
```

### Java Example:
```java
public class LinkedList {
    // Private Nested Class
    private class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node head;

    public void add(int value) {
        Node newNode = new Node(value);
        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
    }
}
```

---

## Private Class এর সুবিধাসমূহ (Advantages)

1. **উন্নত এনক্যাপসুলেশন (Enhanced Encapsulation):**
   যে ক্লাস বা লজিকটি বাইরের অন্যান্য ক্লাসের জানার প্রয়োজন নেই, সেটিকে সম্পূর্ণরূপে লুকিয়ে ফেলা যায় (Information Hiding)।
2. **কোড মেইনটেইনেবিলিটি (Better Maintainability):**
   যেহেতু ক্লাসটি নির্দিষ্ট একটি ক্লাসের বাইরে ব্যবহার করা যায় না, তাই এই ক্লাসে কোনো পরিবর্তন আনলে বাইরের অন্যান্য কোডে কোনো প্রভাব পড়ে না।
3. **লজিক্যাল গ্রুপিং (Logical Grouping):**
   যদি কোনো ক্লাস শুধুমাত্র অন্য একটি ক্লাসের কাজের সহায়তার জন্য প্রয়োজন হয়, তবে সেটিকে আলাদা ফাইলে না লিখে একই ফাইলের ভেতরে Nested Private Class হিসেবে রাখা পরিষ্কার কোড স্ট্রাকচার তৈরি করে।

---

## বাস্তবমুখী ব্যবহার (Real-world Use Cases)

* **ডাটা স্ট্রাকচারের নোড (Data Structure Nodes):**
  `LinkedList`, `Tree` বা `Graph` ডিক্লেয়ার করার সময় তাদের ভেতরের `Node` বা `Vertex` ক্লাসকে `private` রাখা হয়, কারণ বাইরের ক্লাসের সরাসরি নোড অ্যাক্সেস করার প্রয়োজন নেই।
* **হেল্পার ক্লাস (Helper / Utility Classes):**
  ধরা যাক, একটি ক্লাসের কাজ সম্পন্ন করার জন্য একটি নির্দিষ্ট ফরম্যাটার বা ডাটা কনভার্টার ক্লাসের প্রয়োজন যা অন্য কোথাও লাগবে না। সেক্ষেত্রে Private Class বেশ উপযোগী।
* **স্টেট প্যাটার্ন বা ইন্টারনাল ওয়ার্কার (Internal Worker / States):**
  কোনো অ্যাপ্লিকেশনের অভ্যন্তরীণ ব্যাকগ্রাউন্ড প্রসেস বা কোনো অবজেক্টের স্টেট পরিবর্তনের লজিক বাইরের অ্যাপ থেকে আড়াল রাখতে এটি ব্যবহার করা হয়।
