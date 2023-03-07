
import json
import random
import readline
import keyboard

initialTestingGrounds = [""]
scores = []

kFactor = 50


def expected_prob_of_winning(score1, score2):
    exponent = (score2 - score1)/400
    ans = 1/(1 + pow(10, exponent))
    return ans

def update_scores(score1, score2, win):
    if (win):
        prob = expected_prob_of_winning(score1, score2)
        score1 = score1 + (1-prob) * kFactor
        score2 = score2 - (1-prob) * kFactor
    else:
        prob = expected_prob_of_winning(score1, score2)
        score1 = score1 - (1-prob) * kFactor
        score2 = score2 + (1-prob) * kFactor
    return (score1, score2)
    
    

def update(dct, item1, item2, score):
    pass

def sort():
    pass

def results():

    print(scores)

def main():
    print("Let\'s sort this out.")
    f = open('items.json')
    items = json.load(f)['items']
    length = len(items)
    scores = [1000] * length
    print(update_scores(1000, 1000, True))

    while (True):
        one = random.randrange(0, length, 1)
        two = one
        # print
        # keyboard.on_press_key("left arrow", print("HOWDY"))
                              
        while (two==one):
            two = random.randrange(0, length, 1)
        command = input(str(items[one]) + " | " + str(items[two]) + ": ")
        print(command)
        if str(command).strip() == "l":
            print("MADE IT")
            ans = update_scores(scores[one], scores[two], True)
            print(ans)
            scores[one] = ans[0]
            scores[two] = ans[1]
        elif command == "r":
            ans = update_scores(scores[two], scores[one], True)
            scores[two] = ans[0]
            scores[one] = ans[1]
        if command == "q":
            break

    

    print(list(reversed([x for _, x in sorted(zip(scores, items))])))
    print(list(reversed(sorted(scores))))


if __name__ == "__main__":
    main()