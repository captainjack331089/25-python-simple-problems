"""
Do ouyay peaksay Igpay Atinlay?

No??

How do you translate Pig Latin to English?
The rules used by Pig Latin are as follows:
If a word begins with a vowel(a,e,i,o,u), just as "yay" to the end. For example, "out" is translated into "outyay".
If it begins with a consonant, then we take all consonants before the first vowel and we put them on the end of the word. For example, "which" is translated into "ichwhay".
"""

# Change any input to "Pig Latin"(only support English)
import time
def pig_Latin_Translate(message):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    message = list(message)

    i = 0

    while message[i] not in vowel_list:
        message.append(message[i])
        message = message[(i+1):]

    pig_latin_suffix = ['y', 'a',  'y']
    message = message + pig_latin_suffix

    return(''.join(message))

if __name__ == '__main__':
    message = input('Please enter something: \n')
    print('I will translate it into Pig Latin : )')

    new_message = pig_Latin_Translate(message)
    print('Translating.....\n')
    time.sleep(1)
    print('{} ----> {}'.format(message, new_message))


