def emoji_to_text_converter(emoji):
    emoji_dict = {
        "😊": "Smile",
        "😢": "Sad",
        "👍": "Thumbs up",
        "👎": "Thumbs down",
        "❤️": "Heart",
        # Add more emojis and their meanings as needed
    }

    # Check if the given emoji is in the dictionary
    if emoji in emoji_dict:
        return emoji_dict[emoji]
    else:
        return "Unknown Emoji"

# Example usage
user_input = input("Enter an emoji: ")
result = emoji_to_text_converter(user_input)
print(f"The meaning of {user_input} is: {result}")
