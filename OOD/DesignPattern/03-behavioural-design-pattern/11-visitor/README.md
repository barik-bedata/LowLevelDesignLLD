# Visitor Design Pattern

## 📖 Overview
The **Visitor Design Pattern** is a behavioral design pattern that allows you to add new operations to existing classes without modifying them. It separates the algorithm from the objects on which it operates, heavily utilizing a technique called **Double Dispatch**.

---

## 🏘️ গল্পে গল্পে Visitor Pattern (The Story)
ধরুন একটি পাড়ায় ৩টি ভিন্ন ভিন্ন বাড়ি আছে: **কাঠের বাড়ি, ইটের বাড়ি, এবং মাটির বাড়ি**।
এখন একদিন ওই পাড়ায় একজন **ইন্স্যুরেন্স এজেন্ট (Visitor)** আসলো। তার কাজ হলো প্রতিটি বাড়ির জন্য ইন্স্যুরেন্স প্রিমিয়াম হিসাব করা।

এখন, "ইন্স্যুরেন্স কীভাবে হিসাব করতে হবে"—এই লজিক কি বাড়ির ভেতরে লেখা থাকা উচিত? কখনোই না! কারণ বাড়ির কাজ হলো শুধু মানুষকে আশ্রয় দেওয়া (Single Responsibility Principle).

তাই Visitor Pattern বলে:
- বাড়ির দরজায় শুধু একটি মেথড রাখো: `Accept(Visitor)`.
- ইন্স্যুরেন্স এজেন্ট (Visitor) যখন দরজায় কড়া নাড়বে, বাড়িওয়ালা শুধু দরজা খুলে বলবে, "Welcome! ভেতরে আসুন!" (`visitor.Visit(this)`).
- এরপর এজেন্ট ঘরের ভেতরে ঢুকে দেখবে এটা কাঠের বাড়ি নাকি ইটের বাড়ি, এবং সেই অনুযায়ী সে নিজের খাতায় হিসাব করবে।

ভবিষ্যতে যদি ইন্স্যুরেন্স এজেন্টের বদলে একজন **Tax Collector (ট্যাক্স অফিসার)** আসে, তবে বাড়ির কোনো কোড চেঞ্জ করতে হবে না! ট্যাক্স অফিসারও একই দরজা দিয়ে ঢুকবে এবং নিজের মতো ট্যাক্স হিসাব করবে।

---

## 🧠 সহজ বাংলায় — সমস্যা ও সমাধান

### সমস্যাটা কী?

```
ধরো তোমার কাছে ৩ ধরনের Product আছে:
  📚 Book, 💻 Electronics, 👕 Clothing

এখন ৩টা কাজ করতে হবে:
  1. Discount calculate করো
  2. Shipping cost calculate করো
  3. Tax calculate করো

Without Visitor (ভুল পথ):
class Book {
    CalculateDiscount() { ... }  ← Book class এ
    CalculateShipping() { ... }  ← Book class এ ভরা হয়ে যায়
    CalculateTax()      { ... }  ← নতুন কাজ = সব class বদলাও ❌
}

সমস্যা:
→ নতুন কাজ যোগ হলে প্রতিটা class বদলাতে হয় ❌
→ Open/Closed Principle ভাঙে ❌
→ Class এ method ভরে যায় ❌
```

### Visitor Pattern এর সমাধান:

```
"কাজগুলো আলাদা Visitor class এ নিয়ে যাও।
 Product class শুধু Accept() করুক।
 নতুন কাজ = নতুন Visitor class — Product touch করো না।"

আগে:                       পরে:
Book {                      Book   { Accept(visitor) }
  CalculateDiscount()       Electronics { Accept(visitor) }
  CalculateShipping() →     Clothing { Accept(visitor) }
  CalculateTax()
}                           DiscountVisitor  { Visit(Book), Visit(Electronics)... }
                            ShippingVisitor  { Visit(Book), Visit(Electronics)... }
                            TaxVisitor       { Visit(Book), Visit(Electronics)... }

Product class বদলায় না! নতুন কাজ = নতুন Visitor ✅
```

---

## 🔑 Double Dispatch — এটাই Visitor এর আসল Magic

```
সাধারণ call (Single Dispatch):
  product.CalculateDiscount()
  → শুধু product এর type জানা যায়

Visitor call (Double Dispatch):
  product.Accept(visitor)         ← Step 1: Product কে বলো
  → ভেতরে: visitor.Visit(this)   ← Step 2: Visitor কে বলো

দুইটা dispatch হয়!
  1. কোন Product? (Book / Electronics / Clothing)
  2. কোন Visitor? (Discount / Shipping / Tax)

এই দুটো মিলিয়ে → সঠিক method চলে ✅
```

---

## 🧱 5 Key Components

1. **Visitor Interface (`IShoppingVisitor`)**
   - ডিক্লেয়ার করে কোন কোন element কে visit করা যাবে
   - প্রতিটা Element type এর জন্য একটা `Visit()` method

2. **Concrete Visitors (`DiscountVisitor`, `ShippingVisitor`, `TaxVisitor`)**
   - আসল business logic এখানে থাকে
   - প্রতিটা নতুন operation = একটা নতুন Visitor class

3. **Element Interface (`IProduct`)**
   - সব Element এর common interface
   - একটাই কাজ → `Accept(visitor)` করা

4. **Concrete Elements (`Book`, `Electronics`, `Clothing`)**
   - Real objects, কিন্তু operation জানে না
   - `Accept()` এ শুধু `visitor.Visit(this)` লেখা

5. **Client (`List<IProduct>`)**
   - Elements এর collection তৈরি করে
   - Visitor পাঠিয়ে operation চালায়

---

## 🏗️ Structure Diagram

```
┌──────────────────────────────────┐
│    IShoppingVisitor (Interface)  │
│  + Visit(Book book)              │
│  + Visit(Electronics elec)       │
│  + Visit(Clothing clothing)      │
└────────────┬─────────────────────┘
             │ implements
    ┌─────────┼──────────────┐
    ↓         ↓              ↓
┌──────────┐ ┌──────────┐ ┌──────────┐
│ Discount │ │ Shipping │ │   Tax    │
│ Visitor  │ │ Visitor  │ │ Visitor  │
└──────────┘ └──────────┘ └──────────┘

┌──────────────────────────────────┐
│      IProduct (Interface)        │
│  + Accept(IShoppingVisitor)      │
└────────────┬─────────────────────┘
             │ implements
   ┌──────────┼──────────┐
   ↓          ↓          ↓
┌──────┐ ┌─────────────┐ ┌─────────┐
│ Book │ │ Electronics │ │Clothing │
└──────┘ └─────────────┘ └─────────┘
  প্রতিটা Accept() এ visitor.Visit(this) করে
```

---

## 💻 Full C# Code — Shopping Cart Example

### Component 1: Visitor Interface

```csharp
public interface IShoppingVisitor
{
    void Visit(Book book);
    void Visit(Electronics electronics);
    void Visit(Clothing clothing);
}
```

### Component 2: Element Interface

```csharp
public interface IProduct
{
    string Name { get; }
    double Price { get; }
    void Accept(IShoppingVisitor visitor);
}
```

### Component 3: Concrete Elements

```csharp
// 📚 Book
public class Book : IProduct
{
    public string Name { get; set; }
    public double Price { get; set; }
    public string Author { get; set; }

    public Book(string name, string author, double price)
    {
        Name = name;
        Author = author;
        Price = price;
    }

    public void Accept(IShoppingVisitor visitor)
    {
        // "আমি Book, তুমি আমাকে handle করো"
        visitor.Visit(this);
    }
}

// 💻 Electronics
public class Electronics : IProduct
{
    public string Name { get; set; }
    public double Price { get; set; }
    public double WeightKg { get; set; }

    public Electronics(string name, double price, double weightKg)
    {
        Name = name;
        Price = price;
        WeightKg = weightKg;
    }

    public void Accept(IShoppingVisitor visitor)
    {
        // "আমি Electronics, তুমি আমাকে handle করো"
        visitor.Visit(this);
    }
}

// 👕 Clothing
public class Clothing : IProduct
{
    public string Name { get; set; }
    public double Price { get; set; }
    public string Size { get; set; }

    public Clothing(string name, double price, string size)
    {
        Name = name;
        Price = price;
        Size = size;
    }

    public void Accept(IShoppingVisitor visitor)
    {
        // "আমি Clothing, তুমি আমাকে handle করো"
        visitor.Visit(this);
    }
}
```

### Component 4: Concrete Visitors

```csharp
// ✅ Visitor 1: Discount Calculate করো
public class DiscountVisitor : IShoppingVisitor
{
    public double TotalDiscount { get; private set; } = 0;

    public void Visit(Book book)
    {
        double discount = book.Price * 0.20; // Book এ 20% discount
        TotalDiscount += discount;
        Console.WriteLine($"📚 {book.Name}");
        Console.WriteLine($"   Original Price : ৳{book.Price:N0}");
        Console.WriteLine($"   Discount (20%) : ৳{discount:N0}");
        Console.WriteLine($"   Final Price    : ৳{book.Price - discount:N0}");
    }

    public void Visit(Electronics electronics)
    {
        double discount = electronics.Price * 0.10; // Electronics এ 10% discount
        TotalDiscount += discount;
        Console.WriteLine($"💻 {electronics.Name}");
        Console.WriteLine($"   Original Price : ৳{electronics.Price:N0}");
        Console.WriteLine($"   Discount (10%) : ৳{discount:N0}");
        Console.WriteLine($"   Final Price    : ৳{electronics.Price - discount:N0}");
    }

    public void Visit(Clothing clothing)
    {
        double discount = clothing.Price * 0.30; // Clothing এ 30% discount
        TotalDiscount += discount;
        Console.WriteLine($"👕 {clothing.Name}");
        Console.WriteLine($"   Original Price : ৳{clothing.Price:N0}");
        Console.WriteLine($"   Discount (30%) : ৳{discount:N0}");
        Console.WriteLine($"   Final Price    : ৳{clothing.Price - discount:N0}");
    }
}

// ✅ Visitor 2: Shipping Cost Calculate করো
public class ShippingVisitor : IShoppingVisitor
{
    public double TotalShipping { get; private set; } = 0;

    public void Visit(Book book)
    {
        double shipping = 30; // Book এ flat ৳30
        TotalShipping += shipping;
        Console.WriteLine($"📚 {book.Name}");
        Console.WriteLine($"   Shipping : ৳{shipping} (Flat rate)");
    }

    public void Visit(Electronics electronics)
    {
        double shipping = electronics.WeightKg * 100; // ৳100 per kg
        TotalShipping += shipping;
        Console.WriteLine($"💻 {electronics.Name}");
        Console.WriteLine($"   Weight   : {electronics.WeightKg}kg");
        Console.WriteLine($"   Shipping : ৳{shipping} (৳100/kg)");
    }

    public void Visit(Clothing clothing)
    {
        double shipping = 50; // Clothing এ flat ৳50
        TotalShipping += shipping;
        Console.WriteLine($"👕 {clothing.Name} (Size: {clothing.Size})");
        Console.WriteLine($"   Shipping : ৳{shipping} (Flat rate)");
    }
}

// ✅ Visitor 3: Tax Calculate করো
public class TaxVisitor : IShoppingVisitor
{
    public double TotalTax { get; private set; } = 0;

    public void Visit(Book book)
    {
        // Book এ কোনো Tax নেই (Education)
        Console.WriteLine($"📚 {book.Name}");
        Console.WriteLine($"   Tax : ৳0 (Books are tax-free ✅)");
    }

    public void Visit(Electronics electronics)
    {
        double tax = electronics.Price * 0.15; // Electronics এ 15% VAT
        TotalTax += tax;
        Console.WriteLine($"💻 {electronics.Name}");
        Console.WriteLine($"   VAT (15%) : ৳{tax:N0}");
    }

    public void Visit(Clothing clothing)
    {
        double tax = clothing.Price * 0.075; // Clothing এ 7.5% Tax
        TotalTax += tax;
        Console.WriteLine($"👕 {clothing.Name}");
        Console.WriteLine($"   Tax (7.5%) : ৳{tax:N0}");
    }
}
```

### Component 5: Client (Main)

```csharp
using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        // Shopping Cart এ Products যোগ করো
        var cart = new List<IProduct>
        {
            new Book("Clean Code", "Robert Martin", 800),
            new Electronics("Samsung Galaxy", 45_000, 0.2),
            new Clothing("Cotton T-Shirt", 1_200, "L"),
            new Book("Design Patterns", "GoF", 1_200),
            new Electronics("MacBook Pro", 1_50_000, 2.1)
        };

        // Visitor 1: Discount
        Console.WriteLine("==========================================");
        Console.WriteLine("   🏷️  Discount Calculation");
        Console.WriteLine("==========================================");
        var discountVisitor = new DiscountVisitor();
        foreach (var product in cart)
        {
            product.Accept(discountVisitor);
            Console.WriteLine();
        }
        Console.WriteLine($"💰 Total Discount Saved: ৳{discountVisitor.TotalDiscount:N0}");

        // Visitor 2: Shipping
        Console.WriteLine("\n==========================================");
        Console.WriteLine("   🚚 Shipping Cost Calculation");
        Console.WriteLine("==========================================");
        var shippingVisitor = new ShippingVisitor();
        foreach (var product in cart)
        {
            product.Accept(shippingVisitor);
            Console.WriteLine();
        }
        Console.WriteLine($"📦 Total Shipping Cost: ৳{shippingVisitor.TotalShipping:N0}");

        // Visitor 3: Tax
        Console.WriteLine("\n==========================================");
        Console.WriteLine("   🧾 Tax Calculation");
        Console.WriteLine("==========================================");
        var taxVisitor = new TaxVisitor();
        foreach (var product in cart)
        {
            product.Accept(taxVisitor);
            Console.WriteLine();
        }
        Console.WriteLine($"🏛️  Total Tax: ৳{taxVisitor.TotalTax:N0}");
    }
}
```

### ✅ Output

```
==========================================
   🏷️  Discount Calculation
==========================================
📚 Clean Code
   Original Price : ৳800
   Discount (20%) : ৳160
   Final Price    : ৳640

💻 Samsung Galaxy
   Original Price : ৳45,000
   Discount (10%) : ৳4,500
   Final Price    : ৳40,500

👕 Cotton T-Shirt
   Original Price : ৳1,200
   Discount (30%) : ৳360
   Final Price    : ৳840

📚 Design Patterns
   Original Price : ৳1,200
   Discount (20%) : ৳240
   Final Price    : ৳960

💻 MacBook Pro
   Original Price : ৳1,50,000
   Discount (10%) : ৳15,000
   Final Price    : ৳1,35,000

💰 Total Discount Saved: ৳20,260

==========================================
   🚚 Shipping Cost Calculation
==========================================
📚 Clean Code
   Shipping : ৳30 (Flat rate)

💻 Samsung Galaxy
   Weight   : 0.2kg
   Shipping : ৳20 (৳100/kg)

👕 Cotton T-Shirt (Size: L)
   Shipping : ৳50 (Flat rate)

📚 Design Patterns
   Shipping : ৳30 (Flat rate)

💻 MacBook Pro
   Weight   : 2.1kg
   Shipping : ৳210 (৳100/kg)

📦 Total Shipping Cost: ৳340

==========================================
   🧾 Tax Calculation
==========================================
📚 Clean Code
   Tax : ৳0 (Books are tax-free ✅)

💻 Samsung Galaxy
   VAT (15%) : ৳6,750

👕 Cotton T-Shirt
   Tax (7.5%) : ৳90

📚 Design Patterns
   Tax : ৳0 (Books are tax-free ✅)

💻 MacBook Pro
   VAT (15%) : ৳22,500

🏛️  Total Tax: ৳29,340
```

---

## নতুন Operation যোগ করতে চাইলে?

```csharp
// নতুন কাজ: Invoice Generate করো
// শুধু নতুন Visitor class বানাও — কোনো Product class বদলায় না!

public class InvoiceVisitor : IShoppingVisitor
{
    public void Visit(Book book)
        => Console.WriteLine($"INVOICE | 📚 {book.Name} | ৳{book.Price:N0}");

    public void Visit(Electronics electronics)
        => Console.WriteLine($"INVOICE | 💻 {electronics.Name} | ৳{electronics.Price:N0}");

    public void Visit(Clothing clothing)
        => Console.WriteLine($"INVOICE | 👕 {clothing.Name} | ৳{clothing.Price:N0}");
}

// Book, Electronics, Clothing — একটুও বদলায়নি! ✅
```

---

## ✅ কেন Visitor Pattern ব্যবহার করবো?

| সমস্যা (আগে) | সমাধান (Visitor দিয়ে) |
|-------------|----------------------|
| নতুন operation = সব class বদলাও | নতুন Visitor class বানাও |
| Class এ method ভরে যায় | Class এ শুধু `Accept()` |
| Open/Closed Principle ভাঙে | Extend করো, Modify না |
| Single Responsibility ভাঙে | প্রতিটা Visitor = একটা দায়িত্ব |

---

## ⚠️ কখন ব্যবহার করবো না?

```
❌ Element class ঘন ঘন বদলালে
   → নতুন Element যোগ = সব Visitor এ Visit() যোগ করো

❌ Elements এর সংখ্যা কম হলে
   → Simple if-else যথেষ্ট

❌ Operations কম হলে
   → সরাসরি method রাখাই ভালো
```

---

## ⚠️ Visitor Pattern-এ State Management (`+=` vs `=`)

Visitor এর ভেতরে ডেটা কীভাবে রাখা হচ্ছে, তার ওপর আপনার অ্যাপ্লিকেশনের রেজাল্ট পুরোপুরি নির্ভর করে:
- **Accumulating State (`+=`)**: আমাদের `DiscountVisitor`-এ আমরা `TotalDiscount += discount` ব্যবহার করেছি। এর ফলে সব product এর discount যোগ হয়ে **Total Sum** বের হয়।
- **Single Assignment (`=`)**: যদি `+=` না করে `TotalDiscount = discount` লিখতাম, তবে শুধু সর্বশেষ product এর discount দেখাতো।

---

## 🧠 মনে রাখার Trick

```
Accept() = "দরজা খোলো"          → Product করে
Visit()  = "ঢুকে কাজ করো"       → Visitor করে

Product (Book/Electronics) = বাড়ি 🏠
  → দরজা খুলে দেয় (Accept)
  → বাড়ি বদলায় না

Visitor (Discount/Tax/Ship) = Inspector 🧑‍💼
  → ঢুকে নিজের কাজ করে (Visit)
  → নতুন Inspector = নতুন class

বাড়ি কখনো বদলায় না! ✅
```

---

## 💡 Important Note on GFG Article Bug
The GeeksforGeeks article had a severe SOLID violation. It hardcoded the properties of the shapes (like `radiusOfCircle = 5`) inside the `AreaCalculator` Visitor class!
**Why is this wrong?** Because a Circle's radius belongs to the Circle, not the Visitor! If we have two different circles with radii 5 and 10, the GFG code would fail entirely.
In our `ShapeAreaExample.cs`, we have fixed this. The Shapes hold their own properties, and the Visitor accesses them properly.

---

## 💻 4 Practical C# Examples (এই Folder এ)

| File | Elements | Visitors |
|------|----------|---------|
| `ShapeAreaExample.cs` | Circle, Square, Triangle | AreaCalculatorVisitor |
| `SupermarketCheckoutExample.cs` | Laptop, Fruit, Book | TaxVisitor, DiscountVisitor |
| `DocumentExporterExample.cs` | Paragraph, Image, Table | HtmlExportVisitor, PdfExportVisitor |
| `OrganizationSalaryExample.cs` | RegularEmployee, Manager, Director | BonusCalculatorVisitor, MedicalAllowanceVisitor |

---

*Pattern Category: **Behavioural Design Pattern***
*GoF Book: Design Patterns — Elements of Reusable Object-Oriented Software (1994)*
