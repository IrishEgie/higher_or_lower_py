import art
import gamedata as gd
import random as rd

#initialize variables
score = 0
restart = True
vs = art.vs
logo = art.logo

print(logo)

# default 
# #print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")

# print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.")
# print(f"Compare A: {b["name"]}, a {b["description"]}, from {b["country"]}: ")

while restart:
    if score>0:
        a = b
    else:
        a = {}
        a = gd.data[rd.randint(0, 50)-1]# a is dict
    b = {}
    b = gd.data[rd.randint(0, 50)-1]# b is dict
    
    a_fc = a["follower_count"]
    b_fc = b["follower_count"]

    # print(a_fc)
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.")
    print(vs) #vs art
    # print(b_fc)
    guess = input(f"Compare B: {b["name"]}, a {b["description"]}, from {b["country"]}: ").lower() #fetch user guess

    if (guess == "a" and a_fc>b_fc) or (guess == "b" and b_fc>a_fc):
        score+=1
        print(f"You're right! Current score: {score}.")
    else:
        print("\n"*20)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
        restart = False
        
