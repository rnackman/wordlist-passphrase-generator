from sys import argv
import random
import requests

# Get long word list.
r = requests.get('https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt')
words_txt = r.text

def parse_txt(txt):
  code_words = []

  lines = txt.splitlines()
  for code_word in lines:
    code_words.append(code_word.split('\t'))

  return dict(code_words)

def get_random_int():
  return str(random.randint(1,6))

def get_passcode(num_digits):
  passcode = ''

  for i in xrange(num_digits):
    passcode += get_random_int()

  return passcode

def get_passcodes(num_passcodes, len_passcodes):
  passcodes = []

  for i in xrange(num_passcodes):
    passcodes.append(get_passcode(len_passcodes))

  return passcodes

def get_word(code, dictionary):
  return dictionary[code]

def get_passphrase(length):
  dictionary = parse_txt(words_txt)
  passcodes = get_passcodes(int(length), 5)
  passphrases = []

  for passcode in passcodes:
    passphrases.append(get_word(passcode, dictionary))

  passphrase = ' '.join(passphrases)
  return passphrase

def passphrase():
  print "How long do you want your passphrase to be?"
  prompt = "Please enter a number of words: "
  passphrase_length = int(raw_input(prompt))

  return get_passphrase(passphrase_length)
