date =  input("ENter today`s date: ")
mood = input("How do you rate mood today from 1 to 10?:")
thoughts = input("let your thoughts flow: \n")

with open("files/journal/{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)