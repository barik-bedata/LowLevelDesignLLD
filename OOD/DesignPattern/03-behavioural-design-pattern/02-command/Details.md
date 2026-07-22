# Command Design Pattern - Deep Dive & Real-World Implementation

## 📌 ১. ওভারভিউ (Overview)
**Command Design Pattern** হলো একটি Behavioral Design Pattern, যা একটি মেথড কল বা রিকোয়েস্টকে একটি স্বতন্ত্র **অবজেক্টে (Command Object)** রূপান্তর করে। 

### ❓ আপনার মনে প্রশ্ন আসতে পারে: "মেথড তো সরাসরি `tv.TurnOn()` ডিরেক্ট কল করলেই হতো! এত জলঘোলা করার কি দরকার ছিল?"
ছোট বা সাধারণ প্রজেক্টে সরাসরি মেথড কল করাটাই বুদ্ধিমানের কাজ। কিন্তু সফটওয়্যার যখন বড় হয় এবং তাতে **Undo/Redo (Ctrl+Z)**, **Task Scheduler/Queue**, **Macro Commands** বা **UI Decoupling**-এর মতো ফিচার যুক্ত হয়, তখন সরাসরি মেথড কল করলে কোড রিজিড ও আনমেইনটেইনেবল হয়ে যায়।

---

## 🚀 ২. কেন Command Pattern দরকার? (The Core Benefits)

| ফিচার / উদ্দেশ্য | সরাসরি মেথড কল (`tv.TurnOn()`) | Command Pattern |
| :--- | :--- | :--- |
| **Undo / Redo** | করা প্রায় অসম্ভব (হিস্টোরি মনে রাখা যায় না)। | `Stack<ICommand>` দিয়ে খুব সহজে করা যায়। |
| **Task Queue / Scheduling** | কাজ সাথে সাথে চালাতে হয়, পরে জমিয়ে রাখা যায় না। | `Queue<ICommand>`-এ জমা রেখে পরে একবারে চালানো যায়। |
| **Loose Coupling** | UI বা বাটন ক্লাসকে টিভি/এসির সব মেথড জানতে হয়। | বাটন শুধু `ICommand.Execute()` চেনে, রিসিভারকে চেনেও না। |
| **Macro Execution** | প্রতিটা অবজেক্টের জন্য আলাদা কোড লিখতে হয়। | একাধিক কমান্ড প্যাক করে এক বাটন চাপেই সব চালানো যায়। |

---

## 🛠️ ৩. Real-World C# Implementation (Undo/Redo + Task Scheduler)

নিচে একটি সম্পূর্ণ ইন্টারপ্রাইজ-লেভেল C# উদাহরণ দেওয়া হলো, যেখানে **Multi-level Undo/Redo (Stack Based)** এবং **Task Queue Scheduler (Queue Based)** একসাথে ইমপ্লিমেন্ট করা হয়েছে:

```csharp
using System;
using System.Collections.Generic;

namespace BehavioralDesignPattern.CommandRealWorld
{
    // ==========================================
    // 1. Receivers (আসল কাজ যারা করে)
    // ==========================================
    public class Light
    {
        public string Location { get; }
        public Light(string location) => Location = location;

        public void TurnOn() => Console.WriteLine($"[Light] 💡 {Location} Light turned ON.");
        public void TurnOff() => Console.WriteLine($"[Light] 💡 {Location} Light turned OFF.");
    }

    public class SmartLock
    {
        public void Lock() => Console.WriteLine("[SmartLock] 🔒 Main Door is now LOCKED.");
        public void Unlock() => Console.WriteLine("[SmartLock] 🔓 Main Door is now UNLOCKED.");
    }

    public class AirConditioner
    {
        public void SetTemperature(int temp) => Console.WriteLine($"[AC] ❄️ AC set to {temp}°C.");
    }

    // ==========================================
    // 2. Command Interface
    // ==========================================
    public interface ICommand
    {
        void Execute();
        void Undo();
        string Description { get; }
    }

    // ==========================================
    // 3. Concrete Commands (বাটন বা অ্যাকশনসমূহ)
    // ==========================================
    public class LightOnCommand : ICommand
    {
        private readonly Light _light;
        public LightOnCommand(Light light) => _light = light;

        public string Description => $"Turn ON {_light.Location} Light";
        public void Execute() => _light.TurnOn();
        public void Undo() => _light.TurnOff();
    }

    public class LockDoorCommand : ICommand
    {
        private readonly SmartLock _lock;
        public LockDoorCommand(SmartLock lockSystem) => _lock = lockSystem;

        public string Description => "Lock Main Door";
        public void Execute() => _lock.Lock();
        public void Undo() => _lock.Unlock();
    }

    public class SetACTempCommand : ICommand
    {
        private readonly AirConditioner _ac;
        private readonly int _newTemp;
        private readonly int _prevTemp;

        public SetACTempCommand(AirConditioner ac, int newTemp, int prevTemp = 24)
        {
            _ac = ac;
            _newTemp = newTemp;
            _prevTemp = prevTemp;
        }

        public string Description => $"Set AC Temp to {_newTemp}°C";

        public void Execute()
        {
            _ac.SetTemperature(_newTemp);
        }

        public void Undo()
        {
            Console.WriteLine($"[AC Undo] Reverting temperature back to {_prevTemp}°C...");
            _ac.SetTemperature(_prevTemp);
        }
    }

    // ==========================================
    // 4. Undo / Redo Manager (Stack Based)
    // ==========================================
    public class CommandHistoryManager
    {
        private readonly Stack<ICommand> _undoStack = new Stack<ICommand>();
        private readonly Stack<ICommand> _redoStack = new Stack<ICommand>();

        public void ExecuteCommand(ICommand command)
        {
            command.Execute();
            _undoStack.Push(command);
            _redoStack.Clear(); // নতুন কোনো অ্যাকশন করলে Redo হিস্ট্রি ক্লিয়ার হয়ে যায়
        }

        // Ctrl + Z (Undo)
        public void Undo()
        {
            if (_undoStack.Count > 0)
            {
                ICommand lastCommand = _undoStack.Pop();
                Console.WriteLine($"\n↩️ [UNDOing]: {lastCommand.Description}");
                lastCommand.Undo();
                _redoStack.Push(lastCommand);
            }
            else
            {
                Console.WriteLine("\n⚠️ Nothing to Undo!");
            }
        }

        // Ctrl + Y (Redo)
        public void Redo()
        {
            if (_redoStack.Count > 0)
            {
                ICommand redoCommand = _redoStack.Pop();
                Console.WriteLine($"\n↪️ [REDOing]: {redoCommand.Description}");
                redoCommand.Execute();
                _undoStack.Push(redoCommand);
            }
            else
            {
                Console.WriteLine("\n⚠️ Nothing to Redo!");
            }
        }
    }

    // ==========================================
    // 5. Task Queue / Scheduler (Queue Based)
    // ==========================================
    public class TaskScheduler
    {
        private readonly Queue<ICommand> _taskQueue = new Queue<ICommand>();

        public void ScheduleTask(ICommand command)
        {
            _taskQueue.Enqueue(command);
            Console.WriteLine($"[Scheduler] 📌 Task Scheduled: '{command.Description}'");
        }

        // ব্যাচ বা সময় হলে শিডিউলকৃত সব কাজ সিরিয়ালি এক্সিকিউট করা
        public void ExecuteAllScheduledTasks(CommandHistoryManager historyManager)
        {
            Console.WriteLine($"\n--- ⏳ Running Scheduled Queue Tasks ({_taskQueue.Count} tasks) ---");
            
            while (_taskQueue.Count > 0)
            {
                ICommand nextTask = _taskQueue.Dequeue();
                historyManager.ExecuteCommand(nextTask); 
            }
            Console.WriteLine("--- ✅ All Scheduled Tasks Executed ---\n");
        }
    }

    // ==========================================
    // Client Runner
    // ==========================================
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Real-World Command Pattern: Undo/Redo & Queue Scheduler ===\n");

            // ১. রিসিভার
            Light livingRoomLight = new Light("Living Room");
            SmartLock mainDoor = new SmartLock();
            AirConditioner ac = new AirConditioner();

            // ২. ম্যানেজারস
            CommandHistoryManager history = new CommandHistoryManager();
            TaskScheduler scheduler = new TaskScheduler();

            // ----------------------------------------------------
            // পার্ট ১: সজীব কাজ এবং UNDO / REDO টেস্ট
            // ----------------------------------------------------
            Console.WriteLine("--- 1. Live Operations with Undo/Redo ---");
            
            ICommand lightCmd = new LightOnCommand(livingRoomLight);
            ICommand acCmd = new SetACTempCommand(ac, 18, prevTemp: 24);

            history.ExecuteCommand(lightCmd);
            history.ExecuteCommand(acCmd);

            // Undo করা (Ctrl + Z)
            history.Undo(); // এসি আবার ২৪ ডিগ্রিতে চলে যাবে
            history.Undo(); // লাইট অফ হয়ে যাবে

            // Redo করা (Ctrl + Y)
            history.Redo(); // লাইট আবার অন হবে

            // ----------------------------------------------------
            // পার্ট ২: QUEUE / SCHEDULER (Macro / Batch Execution)
            // ----------------------------------------------------
            Console.WriteLine("\n--- 2. Building Night Routine (Queue Scheduling) ---");

            // কাজগুলো লাইনে জমা করা হচ্ছে:
            scheduler.ScheduleTask(new LockDoorCommand(mainDoor));      
            scheduler.ScheduleTask(new SetACTempCommand(ac, 22));        
            scheduler.ScheduleTask(new LightOnCommand(livingRoomLight)); 

            // রাত ১২টা বাজল! শিডিউলটি অটোমেটিক রান হলো:
            scheduler.ExecuteAllScheduledTasks(history);

            // শিডিউল রান হওয়ার পরও প্রয়োজনে শেষ কাজটি Undo করা সম্ভব:
            history.Undo();
        }
    }
}
```

---

## 🌍 ৪. বাস্তব সফটওয়্যার ইন্ডাস্ট্রিতে কোথায় ব্যবহার হয়? (Real-World Examples)

### ১. ফটোশপ ও টেক্সট এডিটর (Figma, Photoshop, VS Code, MS Word)
* **ব্যবহার:** `Ctrl + Z` (Undo) এবং `Ctrl + Y` (Redo) ফিচারে।
* **লজিক:** প্রতিবার ইউজার কিছু ড্র করলে বা টাইপ করলে একটি `Command` অবজেক্ট `Undo Stack`-এ পুশ করা হয়। `Ctrl+Z` দিলে স্ট্যাক থেকে `Pop()` করে `.Undo()` মেথড ফায়ার করা হয়।

### ২. ব্যাকগ্রাউন্ড জব প্রসেসর ও কিউ (Hangfire, RabbitMQ, Celery, AWS SQS)
* **ব্যবহার:** ইমেইল পাঠানো, ভিডিও প্রসেস করা বা ইনভয়েস জেনারেট করায়।
* **লজিক:** ইউজারের রিকোয়েস্ট পাওয়ার সাথে সাথেই ভারী কাজ রান না করে `SendEmailCommand` বানিয়ে একটি `Queue<ICommand>`-এ পুশ করা হয়। ব্যাকগ্রাউন্ড ওয়ার্কার সার্ভিস লাইনে থাকা কমান্ডগুলোকে একে একে টেনে নিয়ে `Execute()` করে।

### ৩. ডাটাবেস মাইগ্রেশন (Entity Framework / Liquibase / Laravel Migration)
* **ব্যবহার:** ডাটাবেসের স্কিমা পরিবর্তন ও রোলব্যাক করার সময়।
* **লজিক:** 
  * `Up()` ➔ যা মূলত `Execute()` (নতুন টেবিল তৈরি বা কলাম যোগ করে)।
  * `Down()` ➔ যা মূলত `Undo()` (কোনো ভুল হলে মাইগ্রেশন রোলব্যাক করে আগের অবস্থায় ফিরিয়ে নেয়)।

### ৪. গেইম ডেভেলপমেন্ট (Unity & Unreal Engine - Input Systems & Replays)
* **ব্যবহার:** বাটন রি-ম্যাপিং, রি-প্লে (Replay) এবং টাইম-রিওয়াইন্ড (Time Rewind) ফিচারে।
* **লজিক:** কিবোর্ড বা জয়স্টিকের ইনপুট সরাসরি প্লেয়ারকে মুভ করে না, বরং `MoveCommand`, `JumpCommand` তৈরি করে। গেম রি-প্লে বা রিওয়াইন্ডের সময় সেভ থাকা কমান্ডগুলো উল্টো সিরিয়ালে `Undo()` করে রিওয়াইন্ড ইফেক্ট তৈরি করা হয়।

### ৫. ডিস্ট্রিবিউটেড সিস্টেমস ও ই-কমার্স (Saga Pattern / Compensation Logic)
* **ব্যবহার:** Microservices Architecture এবং E-Commerce Order Processing।
* **লজিক:** ই-কমার্সে `ReserveStockCommand` ➔ `ChargePaymentCommand` ➔ `ShipOrderCommand` চলে। যদি ২য় ধাপে পেমেন্ট ফেল করে, তবে পূর্বের ধাপগুলোর Compensation/Undo কমান্ড (`ReleaseStockCommand`) ফায়ার করে সিস্টেম সঠিক স্টেটে রাখা হয়।
