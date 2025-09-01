"""
Features and descriptions of characters
"""
import random
import argparse

def table(dict_rule, size=1024):
    def expand(dict_rule, size):
        for k, p in dict_rule.items():
            for _ in range(int(p*size)):
                yield k
    total = list(expand(dict_rule, size))
    random.shuffle(total)
    return total

# Simple spectrum
# 1, 4, 6, 4, 1
# SPECTRUM = table({"Missing": 1/16, "Smaller": 4/16, None: 6/16, "Larger": 5/16}, 16)
# Translates directly to 3d6: 3, 4-7, 8-13, 14-17, 18

# More complex:
# 1, 5, 10, 10, 5, 1
SPECTRUM = table({"Missing": 1/32, "Injured": 5/32, "Small": 10/32, None: 10/32, "Large": 6/32}, 32)
# Close to 6d6: 6, 7-11, 12-20, 21-30, 31-35, 36
# d20: 1, 2-4, 5-10, 11-17, 18-19, 20

Feature = [
"Hair Curl", "Hair Length", "Hair Coverage",
"Ears", "Eyebrows", "Eyes", "Nose",
"Facial Hair", "Teeth", "Lips", "Chin",
"Shoulders", "Arms", "Hands", "Chest", "Gut", "Hips", "Thighs", "Knees", "Feet",
"Overall Size"
]

def describe(character):
    print(character)
    random.seed(character.encode('utf-8'))
    for f in Feature:
        note = random.choice(SPECTRUM)
        if note:
            print(f"{f}: {note}")
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("names", nargs="*")
    options = parser.parse_args()
    if options.names:
        for name in options.names:
            describe(name)
    else:
        describe("Farrier")
        describe("Little Smith")

        describe("Fletcher")
        describe("Cobbler")

        describe("Swineherd")
        describe("Goatherd")

        describe("Mouth")
        describe("Big Smith")

        describe("Tinker")
