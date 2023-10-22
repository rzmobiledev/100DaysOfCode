# TODO: Create a letter using starting_letter.txt
with open("./input/Letters/starting_letter.txt", mode="r") as f:
    letters = f.read()

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
with open("./input/Names/invited_names.txt", mode="r") as name:
    all_names = name.read().split()
    for guest in all_names:
        # Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{guest}.txt", mode="w") as w:
            w.write(letters.replace("[name]", guest))
