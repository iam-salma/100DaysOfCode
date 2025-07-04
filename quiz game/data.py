import requests

PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=PARAMETERS)
response.raise_for_status()
data = response.json()
question_data = data["results"]

# question_data = [
#     {"question": "A slug's blood is green.", "correct_answer": "True"},
#     {"question": "The loudest animal is the African Elephant.", "correct_answer": "False"},
#     {"question": "Approximately one quarter of human bones are in the feet.", "correct_answer": "True"},
#     {"question": "The total surface area of a human lungs is the size of a football pitch.", "correct_answer": "True"},
#     {"question": "In West Virginia, USA, if you accidentally hit an animal with your car,"
#                  " you are free to take it home to eat.", "correct_answer": "True"},
#     {"question": "In London, UK, if you happen to die in the House of Parliament,"
#                  " you are entitled to a state funeral.", "correct_answer": "False"},
#     {"question": "It is illegal to pee in the Ocean in Portugal.", "correct_answer": "True"},
#     {"question": "You can lead a cow down stairs but not up stairs.", "correct_answer": "False"},
#     {"question": "Google was originally called 'Backrub'.", "correct_answer": "True"},
#     {"question": "Buzz Aldrin's mother's maiden name was 'Moon'.", "correct_answer": "True"},
#     {"question": "No piece of square dry paper can be folded in half more than 7 times.", "correct_answer": "False"},
#     {"question": "A few ounces of chocolate can to kill a small dog.", "correct_answer": "True"}
# ]
