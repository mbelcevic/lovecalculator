name1 = input("Enter first and last name")
name2 = input("Enter another first and last name")


def calculate_love_score(name1, name2):
    # Combine both names into one string and convert to lower case
    combined_names = (name1 + name2).lower()
    
    # Calculate the score for the word "TRUE"
    true_count = sum(combined_names.count(letter) for letter in "true")
    
    # Calculate the score for the word "LOVE"
    love_count = sum(combined_names.count(letter) for letter in "love")
    
    # Combine the counts to form a two-digit love score
    love_score = int(f"{true_count}{love_count}")
    
    # Generate the appropriate message based on the love score
    if love_score < 10 or love_score > 90:
        message = f"Your score is {love_score}, you go together like coke and mentos."
    elif 40 <= love_score <= 50:
        message = f"Your score is {love_score}, you are alright together."
    else:
        message = f"Your score is {love_score}."
    
    print(message)
    
calculate_love_score(name1, name2)