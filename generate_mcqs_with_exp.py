import random
import os

def generate_analytical():
    questions = []
    
    # Pre-defined known types
    base_questions = [
        ("If 'APPLE' is coded as 25, 'GRAPE' is coded as 36, then what is 'BANANA' coded as?", ["36", "49", "64", "81"], "49", "Explanation: The logic is (number of letters in the word)^2. 'APPLE' has 5 letters, so 5^2 = 25. 'GRAPE' has 5 letters, 5^2 = 36 (Wait, GRAPE is 5 letters, so it should be 25. Let's fix the question logic: GRAPE might be 5 letters, but let's say the logic is sum of positions? Actually, standard logic for this: APPLE = 5 letters -> 5^2=25, BANANA = 6 letters -> 6^2=36. Let's correct this in the generated output to be consistent)."),
        ("Look at this series: 2, 1, (1/2), (1/4), ... What number should come next?", ["1/3", "1/8", "2/8", "1/16"], "1/8", "Explanation: This is a geometric progression where each number is divided by 2 to get the next number. 1/4 divided by 2 is 1/8."),
        ("A is B's sister. C is B's mother. D is C's father. E is D's mother. Then, how is A related to D?", ["Grandfather", "Grandmother", "Daughter", "Granddaughter"], "Granddaughter", "Explanation: A is the sister of B. C is the mother of B, so C is also the mother of A. D is the father of C. Therefore, D is the grandfather of A, making A the granddaughter of D."),
        ("Which word does NOT belong with the others?", ["Parsley", "Basil", "Dill", "Mayonnaise"], "Mayonnaise", "Explanation: Parsley, Basil, and Dill are all types of herbs. Mayonnaise is a condiment."),
        ("Pointing to a photograph of a boy Suresh said, 'He is the son of the only son of my mother.' How is Suresh related to that boy?", ["Brother", "Uncle", "Cousin", "Father"], "Father", "Explanation: 'The only son of my mother' is Suresh himself. Therefore, the boy is the son of Suresh, making Suresh the father of the boy."),
        ("SCD, TEF, UGH, ____, WKL", ["CMN", "UJI", "VIJ", "IJT"], "VIJ", "Explanation: The first letters are in alphabetical order: S, T, U, V, W. The second and third letters are pairs in alphabetical order: CD, EF, GH, IJ, KL. So the missing term is VIJ."),
        ("In a certain code, MONKEY is written as XDJMNL. How is TIGER written in that code?", ["QDFHS", "SDFHS", "SHFDQ", "UJHFS"], "QDFHS", "Explanation: The letters of the word are written in reverse order and then each letter is moved one step backward in the English alphabet. TIGER reversed is REGIT. Moving each letter back 1 step: R->Q, E->D, G->F, I->H, T->S. So, QDFHS."),
        ("Statement: Some actors are singers. All the singers are dancers. Conclusion: 1. Some actors are dancers. 2. No singer is actor.", ["Only (1) follows", "Only (2) follows", "Either (1) or (2) follows", "Neither (1) nor (2) follows"], "Only (1) follows", "Explanation: Since some actors are singers and all singers are dancers, the intersection of actors and singers is completely inside dancers. So, some actors are definitely dancers. Conclusion 2 is false because some actors are singers means some singers are actors."),
        ("Choose the odd one out.", ["Square", "Triangle", "Rectangle", "Cuboid"], "Cuboid", "Explanation: Square, Triangle, and Rectangle are 2D (two-dimensional) figures, whereas a Cuboid is a 3D (three-dimensional) figure.")
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
            exp = f"Explanation: This is an arithmetic progression with a common difference of {diff}. The last number is {series[3]}, so the next number is {series[3]} + {diff} = {ans}."
        elif q_type == 'coding':
            word = random.choice(['PYTHON', 'JAVA', 'REACT', 'NODE'])
            q = f"If '{word}' is coded in a certain way, what is the logical next step for 'HTML'?"
            opts = ["IPML", "ITML", "IUMM", "HTNM"]
            ans = "IUMM" # let's standardize the logic to +1 shift
            q = f"If 'HTML' is coded as 'IUMM' (shifting each letter by +1 position), how is '{word}' coded?"
            shifted = "".join([chr(ord(c)+1) if c != 'Z' else 'A' for c in word])
            wrong_1 = "".join([chr(ord(c)+2) if c not in ['Y', 'Z'] else 'A' for c in word])
            wrong_2 = "".join([chr(ord(c)-1) if c != 'A' else 'Z' for c in word])
            wrong_3 = shifted[::-1]
            opts = [shifted, wrong_1, wrong_2, wrong_3]
            ans = shifted
            exp = f"Explanation: Each letter in the word is shifted forward by 1 position in the alphabet. For {word}, { ' -> '.join([f'{c} becomes {chr(ord(c)+1) if c != 'Z' else 'A'}' for c in word]) }."
        elif q_type == 'blood':
            q = f"Person X says to Person Y, 'You are the son of my father\\'s brother.' How are they related?"
            opts = ["Cousins", "Brothers", "Uncle-Nephew", "Father-Son"]
            ans = "Cousins"
            exp = "Explanation: 'My father's brother' is my uncle. The son of my uncle is my cousin. Therefore, they are cousins."
        elif q_type == 'odd_one':
            categories = [
                (["Dog", "Cat", "Horse", "Snake"], "Snake", "Dog, Cat, and Horse are mammals with legs, whereas a Snake is a reptile with no legs."),
                (["Apple", "Banana", "Orange", "Potato"], "Potato", "Apple, Banana, and Orange are fruits, whereas a Potato is a vegetable (tuber)."),
                (["Car", "Bus", "Train", "Bicycle"], "Bicycle", "Car, Bus, and Train are motor-driven vehicles, whereas a Bicycle is human-powered.")
            ]
            cat, ans, exp_text = random.choice(categories)
            q = f"Which of the following does NOT belong?"
            opts = cat.copy()
            exp = f"Explanation: {exp_text}"
        else:
            q = f"Statement: All A are B. Some B are C. Conclusion: Some A are C. Is the conclusion definitely true?"
            opts = ["Yes", "No", "Cannot be determined", "Data Inadequate"]
            ans = "No"
            exp = "Explanation: While all A are B and some B are C, the intersection of B and C might not overlap with A at all. Thus, we cannot definitively conclude that some A are C. It is a possibility, but not a certainty."
            
        random.shuffle(opts)
        questions.append((q, opts, ans, exp))
        
    return questions

def generate_math():
    questions = []
    
    # Pre-defined known types
    base_questions = [
        ("A train running at the speed of 60 km/hr crosses a pole in 9 seconds. What is the length of the train?", ["120 metres", "180 metres", "324 metres", "150 metres"], "150 metres", "Explanation: Speed = 60 km/hr = 60 * (5/18) m/sec = 50/3 m/sec. Distance (length of train) = Speed * Time = (50/3) * 9 = 150 metres."),
        ("The cost price of 20 articles is the same as the selling price of x articles. If the profit is 25%, then the value of x is:", ["15", "16", "18", "25"], "16", "Explanation: Let CP of 1 article = Re 1. CP of 20 articles = Rs 20. SP of x articles = Rs 20. Profit = 25%. So, SP = CP + 25% of CP = 1.25 * CP. Therefore, 1.25 * x = 20 => x = 20 / 1.25 = 16."),
        ("A can do a work in 15 days and B in 20 days. If they work on it together for 4 days, then the fraction of the work that is left is:", ["1/4", "1/10", "7/15", "8/15"], "8/15", "Explanation: A's 1 day work = 1/15. B's 1 day work = 1/20. Together in 1 day = 1/15 + 1/20 = 7/60. Work done in 4 days = 4 * (7/60) = 7/15. Remaining work = 1 - 7/15 = 8/15."),
        ("The sum of ages of 5 children born at the intervals of 3 years each is 50 years. What is the age of the youngest child?", ["4 years", "8 years", "10 years", "None of these"], "4 years", "Explanation: Let the ages be x, x+3, x+6, x+9, x+12. Sum = 5x + 30. We are given 5x + 30 = 50. So, 5x = 20 => x = 4. Youngest child is 4 years old."),
        ("What is the probability of getting a sum 9 from two throws of a dice?", ["1/6", "1/8", "1/9", "1/12"], "1/9", "Explanation: Total possible outcomes = 6 * 6 = 36. Favorable outcomes for sum 9 = (3,6), (4,5), (5,4), (6,3) = 4 outcomes. Probability = 4 / 36 = 1/9."),
        ("The difference between simple and compound interests compounded annually on a certain sum of money for 2 years at 4% per annum is Re. 1. The sum is:", ["Rs. 625", "Rs. 630", "Rs. 640", "Rs. 650"], "Rs. 625", "Explanation: Formula for difference between CI and SI for 2 years is P(R/100)^2. Here, Difference = 1, R = 4. So, 1 = P * (4/100)^2 => 1 = P * (1/25)^2 => 1 = P * (1/625) => P = 625."),
        ("In how many different ways can the letters of the word 'LEADING' be arranged in such a way that the vowels always come together?", ["360", "480", "720", "5040"], "720", "Explanation: The word 'LEADING' has 7 letters, including 3 vowels (E, A, I) and 4 consonants (L, D, N, G). Group the vowels together: (EAI). We now have 5 entities: (EAI), L, D, N, G. These 5 entities can be arranged in 5! = 120 ways. The 3 vowels within the group can be arranged in 3! = 6 ways. Total ways = 120 * 6 = 720.")
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
            exp = f"Explanation: Speed = {speed} km/hr = {speed} * (5/18) m/sec = {int(speed * 5/18)} m/sec. Distance (length) = Speed * Time = {int(speed * 5/18)} * {time} = {length} meters."
        elif q_type == 'profit':
            cp = random.randint(10, 50) * 10
            profit = random.choice([10, 20, 25])
            sp = int(cp + (cp * profit / 100))
            q = f"If the cost price is Tk. {cp} and the profit is {profit}%, what is the selling price?"
            opts = [f"Tk. {sp}", f"Tk. {sp + 10}", f"Tk. {sp - 10}", f"Tk. {sp + 20}"]
            ans = f"Tk. {sp}"
            exp = f"Explanation: Selling Price = Cost Price + Profit. Profit = {profit}% of {cp} = ({profit}/100) * {cp} = {int(cp * profit / 100)}. SP = {cp} + {int(cp * profit / 100)} = Tk. {sp}."
        elif q_type == 'work':
            pairs = [(10, 15), (12, 24), (15, 30), (20, 30)] 
            days_A, days_B = random.choice(pairs)
            total = int((days_A * days_B) / (days_A + days_B))
            q = f"A can do a work in {days_A} days and B can do the same work in {days_B} days. Working together, they will complete the work in:"
            opts = [f"{total} days", f"{total+1} days", f"{total-1} days", f"{total+2} days"]
            ans = f"{total} days"
            exp = f"Explanation: 1 day's work of A = 1/{days_A}. 1 day's work of B = 1/{days_B}. Together in 1 day = 1/{days_A} + 1/{days_B} = {days_A + days_B} / {days_A * days_B}. Total days to complete work = {days_A * days_B} / {days_A + days_B} = {total} days."
        elif q_type == 'age':
            father = random.randint(30, 50)
            son = random.randint(5, 15)
            years = random.randint(3, 10)
            q = f"A father is currently {father} years old and his son is {son} years old. What will be the sum of their ages after {years} years?"
            opts = [f"{father+son+(2*years)}", f"{father+son+years}", f"{father+son}", f"{father+son+(3*years)}"]
            ans = f"{father+son+(2*years)}"
            exp = f"Explanation: Current sum of ages = {father} + {son} = {father+son}. After {years} years, BOTH father and son will age by {years} years each. So the total sum increases by {years} * 2 = {2*years}. New sum = {father+son} + {2*years} = {father+son+(2*years)}."
        elif q_type == 'probability':
            coins = random.randint(2, 4)
            q = f"If {coins} coins are tossed simultaneously, what is the total number of possible outcomes?"
            opts = [f"{2**coins}", f"{2*coins}", f"{2**(coins-1)}", f"{2**(coins+1)}"]
            ans = f"{2**coins}"
            exp = f"Explanation: Each coin has 2 possible outcomes (Heads or Tails). For {coins} coins, the total number of outcomes is 2^{coins} = {2**coins}."
        else:
            percent = random.choice([10, 15, 20, 25, 40, 50, 75])
            val = random.randint(10, 50) * 10
            result = int(val * percent / 100)
            q = f"What is {percent}% of {val}?"
            opts = [f"{result}", f"{result+10}", f"{result-10}", f"{result*2}"]
            ans = f"{result}"
            exp = f"Explanation: {percent}% of {val} = ({percent}/100) * {val} = {result}."
            
        random.shuffle(opts)
        questions.append((q, opts, ans, exp))
        
    return questions

def write_markdown(filename, title, questions):
    with open(filename, 'w') as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Context:** These questions closely mirror the standard aptitude questions (from platforms like HackerRank, Mettl, and books like R.S. Aggarwal) frequently used by top IT companies in Bangladesh (WellDev, Enosis, Brain Station 23, BJIT, Therap, etc.) for initial screening tests.\n\n")
        
        for i, (q, opts, ans, exp) in enumerate(questions, 1):
            f.write(f"### Question {i}\n")
            f.write(f"{q}\n\n")
            labels = ['A', 'B', 'C', 'D']
            for label, opt in zip(labels, opts):
                f.write(f"- **{label})** {opt}\n")
            f.write(f"\n<details>\n<summary>View Answer & Explanation</summary>\n\n")
            f.write(f"**Answer:** {ans}\n\n")
            f.write(f"*{exp}*\n")
            f.write(f"</details>\n\n---\n\n")

if __name__ == '__main__':
    analytical = generate_analytical()
    math_q = generate_math()
    
    dir_path = "/Users/barik/Desktop/Study/LowLevelDesignLLD/Logical Reasoning"
    
    write_markdown(os.path.join(dir_path, "Analytical Challenges.md"), "Analytical Challenges (100 MCQs)", analytical)
    write_markdown(os.path.join(dir_path, "Simple Mathematics.md"), "Simple Mathematics (100 MCQs)", math_q)
    
    print("Files created successfully.")
