# Template Method Design Pattern

## 📖 Overview
The **Template Method Design Pattern** is a behavioral design pattern that defines the overall structure (skeleton) of an algorithm in a base class. It allows subclasses to redefine or customize specific steps of the algorithm without changing its core structure.

---

## 🤔 Is this even a Design Pattern?
**"This just looks like basic Inheritance and Method Overriding!"**

Yes, you are absolutely right! Today, what we consider "basic OOP knowledge" was documented as the *Template Method Pattern* in the 1990s by the Gang of Four (GoF). Before modern OOP became a standard, organizing code with a fixed skeleton and variable steps was a major architectural breakthrough.

### 🎬 The Hollywood Principle
The true magic of this pattern lies in the **"Hollywood Principle": *Don't call us, we'll call you.***
Instead of the subclass calling the parent class, the Parent (Base) class calls the Subclass at the exact right moment.

This is the exact mechanism that powers almost all modern **Frameworks** (like ASP.NET, React, Android SDK). The framework writes the giant "Template Method" and calls your custom overridden methods (like `OnInit`, `Page_Load`, `onCreate`) when needed!

---

## 🧱 Components (4 Key Elements)

1. **Abstract Class**
   - Defines the template method (algorithm skeleton) with some steps implemented and others left abstract or as hooks for customization.
2. **Template Method**
   - Outlines the algorithm's fixed structure by calling steps in order.
   - In C#, this is kept non-virtual (equivalent to `final` in Java) to prevent changes to the skeleton sequence.
3. **Abstract/Hook Methods**
   - Placeholder methods in the abstract class that subclasses *must* implement or *optionally* override.
4. **Concrete Subclasses**
   - Provide implementations for abstract methods, customizing specific steps while preserving the overall algorithm.

---

## 🧠 সহজ বাংলায় বোঝা (Simple Bengali Explanation)

### সমস্যাটা কী ছিল?

ধরো তুমি ৩ ধরনের Report বানাও:

```
PDF Report:
  1. Data collect করো       ← same সবার জন্য
  2. PDF format এ সাজাও    ← আলাদা
  3. PDF file save করো      ← আলাদা
  4. Email পাঠাও            ← same সবার জন্য

Excel Report:
  1. Data collect করো       ← same
  2. Excel format এ সাজাও  ← আলাদা
  3. Excel file save করো    ← আলাদা
  4. Email পাঠাও            ← same

সমস্যা:
Step 1 আর Step 4 বারবার copy-paste হচ্ছে ❌
→ Code Duplication বাড়ছে
→ একটা change = সব জায়গায় change করতে হয়
```

### Template Method এর সমাধান:

```
"Common steps গুলো Parent class এ লিখে রাখো
 Different steps গুলো Child class override করুক"

Parent class = Template (কাঠামো ঠিক করে)
Child class  = Details (নিজের মতো করে)
```

---

## 🏗️ Structure / Flow

```
generateReport() call হলো
        ↓
┌───────────────┐
│ collectData() │ ← Parent এর code চলে (same সবার)
└───────┬───────┘
        ↓
┌───────────────┐
│ formatData()  │ ← Child এর code চলে (আলাদা আলাদা)
└───────┬───────┘
        ↓
┌───────────────┐
│  saveFile()   │ ← Child এর code চলে (আলাদা আলাদা)
└───────┬───────┘
        ↓
┌───────────────┐
│  sendEmail()  │ ← Parent এর code চলে (same সবার)
└───────────────┘
```

```
┌─────────────────────────────────────┐
│         Abstract Class              │
│      (Template ধরে রাখে)            │
│                                     │
│  + generateReport()  ← TEMPLATE     │
│    {                                │
│      collectData()   ← same         │
│      formatData()    ← abstract ↓   │
│      saveFile()      ← abstract ↓   │
│      sendEmail()     ← same         │
│    }                                │
└──────────────┬──────────────────────┘
               │
    ┌──────────┼──────────┐
    ↓          ↓          ↓
┌───────┐  ┌───────┐  ┌───────┐
│  PDF  │  │ Excel │  │ HTML  │
│Report │  │Report │  │Report │
│       │  │       │  │       │
│format │  │format │  │format │
│save   │  │save   │  │save   │
└───────┘  └───────┘  └───────┘
নিজেদের মতো implement করে
```

---

## 💻 Java Code Example (Report Generator)

### Step 1: Abstract Parent Class (Template)

```java
// Abstract class = Template
abstract class ReportGenerator {

    // ✅ TEMPLATE METHOD — final মানে কেউ override করতে পারবে না
    // Sequence সবসময় fixed থাকবে
    public final void generateReport() {
        collectData();   // same সবার জন্য
        formatData();    // আলাদা আলাদা → child করবে
        saveFile();      // আলাদা আলাদা → child করবে
        sendEmail();     // same সবার জন্য
    }

    // ✅ Common steps — এখানেই implemented (সবার জন্য same)
    private void collectData() {
        System.out.println("Database থেকে data collect করা হলো");
    }

    private void sendEmail() {
        System.out.println("Email পাঠানো হলো ✉️");
    }

    // ❌ Different steps — child class implement করবে
    protected abstract void formatData();
    protected abstract void saveFile();
}
```

### Step 2: Concrete Child Classes

```java
// PDF Report — নিজের মতো implement করে
class PDFReport extends ReportGenerator {

    @Override
    protected void formatData() {
        System.out.println("Data কে PDF format এ সাজানো হলো 📄");
    }

    @Override
    protected void saveFile() {
        System.out.println("report.pdf হিসেবে save হলো 💾");
    }
}

// Excel Report — নিজের মতো implement করে
class ExcelReport extends ReportGenerator {

    @Override
    protected void formatData() {
        System.out.println("Data কে Excel format এ সাজানো হলো 📊");
    }

    @Override
    protected void saveFile() {
        System.out.println("report.xlsx হিসেবে save হলো 💾");
    }
}

// HTML Report — নিজের মতো implement করে
class HTMLReport extends ReportGenerator {

    @Override
    protected void formatData() {
        System.out.println("Data কে HTML format এ সাজানো হলো 🌐");
    }

    @Override
    protected void saveFile() {
        System.out.println("report.html হিসেবে save হলো 💾");
    }
}
```

### Step 3: Main — Use করো

```java
public class Main {
    public static void main(String[] args) {

        System.out.println("=== PDF Report ===");
        ReportGenerator pdf = new PDFReport();
        pdf.generateReport();

        System.out.println("\n=== Excel Report ===");
        ReportGenerator excel = new ExcelReport();
        excel.generateReport();

        System.out.println("\n=== HTML Report ===");
        ReportGenerator html = new HTMLReport();
        html.generateReport();
    }
}
```

### Output:
```
=== PDF Report ===
Database থেকে data collect করা হলো
Data কে PDF format এ সাজানো হলো 📄
report.pdf হিসেবে save হলো 💾
Email পাঠানো হলো ✉️

=== Excel Report ===
Database থেকে data collect করা হলো
Data কে Excel format এ সাজানো হলো 📊
report.xlsx হিসেবে save হলো 💾
Email পাঠানো হলো ✉️

=== HTML Report ===
Database থেকে data collect করা হলো
Data কে HTML format এ সাজানো হলো 🌐
report.html হিসেবে save হলো 💾
Email পাঠানো হলো ✉️
```

---

## 🌍 Real Life Examples যেখানে Template Method আছে

```
1. ☕ Coffee/Tea বানানো:
   boilWater()      → same (সবার জন্য)
   brew()           → আলাদা (Coffee vs Tea)
   pourInCup()      → same (সবার জন্য)
   addCondiments()  → আলাদা (sugar vs milk)

2. 🎮 Game এর Flow:
   initialize()     → same
   startPlay()      → আলাদা (Chess vs Cricket)
   endPlay()        → same

3. 🏦 Bank Transaction:
   validateUser()    → same
   processPayment()  → আলাদা (Card vs Mobile Banking)
   generateReceipt() → same

4. 🏗️ CI/CD Pipeline:
   lintCode()        → same
   compile()         → আলাদা (Android vs iOS)
   runTests()        → same
   deploy()          → আলাদা
```

---

## ✅ কেন ব্যবহার করবো? (Benefits)

| সমস্যা (আগে) | সমাধান (Template Method দিয়ে) |
|-------------|-------------------------------|
| Code Duplication | Common code একবারই লেখা |
| Step miss হওয়ার ভয় | Sequence fixed, কেউ miss করতে পারবে না |
| নতুন type যোগ কঠিন | নতুন class বানাও, শুধু আলাদা steps লিখো |
| Change করতে সব জায়গায় যেতে হয় | Parent এ একবার change = সবার জন্য apply |

---

## ⚠️ কখন ব্যবহার করবো না?

```
❌ যদি steps এর সংখ্যা বা sequence ঘন ঘন বদলায়
❌ যদি subclass গুলো খুব বেশি আলাদা হয়
   (তখন Strategy Pattern ভালো)
❌ যদি শুধু ১টাই implementation থাকে
   (তখন Template দরকার নেই)
```

---

## 🔄 Template Method vs Strategy Pattern

| বিষয় | Template Method | Strategy Pattern |
|------|----------------|-----------------|
| কীভাবে? | Inheritance (extends) | Composition (has-a) |
| Algorithm | Partially fixed | পুরোটাই বদলানো যায় |
| Flexibility | কম | বেশি |
| কখন? | Steps same, কিছু আলাদা | পুরো algorithm আলাদা |

---

## 🧠 মনে রাখার Trick

```
Template Method = রান্নার Recipe 📖

Recipe বলে:
  Step 1: উপকরণ নাও     (fixed — সবার জন্য)
  Step 2: রান্না করো    (তোমার মতো — আলাদা)
  Step 3: পরিবেশন করো   (fixed — সবার জন্য)

Recipe বদলায় না, কিন্তু Step 2 তে:
  কেউ ভাত রাঁধে 🍚
  কেউ বিরিয়ানি রাঁধে 🍖
  কেউ খিচুড়ি রাঁধে 🥘

এটাই Template Method! 🎯
```

---

## 💻 6 Practical C# Examples (এই Folder এ)

এই folder এ **6টি Real-Life C# Example** আছে:

| File | Scenario | Template Sequence |
|------|----------|-------------------|
| `BeverageMakerExample.cs` | Tea & Coffee বানানো | Boil → Brew → Pour → Condiments |
| `DataMinerExample.cs` | PDF & CSV parsing | Open → Extract → Parse → Save → Close |
| `SoftwareBuilderExample.cs` | CI/CD Pipeline | Lint → Compile → Test → Deploy |
| `GameAIExample.cs` | Game AI (Orcs vs Elves) | Resources → Build → Units → Attack |
| `ReportGeneratorExample.cs` | HTML & PDF Reports | Header → Body → Footer |
| `DatabaseQueryRunnerExample.cs` | SQL & MongoDB Query | Connect → Run → Disconnect |

---

*Pattern Category: **Behavioural Design Pattern***
*Also known as: Template, Template Method*
*GoF Book: Design Patterns — Elements of Reusable Object-Oriented Software (1994)*
