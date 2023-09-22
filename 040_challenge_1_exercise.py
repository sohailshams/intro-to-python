# Video alternative: https://youtu.be/qDWyR0XpJtQ&t=1295s

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
    long_strings = get_long_strings(words)
    ellipsis_string = correct_long_ellipsis_string(long_strings)
    result = correct_format(ellipsis_string) 
    return result

def get_long_strings(words):
    long_words = []
    for word in words:
        if len(word) >= 10 and not '-' in word:
            long_words.append(word)
    return long_words

def correct_long_ellipsis_string(long_strings):
    ellipsis_long_words = []
    for word in long_strings:
        if len(word) < 15:
            ellipsis_long_words.append(word)
        else:
            ellipsis_string = word[0:15] + '...'
            ellipsis_long_words.append(ellipsis_string)
    return ellipsis_long_words

def correct_format(ellipsis_string):
  print('ellipsis_string', len(ellipsis_string))
  result = 'These words are quite long:'
  count = 0
  if len(ellipsis_string) == 0:
      result += ' '
      
  for word in ellipsis_string:
      if count > 0:
          result += ','

      result += ' ' + word
      count +=1

  return result



check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
