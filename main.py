# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

# read the 'starting_letter.txt' file
with open("./Input/Letters/starting_letter.txt") as letter_file:
    content = letter_file.read()

# read the 'invited_names.txt' file
with open("./Input/Names/invited_names.txt") as invited_names:
    # read letter line by line
    for person in invited_names.readlines():
        # Remove the new line escape sequence using strip() method
        stripped_name = person.strip()
        # write separate file for each person present in 'invited_names.txt' file
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as invitation:
            # replace the '[name]' with actual name of the person and then write
            new_letter = content.replace(PLACEHOLDER, stripped_name)
            invitation.write(new_letter)
