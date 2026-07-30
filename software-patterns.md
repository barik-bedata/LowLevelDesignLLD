# Software Architecture & Design Patterns Comprehensive Guide

Software Engineering-এ সকল প্রকার প্যাটার্নকে একত্রে **Software Architecture & Design Patterns** বা **Software Patterns** বলা হয়। সিস্টেমের পরিধি (Scope/Granularity) অনুযায়ী এগুলোকে প্রধানত ৪টি মূল ক্যাটাগরিতে বিভক্ত করা যায়।

---

## 📌 Categorization Overview (শ্রেণীবিভাগ এক নজরে)

| Category Level | Focus Area | Example Patterns |
| :--- | :--- | :--- |
| **1. System / Enterprise Architecture** | পুরো ডিস্ট্রিবিউটেড সিস্টেম ও সার্ভারের গঠন | Event-Driven Architecture, Microservices, Monolithic, CQRS |
| **2. Application / UI Architecture** | কোনো নির্দিষ্ট অ্যাপ্লিকেশনের হাই-লেভেল কোড স্ট্রাকচার | MVC, MVP, MVVM, Clean Architecture, Layered Architecture |
| **3. Data Access & Persistence** | ডাটাবেজ ও বিজনেস লজিকের মধ্যবর্তী লেয়ার | Repository Pattern, DAO, Unit of Work, Active Record |
| **4. GoF (Gang of Four) Design Patterns** | অবজেক্ট ও ক্লাসের মাইক্রো-লেভেল কোড সমাধান | Builder, Adapter, Singleton, Factory, Command, Observer |

---

## 1. System / Enterprise Architecture Patterns (ম্যাক্রো-লেভেল)
> **পরিধি:** পুরো ডিস্ট্রিবিউটেড সিস্টেম, ব্যাকএন্ড আর্কিটেকচার এবং সার্ভিসগুলোর মধ্যে ডেটা প্রবাহ নিয়ন্ত্রণ।

### 1.1 Event-Driven Architecture (EDA)
* **বর্ণনা:** সিস্টেমের উপাদানগুলো ঘটনার (Event) ওপর ভিত্তি করে কাজ করে। একটি উপাদান ইভেন্ট প্রকাশ করে (Producer) এবং অন্য উপাদান তা গ্রহণ করে (Consumer/Subscriber)।
* **ব্যবহারের স্থান:** Kafka, RabbitMQ, Real-time Notification System, Microservices communication.

### 1.2 Microservices Architecture
* **বর্ণনা:** একটি বড় অ্যাপ্লিকেশনকে অনেকগুলো ছোট, স্বাধীন ও স্বয়ংসম্পূর্ণ সেবায় (Services) বিভক্ত করা হয়।
* **সুবিধা:** স্বাধীন ডিপ্লয়মেন্ট, স্কেলেবিলিটি এবং ফল্ট আইসোলেশন।

### 1.3 Monolithic Architecture
* **বর্ণনা:** পুরো সিস্টেমের সমস্ত মডিউল, ইউআই, বিজনেজ লজিক এবং ডাটাবেজ কোড একটিমাত্র কোডবেসে রাখা হয়।

### 1.4 CQRS (Command Query Responsibility Segregation)
* **বর্ণনা:** সিস্টেমের ডেটা পড়া (Query / Read) এবং ডেটা পরিবর্তন করার (Command / Write) জন্য দুটি আলাদা মডেল ব্যবহার করা হয়।

---

## 2. Application / UI Architecture Patterns (মিডিয়াম-লেভেল)
> **পরিধি:** একটি নির্দিষ্ট অ্যাপ্লিকেশনের কোডবেসে UI, বিজনেস লজিক ও ডেটা ফ্লো আলাদা রাখার ফ্রেমওয়ার্ক।

### 2.1 MVP (Model-View-Presenter)
* **বর্ণনা:** UI (View) এবং Data (Model)-এর মধ্যে পূর্ণ যোগাযোগ রক্ষা করে Presenter। Presenter কোনো ফ্রেমওয়ার্ক-নির্ভর নয়, ফলে সহজে Unit Test করা যায়।
* **নোট:** এটি **GoF 23 Design Patterns**-এর অংশ নয়, এটি একটি **UI Architectural Pattern**।

### 2.2 MVC (Model-View-Controller)
* **বর্ণনা:** View ইউজারের ইনপুট Controller-কে পাঠায়, Controller Model আপডেট করে এবং View-কে রিফ্রেশ করে। (Web Backend / Ruby on Rails / ASP.NET)-এ বহুল ব্যবহৃত।

### 2.3 MVVM (Model-View-ViewModel)
* **বর্ণনা:** Data Binding-এর মাধ্যমে View এবং ViewModel স্বয়ংক্রিয়ভাবে সিঙ্ক থাকে (Android Jetpack / WPF / Vue.js-এ ব্যবহৃত)।

### 2.4 Clean Architecture / Hexagonal Architecture
* **বর্ণনা:** বিজনেস লজিককে (Core Domain) ফ্রেমওয়ার্ক, ডাটাবেজ এবং ইউআই থেকে সম্পূর্ণ স্বাধীন ও টেস্টেবল রাখার জন্য তৈরি আর্কিটেকচার।

---

## 3. Data Access & Persistence Patterns (ডেটা/ডোমেইন লেভেল)
> **পরিধি:** ডাটাবেজ অপারেশন ও কোডের বিজনেস লজিকের মধ্যে সেতুবন্ধন।

### 3.1 Repository Pattern
* **বর্ণনা:** ডেটা সোর্সকে (Database, API, Cache) একটি সাধারণ কালেকশনের মতো আবৃত করে রাখা। বিজনেস লজিক জানতেই পারে না ডেটা কোথায় থেকে আসছে।
* **সুবিধা:** ডাটাবেজ সহজে পরিবর্তনযোগ্য এবং Testing/Mocking করা সহজ।

### 3.2 Data Access Object (DAO) Pattern
* **বর্ণনা:** ডেটাবেজের সাথে সরাসরি CRUD (Create, Read, Update, Delete) কাজ সম্পন্ন করার মেথডসমূহ ধারণ করে।

### 3.3 Unit of Work Pattern
* **বর্ণনা:** একটি বিজনেস ট্রানজেকশনে একাধিক ডাটাবেজ পরিবর্তনকে একত্রিত করে একসাথে Commit বা Rollback নিশ্চিত করা।

---

## 4. GoF (Gang of Four) Design Patterns (মাইক্রো-লেভেল)
> **পরিধি:** ১৯৯৪ সালে প্রকাশিত 'Gang of Four' বইয়ের ২৩টি ক্লাসিক ডিজাইন প্যাটার্ন। এগুলো অবজেক্ট ও ক্লাস লেভেলের কোড সমস্যা দূর করে।

### 4.1 Creational Patterns (অবজেক্ট তৈরির প্যাটার্ন)
1. **Builder Pattern:** বাধ্যতামূলক (Fixed) এবং ঐচ্ছিক (Optional) প্রপার্টিসমূহ দিয়ে একটি জটিল অবজেক্ট ধাপে ধাপে তৈরি করে (Telescoping Constructor অ্যান্টি-প্যাটার্ন সমাধান করে)।
2. **Factory Method:** অবজেক্ট তৈরির দায়িত্ব সাব-ক্লাসের ওপর ছেড়ে দেওয়া।
3. **Abstract Factory:** সম্পর্কিত অবজেক্ট ফ্যামিলি তৈরি করার ইন্টারফেস।
4. **Singleton:** নিশ্চিত করে কোনো ক্লাসের একটিমাত্র ইনস্ট্যান্স থাকবে।
5. **Prototype:** বিদ্যমান অবজেক্ট ক্লোন করে নতুন অবজেক্ট তৈরি করা।

### 4.2 Structural Patterns (গঠনগত প্যাটার্ন)
1. **Adapter Pattern:** দুটি অসঙ্গতিপূর্ণ (Incompatible) ইন্টারফেসকে একসাথে কাজ করার সুযোগ দেওয়া।
2. **Decorator Pattern:** বিদ্যমান অবজেক্টের আচরণ ডাইনামিকালি এক্সটেন্ড বা বর্ধিত করা।
3. **Facade Pattern:** জটিল সাব-সিস্টেমের জন্য একটি সহজ ইন্টারফেস প্রদান করা।
4. **Proxy, Bridge, Composite, Flyweight.**

### 4.3 Behavioral Patterns (আচরণগত প্যাটার্ন)
1. **Observer Pattern:** এক-থেকে-অনেক (1-to-N) অবজেক্ট নির্ভরতা তৈরি করা, যেন কোনো পরিবর্তন হলে সাবস্ক্রাইবাররা নোটিফিকেশন পায়।
2. **Strategy Pattern:** রান-টাইমে الگোরিদম পরিবর্তন করার নমনীয়তা দেওয়া।
3. **Command Pattern:** কোনো রিকোয়েস্টকে স্ট্যান্ডঅ্যালোন অবজেক্ট হিসেবে আবৃত করা।
4. **State, Iterator, Mediator, Memento, Visitor, Chain of Responsibility, Interpreter, Template Method.**

---

## 💡 Important OOP & MCQ Quick Notes

* **Diamond Problem:** একাধিক ক্লাস (B & C) একটি বেস ক্লাস (A) কে ইনহেরিট করে ওভাররাইড করলে এবং ৪র্থ ক্লাস (D) উভয়কে ইনহেরিট করলে যে Ambiguity সৃষ্টি হয়। সমাধান: C++ Scope Resolution বা Interfaces (Java)।
* **Polymorphism Types in C++:** প্রধানত **২ প্রকার** —
  1. Compile-time (Function & Operator Overloading)
  2. Run-time (Function Overriding / Virtual Functions)
* **Upcasting:** Child ➔ Parent রূপান্তর। এটি **১০০% Safe** এবং Implicit (কারণ Parent-এর সব প্রপার্টি Child-এ থাকেই)।
