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

### 🍫 The Chocolate Analogy (সহজ বাস্তব জীবনের উদাহরণ)
UI আর্কিটেকচার বোঝার জন্য মনে করি একজন বাচ্চা চকোলেট খেতে চায়:
* **Model (মডেল):** চকলেটের বয়াম / ফ্রিজ (Database, API, Data Layer)।
* **View (ভিউ):** ছোট্ট বাচ্চা / মোবাইল স্ক্রিন (যেখানে বাটন চ্যাপা হয় ও চকলেট স্ক্রিনে দেখানো হয়)।
* **Middleman (Controller / Presenter / ViewModel):** মাঝখানের মধ্যস্থতাকারী মাধ্যম।

---

### 2.1 MVC (Model - View - Controller)
* **মূল নীতি:** Model এবং View-এর মধ্যে সরাসরি যোগাযোগ থাকতে পারে।
* **সহজ উদাহরণ:** 
  1. বাচ্চাটি সরাসরি কিচেনের শেফ বা রেস্তোরাঁর **Controller**-কে অর্ডারের কথা বলল।
  2. Controller ফ্রিজ (Model) থেকে চকলেট প্রসেস করল।
  3. Model সরাসরি আপডেট হয়ে বাচ্চাটিকে (View) টেক্সট/ডাটা দিয়ে দিল।
* **ফ্লো:** `User ➔ Controller ➔ Model ➔ View`

```kotlin
// --- MVC Code Flow Example ---
class Controller(private val model: ChocolateModel, private val view: ChocolateView) {
    fun onGetChocolateClicked() {
        model.fetchData() // Model আপডেট হয় এবং Model সরাসরি View-কে নোটিফাই করে
    }
}
```

---

### 2.2 MVP (Model - View - Presenter)
* **মূল নীতি:** Model এবং View **কখনোই সরাসরি কথা বলে না**। সব যোগাযোগ Presenter-এর মাধ্যমে হয়। Presenter নিজের হাতে ধরে ধরে View-কে নির্দেশ দেয়।
* **সহজ উদাহরণ (রিমোট কেয়ারটেকার):**
  1. বাচ্চা বললে: *"চকলেট দাও!"* (View ➔ Presenter)
  2. Presenter ফ্রিজ থেকে চকলেট নিয়ে এল। (Presenter ↔ Model)
  3. Presenter বাচ্চার মুখ হাত ধরে বলল: *"এই নাও হা করো, আমি চকলেটটা খাইয়ে দিচ্ছি আর মুখ মুছে দিচ্ছি।"* (Presenter ➔ View)
* **কোড ফ্লো (Code Mechanics):**
  1. View ปุ่มে ক্লিক হলে Presenter-এর মেথড ডাকে: `presenter.getChocolate()`
  2. Presenter Model থেকে ডাটা আনে।
  3. Presenter সরাসরি View-এর ইন্টারফেস কল করে নির্দেশ দেয়: `view.showLoading()`, `view.showChocolate(data)`, অথবা `view.showError()`

```kotlin
// --- MVP Code Flow Example ---

// ১. View Interface
interface ChocolateView {
    fun showLoading()
    fun showChocolateOnScreen(chocolate: String)
    fun showError(message: String)
}

// ২. Presenter (View Interface ধারণ করে)
class ChocolatePresenter(
    private val view: ChocolateView,
    private val model: ChocolateModel
) {
    fun getChocolate() {
        view.showLoading() // 👈 Presenter নির্দেশ দিল: "লোডিং দেখাও"
        try {
            val data = model.fetchFromFridge() // 👈 Model থেকে ডাটা আনল
            view.showChocolateOnScreen(data) // 👈 Presenter বলল: "চকলেট স্ক্রিনে দেখাও"
        } catch (e: Exception) {
            view.showError("চকলেট পাওয়া যায়নি!")
        }
    }
}

// ৩. View (Activity / Fragment)
class MainActivity : AppCompatActivity(), ChocolateView {
    private lateinit var presenter: ChocolatePresenter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        presenter = ChocolatePresenter(this, ChocolateModel())

        button.setOnClickListener {
            presenter.getChocolate() // 👈 View কেবল নির্দেশ দিল
        }
    }

    override fun showLoading() { /* UI লোডিং দেখায় */ }
    override fun showChocolateOnScreen(chocolate: String) { textView.text = chocolate }
    override fun showError(message: String) { toast(message) }
}
```

---

### 2.3 MVVM (Model - View - ViewModel)
* **মূল নীতি:** ViewModel ভিউকে চেনে না! ViewModel তার **জাদুকরী টেবিলে (Observable State/LiveData)** ডাটা আপডেট করে রাখে। View সেই টেবিলের দিকে তাকিয়ে থাকে (Observe করে) এবং ডাটা বদলালেই **স্বয়ংক্রিয়ভাবে (Reactive / Auto Data Binding)** নিজেকে রিফ্রেশ করে নেয়।
* **সহজ উদাহরণ (জাদুকরী টেবিল):**
  1. বাচ্চা বাটন চেপে বলল: *"চকলেট দাও!"* (View ➔ ViewModel)
  2. ViewModel ফ্রিজ থেকে এনে চকলেটের **জাদুকরী টেবিলে (LiveData Variable)** রেখে দিল।
  3. বাচ্চা আগে থেকেই সেই টেবিলের দিকে চোখ রেখে বসে ছিল (Observe করছিল)। টেবিলে চকলেট আসার সাথে সাথে বাচ্চা সেটা দেখে নিল এবং মুখে নিয়ে নিল!
* **ViewModel ↔ View সম্পর্ক:** ViewModel কিন্তু View-কে চেনে না, কোনো নির্দেশও পাঠায় না। শুধু ভিউ ViewModel-কে চেনে।

```kotlin
// --- MVVM Code Flow Example ---

// ১. ViewModel (কোনো View/Activity-র নাম বা রেফারেন্স নেই!)
class ChocolateViewModel(private val model: ChocolateModel) : ViewModel() {
    // 👈 জাদুকরী টেবিল (Observable State / LiveData)
    val chocolateTable = MutableLiveData<String>()
    val isLoading = MutableLiveData<Boolean>()

    fun fetchChocolate() {
        isLoading.value = true
        val data = model.fetchFromFridge()
        chocolateTable.value = data // 👈 টেবিলে ডাটা রেখে দিল! View-কে কল করার দরকার নেই।
        isLoading.value = false
    }
}

// ২. View (Activity / Fragment)
class MainActivity : AppCompatActivity() {
    private val viewModel: ChocolateViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // 👈 টেবিলে চোখ রাখা (Observe করা) - ডাটা চেঞ্জ হলেই অটো রান হবে
        viewModel.chocolateTable.observe(this) { newChocolate ->
            textView.text = newChocolate // 👈 অটোমেটিক আপডেট!
        }

        viewModel.isLoading.observe(this) { loading ->
            progressBar.visibility = if (loading) View.VISIBLE else View.GONE
        }

        button.setOnClickListener {
            viewModel.fetchChocolate() // 👈 ViewModel-কে কল করে দিল
        }
    }
}
```

---

### 🧪 Unit Testing Comparison (MVP vs MVVM)

ViewModel Unit Test করা কেন পানি পানের মতো সহজ?
1. **Android Framework/UI ইন্ডিপেন্ডেন্ট:** ViewModel-এর ভেতর কোনো Activity, Fragment, Context বা UI কম্পোনেন্ট থাকে না।
2. **এমুলেটর লাগে না:** সরাসরি ল্যাপটপের প্রসেসরে (JVM) মাত্র ১-২ সেকেন্ডে টেস্ট রান হয়ে যায়।

```kotlin
// --- MVVM Unit Test Example ---
class ChocolateViewModelTest {

    @Test
    fun `when fetchChocolate is called, chocolateTable should update correctly`() {
        // Arrange
        val fakeModel = ChocolateModel()
        val viewModel = ChocolateViewModel(fakeModel)

        // Act
        viewModel.fetchChocolate()

        // Assert (শুধুমাত্র টেবিলের মান পরীক্ষা করা)
        assertEquals("Dairy Milk", viewModel.chocolateTable.value)
    }
}
```

* **MVP Testing:** Presenter টেস্ট করার জন্য Mock `View` ইন্টারফেস তৈরি করে পাস করতে হতো।
* **MVVM Testing:** কোনো Fake View লাগে না, কারণ ViewModel View-কে চেনেই না!

---

### 📊 Big Comparison Matrix (MVC vs MVP vs MVVM)

| ফিচার / দিক | MVC | MVP | MVVM |
| :--- | :--- | :--- | :--- |
| **Middleman Component** | Controller | Presenter | ViewModel |
| **Model ↔ View কথা বলে?** | হ্যাঁ, বলতে পারে | **না, একদম না** | **না, একদম না** |
| **Middleman View-কে চেনে?** | কিছুটা চেনে | **হ্যাঁ** (Interface `IView` দিয়ে চেনে) | **না** (View-এর কোনো অস্তিত্ব জানে না) |
| **UI আপডেট করার পদ্ধতি** | Controller / Model আপডেট পাঠায় | **Manual / Imperative** (`view.showData()`) | **Automatic / Reactive** (Data Binding & Observing) |
| **সম্পর্ক (Relation)** | 1 Controller : Multi Views | 1 Presenter : 1 View | 1 ViewModel : Multi Views |
| **Memory Leak ঝুঁকি** | মাঝারি | বেশি (Presenter View রেফারেন্স রাখায়) | **নেই বললেই চলে** (Screen Rotate হলেও ক্লিয়ার) |
| **Unit Test করা কেমন?** | কিছুটা কঠিন | সহজ (View Mock করতে হয়) | **সবচেয়ে সহজ** (কোনো Mock View ছাড়াই টেস্ট করা যায়) |
| **আধুনিক ব্যবহার** | Web Frameworks (Rails, Laravel) | Classic Android / WinForms | Modern Frameworks (Compose, SwiftUI, React, Vue) |

---

### 3. Data Access & Persistence Patterns (ডেটা/ডোমেইন লেভেল)
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
2. **Strategy Pattern:** রান-টাইমে অ্যালগরিদম পরিবর্তন করার নমনীয়তা দেওয়া।
3. **Command Pattern:** কোনো রিকোয়েস্টকে স্ট্যান্ডঅ্যালোন অবজেক্ট হিসেবে আবৃত করা।
4. **State, Iterator, Mediator, Memento, Visitor, Chain of Responsibility, Interpreter, Template Method.**

---

## 💡 Important OOP & MCQ Quick Notes

* **Diamond Problem:** একাধিক ক্লাস (B & C) একটি বেস ক্লাস (A) কে ইনহেরিট করে ওভাররাইড করলে এবং ৪র্থ ক্লাস (D) উভয়কে ইনহেরিট করলে যে Ambiguity সৃষ্টি হয়। সমাধান: C++ Scope Resolution বা Interfaces (Java)।
* **Polymorphism Types in C++:** প্রধানত **২ প্রকার** —
  1. Compile-time (Function & Operator Overloading)
  2. Run-time (Function Overriding / Virtual Functions)
* **Upcasting:** Child ➔ Parent রূপান্তর। এটি **১০০% Safe** এবং Implicit (কারণ Parent-এর সব প্রপার্টি Child-এ থাকেই)।
