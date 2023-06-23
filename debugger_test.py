# from https://www.udemy.com/course/the-python-mega-course/learn/lecture/34604378#search

# text = "I love sun"
# word = "love"
#
# words = text.split(" ")
# count = text.count(word)
#
# frequency = count / len(words) * 100
#
# print(frequency)

message = "Hello"

import glob

def get_frequency(text, word):
    words = text.split(" ")
    count = text.count(word)
    glob.glob("*")
    frequency = count / len(words) * 100
    return frequency

frequency = get_frequency("I love sun", "love")
print(frequency)

if frequency > 5:
    print("High frequency")
else:
    print("Low frequency")
print(message)