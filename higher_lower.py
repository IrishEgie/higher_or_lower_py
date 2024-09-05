import art
import gamedata as gd
import random as rd

print(art.logo)

def fetch_a():
    a = gd.data[rd.randint(0, 50)-1]# a is int
    return a
    
def fetch_b():
    b = gd.data[rd.randint(0, 50)-1]
    return b
     # b is int

fetc_gd = {
    "a":fetch_a,
    "b":fetch_b
        }

#key is string
def name(key):
    name = fetc_gd[key]()["name"]
    return name
def desc(key):
    desc = fetc_gd[key]()["description"]
    return desc
def country(key):
    country = fetc_gd[key]()["country"]
    return country
def follower_count(key):
    follower_count = fetc_gd[key]()["follower_count"]
    return follower_count

print(f"Compare A: {name("a")}, a {desc("a")}, from {country("a")}.")
a_fc = follower_count("a")

print(art.vs)

b_fc = follower_count("b")
print(f"Compare B: {name("b")}, a {desc("b")}, from {country("b")}: ")
play = input().lower()



# restart = True
# while restart:







# print("\n"*20)