# import streamlit as st
# from playsound import playsound
# import time
import itertools

sounds = {
    'ʊ': ['oo', 'u', 'o', 'ould'],
    'ey': ['ai', 'a', 'ay', 'ey', 'ea', 'ei', 'eigh', 'aigh'],
    'iy': ['ee', 'ea', 'ie', 'ei', 'i', 'y']
}

phonetic_desd_words = {
    'baby': ['b', 'ey', 'b', 'iy']
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


if __name__ == '__main__':
    print(correct('baby', 'babee'))
# playsound('audio_files/baby.mp3')
# time.sleep(2)
# playsound('audio_files/baby.mp3')