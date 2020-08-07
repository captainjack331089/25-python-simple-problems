"""
Am I dating myself by saying I loved Magic 8 Balls as a kid? Well, if you no longer have yours (maybe because, like me, you smashed it to see what that murky liquid was inside), then create one
"""
# Try to create a simple magic 8 ball Q&A system
import random

def magic_8_ball():
    ans_dict = {
        '1': 'Yes – definitely.',
        '2': 'Most likely.',
        '3': 'It is certain.',
        '4': 'Ask again later.',
        '5': 'Can not predict it now.',
        '6': 'My reply is no.',
        '7': 'Very doubtful',
        '8': 'Without a doubt',
    }
    answer = ans_dict[str(random.randint(1,8))]
    return answer

if __name__ == '__main__':
    q = input('Please ask a question to Magic 8 Ball...\n')
    if q:
        print(magic_8_ball())

