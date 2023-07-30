


"""
This was the first iteration of the code, once it was running correctly,
we defined a non empty input function to prevent empty data from being entered in the madlib

food = input('Food:')
person = input('Person:')
place = input('Place:')
things2 = input('Things (plural):')
animals = input('Animals (plural):')
profession = input('Proffesion:')
feeling = input('Feeling:')
things1 = input('Things (plural):')
clothes = input('Clothes (plural):')
verb = input('Verb ending in "-ing":')

"""

#nei, non empty input
def nei(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be blank. Please try again.")


print('To generate the next madlib, we are going to need the following things:')

food = nei('Food:')
person = nei('Person:')
place = nei('Place:')
things2 = nei('Things (plural):')
animals = nei('Animals (plural):')
profession = nei('Proffesion:')
feeling = nei('Feeling:')
things1 = nei('Things (plural):')
clothes = nei('Clothes (plural):')
verb = nei('Verb ending in "-ing":')


madlib = f"Say {food} the photographer said as the camera flashed! {person} and I had gone to {place} to get our photos taken today. \
The first photo we really wanted was a picture of us dressed as {animals} pretending to be a {profession}. \
When we saw the proofs of it, I was a bit {feeling} because it looked different than in my head. (I hadn't imagined so many {things1} behind us.) \
However, the second photo was exactly what I wanted. We both looked like {things2} wearing {clothes} and {verb}--exactly what I had in mind!"

print(madlib)