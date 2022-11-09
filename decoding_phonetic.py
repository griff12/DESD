import itertools

sounds = {
    'eɪ': ['a_e', 'ai', 'ay', 'ey', 'ei', 'eigh', 'aigh'],
    'æ': ['a'],
    'i': ['ee', 'ea', 'ie', 'ei', 'i', 'y', 'e', 'ey'],
    'ɛ': ['e'],
    'ɑɪ': ['i_e', 'y_e', 'igh', 'ie'],
    'ɪ': ['i', 'y', 'e', 'ih'],
    'oʊ': ['o_e', 'o', 'oa', 'ow', 'oe', 'ough', 'ou', 'oh'],
    'ɑ': ['o', 'a'],
    'yu': ['u_e', 'ue', 'ew'],
    'ʌ': ['u', 'uh'],
    'ʊ': ['oo', 'u', 'ou', 'oul'],
    'u': ['u', 'ui', 'oo', 'ou', 'ue', 'ew', 'eu'],
    'ər': ['r', 'er', 'ir', 'or', 'ur', 'ure'],
    'ð': ['th', 'the'],
    'ɔ': ['o', 'augh', 'ough', 'aw', 'a', 'au'], 
    # '*ə': ['*'],
    'ə': ['a', 'e', 'i', 'o', 'u', 'ah', 'eh', 'ih', 'uh'],
    'dʒ': ['j'],
    'ʃ': ['sh', 'ch', 'ti', 'ss', 's'],
    'tʃ' : ['ch'],
    'k': ['k', 'c', 'ck'],
    'w': ['w', 'wh', 'u'],
    'x': ['x', 'xs', 'cs', 'ks', 'cks'],
    'y': ['y', 'i'],
    # '*y': ['#'],
    'z': ['z', 's'],
}

phonetic_desd_words = {
    'baby': [['b','eɪ','b','i']], 'one': [['w','ʌ','n']], 'boat': [['b','oʊ','t']], 'do': [['d','u']], 'car': [['k','ɑ','r']],
    'was': [['w','ʌ','z']], 'daddy': [['d','æ','d','i']], 'book': [['b','ʌ','k']], 'good': [['g','ʌ','d']], 'doll': [['d','ɑ','l']],
    'girl': [['g','ər','l']], 'apple': [['æ','p','ə','l'], ['æ','p','l']], 'they': [['ð','eɪ']], 'story': [['s','t','oʊ','r','i']], 'some': [['s','ʌ','m']],
    'above':[['ʌ','b','ʌ','v']], 'what': [['w','ʌ','t']], 'any': [['ɛ','n','i']], 'busy': [['b','ɪ','z','i']], 'night': [['n','ɑɪ','t']],
    'done': [['d','ʌ','n']], 'huge': [['h','yu','dʒ']], 'ocean': [['oʊ','ʃ','ə','n']], 'station': [['s','t','eɪ','ʃ','ə','n']], 'could': [['k','ʊ','d']],
    'because': [['b','ɪ','k','ʌ','z'],['b','ʌ','k','ʌ','z']], 'echo': [['ɛ','k','oʊ']], 'couple': [['k','ʌ','p','*ə','l']], 'eager': [['i','g','ər']], 'together': [['t','ə','g','ɛ','ð','ər']],
    'bought': [['b','ɔ','t']], 'delicious': [['d','ɪ','l','ɪ','ʃ','ə','s']], 'neighbor': [['n','eɪ','b','ər']], 'achieve': [['ə','tʃ','i','v']], 'region': [['r','i','dʒ','ə','n']],
    'malicious': [['m','ə','l','ɪ','ʃ','ə','s']], 'bureau': [['b','y','ʊ','ər','oʊ']], 'similar': [['s','ɪ','m','ə','l','ər']], 'campaign': [['k','æ','m','p','eɪ','n']], 'waltz': [['w','ɔ','l','t','s']],
    'prairie': [['p','r','ɛ','ər','i' ], ['p','r','eɪ','ər','i']], 'gadget': [['g','æ','dʒ','ɪ','t']], 'facsimile': [['f','æ','k','s','ɪ','m','ə','l','i'], ['f','æ','x','ɪ','m','ə','l','i']], 'emphasize': [['ɛ','m','f','ə','s','ɑɪ','z']], 'prescription': [['p','r','ɪ','s','k','r','ɪ','p','ʃ','ə','n']],
    'zealous': [['z','ɛ','l','ə','s']], 'clique': [['k','l','i','k']], 'atrocious': [['ə','t','r','oʊ','ʃ','ə','s']], 'catastrophe': [['k','ə','t','æ','s','t','r','ə','f','i']], 'liquidate': [['l','ɪ','k','w','ɪ','d','eɪ','t']]
}

def correct(test_word, test_answer):
    correct_answers = [] # Answers that will be accepted at the end
    for pronounciation in phonetic_desd_words[test_word]:
        possible_answers = {}
        for x, sound in enumerate(pronounciation):
            if sound in sounds:
                possible_answers[x] = sounds[sound]
            else:
                possible_answers[x] = sound

        combos = [] # Initial list of sounds that have multiple spellings   
        for sound in possible_answers.values():
            if type(sound) == list:
                combos.append(sound)
        combos = list(itertools.product(*combos)) # List of tuples with all possible combinations for sounds with multiple spellings

        # Number the places within the word which have multiple possible spellings
        template = []
        x = 0
        for sound in possible_answers.values():
            if type(sound) == list:
                template.append(str(x))
                x += 1
            else:
                template.append(sound)

        # Insert spelling possibilities at correct locations
        for combo in combos:
            answer = ''
            for sound in template:
                if sound.isalpha():
                    answer = answer + sound
                else:
                    answer = answer + combo[int(sound)]
            # Account for 'long' vowels due to ending in 'e'
            if '_e' in answer:
                answer = answer.replace('_e', '') + 'e'
                # Include assumption for long vowel, for instace 'nit' for night
                correct_answers.append(answer[:-1])
            correct_answers.append(answer)
    print(correct_answers)
    return test_answer in correct_answers

if __name__ == '__main__':
    print(correct('malicious', 'lickwidate'))
# playsound('audio_files/baby.mp3')
# time.sleep(2)
# playsound('audio_files/baby.mp3')