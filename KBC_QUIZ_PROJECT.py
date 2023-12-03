### quiz
questions = ["What is the full form of JS?", "What is the extention of python file ?", "what is the capital of india?",
             "what is largest plant in the solar system?", "who is virat kohli?"]
options = [["Java Solution", "Jordan Server", "Java Script", "None of these"], [".pt", ".po", ".pn", ".py"],
           ["delhi", "morena", "gwalior", "goa"], ["mars", "jupiter", "venus", "earth"],
           ["actor", "criketer", "astronot", "youtuber"]]
answers = [3, 4, 1, 2, 2]
padav_1 = 0

# print(options[0][answers[0]-1])
# print(options[1][answers[1]-1])

prize_money = [1000, 2000, 3000, 4000, 5000]
your_winning = 0
rightans = 0
wrongans = 0
padav_money = 0


def fifty_fifty(answers, i):
    ans = int(input("Enter first  option (Ex- 1/2/3/4) - "))
    if (answers[i] == ans):
        return True
    else:
        ans = int(input("Enter second option (Ex- 1/2/3/4) - "))
        if (answers[i] == ans):
            return True
        else:
            return False


def flip_question():
    flip_interest = ["cricket", "politics"]
    flip_questions = [["who is current captain of india cricket team?"], ["who was first lady prime minister?"]]
    flip_option = [["virat", "rohit", "axar", "samson"], ["siddhi", "indhra", "sheela", "mamta"]]
    flip_answer = [1, 1]
    print("1. Cricket\n 2. Politics")

    ints = int(input("choose your intrest cricket(type 1) or politics(type 2)"))
    print("Q. ", flip_questions[ints - 1][0])

    for j in range(len(flip_option[ints - 1])):
        print(j + 1, ". ", flip_option[ints - 1][j], sep="")

    ans = int(input("Enter first  option (Ex- 1/2/3/4) - "))
    if (flip_answer[ints - 1] == ans - 1):
        return True
    else:
        return False


for i in range(len(questions)):
    print("Q. ", questions[i])

    for j in range(len(options[i])):
        print(j + 1, ". ", options[i][j], sep="")
    nx = input('do you want to attempted this question ? ( yes or no )')
    if nx == 'no':
        break

    lf = input('do you want to take lifeline? ( yes or no )')
    if lf == "no":
        ans = int(input("Enter correct option (Ex- 1/2/3/4) - "))

        if (answers[i] == ans):
            your_winning = prize_money[i]
            rightans += 1
            print("Right Answer")
            if i >= 1 and i < 3:
                padav_money = 2000
            elif i >= 3:
                padav_money = 4000

        else:
            print("wrong answer")
            wrongans = 1
            break
        print()

    else:
        lifeline_want = int(
            input("which life line do u want to take?(for fifty_fifty type 1 and for flip_question type 2)"))
        if lifeline_want == 1:
            check_fifty_fifty = fifty_fifty(answers, i)
            if (check_fifty_fifty == True):
                your_winning = prize_money[i]
                rightans += 1
                print("Right Answer")
                if i >= 1 and i < 3:
                    padav_money = 2000
                elif i >= 3:
                    padav_money = 4000
            else:
                wrongans = 1
                break

        elif lifeline_want == 2:
            check_flip_question = flip_question()
            if (check_flip_question == True):
                your_winning = prize_money[i]
                rightans += 1
                print("Right Answer")
                if i >= 1 and i < 3:
                    padav_money = 2000
                elif i >= 3:
                    padav_money = 4000
            else:
                wrongans = 1
                break

if (wrongans == 1):

    print("Total prize money - 5000")
    print("Right answers - ", rightans)
    print("your winning - ", padav_money)

else:
    print("Total prize money - 5000")
    print("Right answers - ", rightans)
    print("your winning - ", your_winning)
