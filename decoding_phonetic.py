# from playsound import playsound
# import time
import itertools

sounds = {
    'ʊ': ['oo', 'u', 'o', 'oul'],
    'ey': ['ai', 'a', 'ay', 'ey', 'ea', 'ei', 'eigh', 'aigh'],
    'iy': ['ee', 'ea', 'ie', 'ei', 'i', 'y', 'e'],
    'ʌ': ['u', 'o', 'ou', 'oe'],
    'ow': ['o', 'oa', 'ow', 'oe', 'ough', 'ou'],
    'uw': ['u', 'ui', 'oo', 'ou', 'ue', 'ew', 'o', 'eu', 'oe'],
    'ɑ': ['o', 'a'],
    'æ': ['a'],
    'ər': ['er', 'ir', 'or', 'ur', 'ure'],
    'ð': ['th', 'the'],
    'k': ['k', 'c', 'ch', 'ck', 'cc'],
    'l': ['l', 'll', 'le'],
    'z': ['z', 'zz', 's'],
    'p': ['p', 'pe', 'pp'],
    'r': ['r', 'rr', 're']
    # 'g': ['g', 'gg'],
    # 'd': ['d', 'dd']
}

phonetic_desd_words = {
    'baby': ['b', 'ey', 'b', 'iy'], 'one': ['w', 'ʌ', 'n'], 'boat': ['b', 'ow', 't'], 'do': ['d', 'uw'], 'car': ['k', 'ɑ', 'r'],
    'was': ['w', 'ʌ', 'z'], 'daddy': ['d', 'æ', 'd', 'iy'], 'book': ['b', 'ʌ', 'k'], 'good': ['g', 'ʌ', 'd'], 'doll': ['d', 'ɑ', 'l'],
    'girl': ['g', 'ər', 'l'], 'apple': ['æ', 'p', 'l'], 'they': ['ð', 'ey'], 'story': ['s', 't', 'ow', 'r', 'iy'], 'some': ['s', 'ʌ', 'm']
}

def correct(test_word, test_answer):
    possible_answers = {}
    for i, sound in enumerate(phonetic_desd_words[test_word]):
        if sound in sounds:
            possible_answers[i] = sounds[sound]
        else:
            possible_answers[i] = sound
    
    combos = []    
    for sound in possible_answers.values():
        if type(sound) == list:
            combos.append(sound)
    combos = list(itertools.product(*combos))
    
    template = []
    i = 0
    for sound in possible_answers.values():
        if type(sound) == list:
            template.append(str(i))
            i += 1
        else:
            template.append(sound)
    
    correct_answers = []
    for combo in combos:
        answer = ''
        for sound in template:
            if sound.isalpha():
                answer = answer + sound
            else:
                answer = answer + combo[int(sound)]
        correct_answers.append(answer)
        print(answer)
    return test_answer in correct_answers

# def run(test_word, test_answer): 
#     playsound(f'audio_files/{test_word}.mp3')
#     time.sleep(2)
#     playsound(f'audio_files/{test_word}.mp3')
#     return correct(test_word, test_answer)

if __name__ == '__main__':
    print(correct('story', 'storre'))
# playsound('audio_files/baby.mp3')
# time.sleep(2)
# playsound('audio_files/baby.mp3')