# Write the user's name
name = "Oluwaseun" "Aredina"

# Print the first initial in block letters
print("Your initials in block letters are:")
print(f"  {name[0].upper()} {name[9].upper()}")
# Loop through the rest of the name and print the initial of each word in block letters
for i in range(1, len(name)):
  # Check if the current character is a space
  if name[i] == " ":
    # If it is, print the next character in upper case in block letters
    print(f"  {name[i+1].upper()}")

