#!/usr/bin/python3


def verify_text(text, info):
    ''' 
    parse the raw text for criteria (not exhaustive):
    1. name of person
    2. name of company
    3. name of hiring manager or recruiter
    4. role

    :param text: output from ingest_letter
    
    :param info: a list of relevant info to search for in the text
    
    :return: letter is valid or not
    '''

    raw_text = " ".join(text.values())

    score = 0

    if info[0] not in raw_text: # name of person
        return score

    for item in info:
        if item in raw_text:
            score += 1

    print(score/len(info))
    return score/len(info) >= 0.75



