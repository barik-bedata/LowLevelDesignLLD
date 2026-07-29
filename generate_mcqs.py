import random
import os
import math

def generate_analytical():
    questions = []
    
    # Pre-defined known types
    base_questions = [
        ("If 'APPLE' is coded as 25, 'GRAPE' is coded as 36, then what is 'BANANA' coded as?", ["36", "49", "64", "81"], "49"),
        ("Look at this series: 2, 1, (1/2), (1/4), ... What number should come next?", ["1/3", "1/8", "2/8", "1/16"], "1/8"),
        ("A is B's sister. C is B's mother. D is C's father. E is D's mother. Then, how is A related to D?", ["Grandfather", "Grandmother", "Daughter", "Granddaughter"], "Granddaughter"),
        ("Which word does NOT belong with the others?", ["Parsley", "Basil", "Dill", "Mayonnaise"], "Mayonnaise"),
        ("Pointing to a photograph of a boy Suresh said, 'He is the son of the only son of my mother.' How is Suresh related to that boy?", ["Brother", "Uncle", "Cousin", "Father"], "Father"),
        ("SCD, TEF, UGH, ____, WKL", ["CMN", "UJI", "VIJ", "IJT"], "VIJ"),
        ("FAG, GAF, HAI, IAH, ____", ["JAK", "HAL", "HAK", "JAI"], "JAK"),
        ("In a certain code, MONKEY is written as XDJMNL. How is TIGER written in that code?", ["QDFHS", "SDFHS", "SHFDQ", "UJHFS"], "QDFHS"),
        ("Statement: Some actors are singers. All the singers are dancers. Conclusion: 1. Some actors are dancers. 2. No singer is actor.", ["Only (1) follows", "Only (2) follows", "Either (1) or (2) follows", "Neither (1) nor (2) follows"], "Only (1) follows"),
        ("Choose the odd one out.", ["Square", "Triangle", "Rectangle", "Cuboid"], "Cuboid")
    ]
    
    questions.extend(base_questions)
    
    # Generate variations
    for i in range(len(questions) + 1, 101):
        q_type = random.choice(['series', 'coding', 'blood', 'odd_one', 'syllogism'])
        
        if q_type == 'series':
            start = random.randint(2, 10)
            diff = random.randint(2, 5)
            series = [start, start + diff, start + 2*diff, start + 3*diff]
            q = f"What is the next number in the series: {series[0]}, {series[1]}, {series[2]}, {series[3]}, ...?"
            ans = str(start + 4*diff)
            opts = [ans, str(start + 4*diff + 1), str(start + 4*diff - 1), str(start + 4*diff + diff)]
        elif q_type == 'coding':
            word = random.choice(['PYTHON', 'JAVA', 'REACT', 'NODE'])
            q = f"If '{word}' is coded in a certain way, what is the logical next step for 'HTML'?"
            opts = ["IPML", "ITML", "IUMM", "HTNM"]
            ans = random.choice(opts)
        elif q_type == 'blood':
            q = f"Person {random.choice(['X','Y','Z'])} says to Person {random.choice(['A','B','C'])}, 'You are the son of my father\\'s brother.' How are they related?"
            opts = ["Cousins", "Brothers", "Uncle-Nephew", "Father-Son"]
            ans = "Cousins"
        elif q_type == 'odd_one':
            categories = [
                ["Dog", "Cat", "Horse", "Snake"],
                ["Apple", "Banana", "Orange", "Potato"],
                ["Car", "Bus", "Train", "Bicycle"]
            ]
            cat = random.choice(categories)
            q = f"Which of the following does NOT belong?"
            opts = cat.copy()
            ans = cat[3]
        else:
            q = f"Statement: All A are B. Some B are C. Conclusion: Some A are C. Is the conclusion definitely true?"
            opts = ["Yes", "No", "Cannot be determined", "Data Inadequate"]
            ans = "No"
            
        random.shuffle(opts)
        questions.append((q, opts, ans))
        
    return questions

def generate_math():
    questions = []
    
    # Pre-defined known types
    base_questions = [
        ("A train running at the speed of 60 km/hr crosses a pole in 9 seconds. What is the length of the train?", ["120 metres", "180 metres", "324 metres", "150 metres"], "150 metres"),
        ("The cost price of 20 articles is the same as the selling price of x articles. If the profit is 25%, then the value of x is:", ["15", "16", "18", "25"], "16"),
        ("A can do a work in 15 days and B in 20 days. If they work on it together for 4 days, then the fraction of the work that is left is:", ["1/4", "1/10", "7/15", "8/15"], "8/15"),
        ("The sum of ages of 5 children born at the intervals of 3 years each is 50 years. What is the age of the youngest child?", ["4 years", "8 years", "10 years", "None of these"], "4 years"),
        ("What is the probability of getting a sum 9 from two throws of a dice?", ["1/6", "1/8", "1/9", "1/12"], "1/9"),
        ("The difference between simple and compound interests compounded annually on a certain sum of money for 2 years at 4% per annum is Re. 1. The sum is:", ["Rs. 625", "Rs. 630", "Rs. 640", "Rs. 650"], "Rs. 625"),
        ("In how many different ways can the letters of the word 'LEADING' be arranged in such a way that the vowels always come together?", ["360", "480", "720", "5040"], "720"),
        ("Two trains of equal length are running on parallel lines in the same direction at 46 km/hr and 36 km/hr. The faster train passes the slower train in 36 seconds. The length of each train is:", ["50 m", "72 m", "80 m", "82 m"], "50 m"),
        ("A alone can do a piece of work in 6 days and B alone in 8 days. A and B undertook to do it for Rs. 3200. With the help of C, they completed the work in 3 days. How much is to be paid to C?", ["Rs. 375", "Rs. 400", "Rs. 600", "Rs. 800"], "Rs. 400"),
        ("A vendor bought toffees at 6 for a rupee. How many for a rupee must he sell to gain 20%?", ["3", "4", "5", "6"], "5")
    ]
    
    questions.extend(base_questions)
    
    # Generate variations
    for i in range(len(questions) + 1, 101):
        q_type = random.choice(['train', 'profit', 'work', 'age', 'probability', 'percentage'])
        
        if q_type == 'train':
            speed = random.choice([36, 54, 72, 90])
            time = random.choice([5, 10, 15, 20])
            length = int(speed * (5/18) * time)
            q = f"A train running at {speed} km/hr crosses a pole in {time} seconds. What is its length?"
            opts = [f"{length} m", f"{length + 10} m", f"{length - 10} m", f"{length + 20} m"]
            ans = f"{length} m"
        elif q_type == 'profit':
            cp = random.randint(10, 50) * 10 # ensure clean numbers
            profit = random.choice([10, 20, 25])
            sp = int(cp + (cp * profit / 100))
            q = f"If the cost price is Tk. {cp} and the profit is {profit}%, what is the selling price?"
            opts = [f"Tk. {sp}", f"Tk. {sp + 10}", f"Tk. {sp - 10}", f"Tk. {sp + 20}"]
            ans = f"Tk. {sp}"
        elif q_type == 'work':
            pairs = [(10, 15), (12, 24), (15, 30), (20, 30)] # these yield integer results
            days_A, days_B = random.choice(pairs)
            total = int((days_A * days_B) / (days_A + days_B))
            q = f"A can do a work in {days_A} days and B can do the same work in {days_B} days. Working together, they will complete the work in:"
            opts = [f"{total} days", f"{total+1} days", f"{total-1} days", f"{total+2} days"]
            ans = f"{total} days"
        elif q_type == 'age':
            father = random.randint(30, 50)
            son = random.randint(5, 15)
            years = random.randint(3, 10)
            q = f"A father is currently {father} years old and his son is {son} years old. What will be the sum of their ages after {years} years?"
            opts = [f"{father+son+(2*years)}", f"{father+son+years}", f"{father+son}", f"{father+son+(3*years)}"]
            ans = f"{father+son+(2*years)}"
        elif q_type == 'probability':
            coins = random.randint(2, 4)
            q = f"If {coins} coins are tossed simultaneously, what is the total number of possible outcomes?"
            opts = [f"{2**coins}", f"{2*coins}", f"{2**(coins-1)}", f"{2**(coins+1)}"]
            ans = f"{2**coins}"
        else:
            percent = random.choice([10, 15, 20, 25])
            val = random.randint(10, 50) * 10
            result = int(val * percent / 100)
            q = f"What is {percent}% of {val}?"
            opts = [f"{result}", f"{result+10}", f"{result-10}", f"{result*2}"]
            ans = f"{result}"
            
        random.shuffle(opts)
        questions.append((q, opts, ans))
        
    return questions

def write_markdown(filename, title, questions):
    with open(filename, 'w') as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Target Companies:** WellDev, Enosis, Brain Station 23, Therap, Kaz Software, etc.\n\n")
        
        for i, (q, opts, ans) in enumerate(questions, 1):
            f.write(f"### Question {i}\n")
            f.write(f"{q}\n\n")
            labels = ['A', 'B', 'C', 'D']
            for label, opt in zip(labels, opts):
                f.write(f"- **{label})** {opt}\n")
            f.write(f"\n<details>\n<summary>View Answer</summary>\n\n")
            f.write(f"**Answer:** {ans}\n")
            f.write(f"</details>\n\n---\n\n")

if __name__ == '__main__':
    analytical = generate_analytical()
    math_q = generate_math()
    
    dir_path = "/Users/barik/Desktop/Study/LowLevelDesignLLD/Logical Reasoning"
    
    write_markdown(os.path.join(dir_path, "Analytical Challenges.md"), "Analytical Challenges (100 MCQs)", analytical)
    write_markdown(os.path.join(dir_path, "Simple Mathematics.md"), "Simple Mathematics (100 MCQs)", math_q)
    
    print("Files created successfully.")
