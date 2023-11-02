# Exercise 5: Pets

# Answer:

pets = []

pet1 = {"kind": "\033[1mCub\033[1m", 
        "owner": "\033[1mJennie\033[1m"}
pet2 = {"kind": "\033[1mBunny\033[1m", 
        "owner": "\033[1mJisoo\033[1m"}
pet3 = {"kind": "\033[1mChick\033[1m", 
        "owner": "\033[1mLalisa\033[1m"}
pet4 = {"kind": "\033[1mHamster\033[1m", 
        "owner": "\033[1mRosé\033[1m"}
pet5 = {"kind": "\033[1mSnake\033[1m", 
        "owner": "\033[1mJimin\033[1m"}


pets = [pet1, pet2, pet3, pet4, pet5]


for pet in pets:
    print ("Kind of Animal:", pet["kind"])
    print ("Owner's Name:", pet["owner"])
    print() 
