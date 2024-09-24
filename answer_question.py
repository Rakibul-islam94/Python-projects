questions=("1.Which language is mostly used in web development?","2.Which language is mostly used in app development?","3.Which one is the newest language among these?",
           "4.Which one is not a programming language?")
answers=(("A. Java","B. Javascript","C. Python","D. C++"),("A. Javascript","B. Python","C. Java","D. Go"),
         ("A. Python","B. Java","C. Rust","D. C++"),("A. Kotlin","B. Html","C. Ruby","D. Swift")
         )
guesses=[]
scores=0
question_num=0
Correct_answers=("B","C","A","B")
for question in questions:
    print("-----------------------------")
    print(question)
    for answer in answers[question_num]:
        print(answer)
    while True:
        guess=input("Enter a valid option(A/B/C/D): ")
        if guess.upper() == "A" or guess.upper() == "B" or guess.upper() == "C" or guess.upper() == "D":
            guesses.append(guess)
            if guess.upper() != Correct_answers[question_num]:
                print()
                print("Incorrect!")
                print(f"Correct answer is: {Correct_answers[question_num]}")
            else:
                print()
                print("Correct")
                scores+=1
            break
        else:
            continue
    question_num+=1
print("-----------------------------")
print()
print("Your guesses:",end=" ")
for guess in guesses:
    print(guess.upper(),end=" ")
print()
print("The correct answers:",end=" ")
for ans in Correct_answers:
    print(ans,end=" ")
print()
final_sore=float((scores/question_num)*100)
print(f"Your final scores({scores}/{question_num}) = {final_sore:00.2f}%")
print()
        