'''You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is *z*."
e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5
L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3
Love Score = 53
Print: "Your score is 53."
These functions will help you:
lower() count()'''

name1 = str(input('What is your name? '))
name2 = str(input('What is the name of the other person? '))
combined_names = name1 + name2
lower_names = combined_names.lower().strip()
t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')
first_digit = t + r + u + e

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')
second_digit = l + o + v + e

score =  int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print('Your score is {}, you go together like coke and mentos.'.format(score))
elif (score >= 40) and (score <= 50):
    print('Your score is {}, you are alright together'.format(score))
else:
    print('Your score is {}'.format(score))




