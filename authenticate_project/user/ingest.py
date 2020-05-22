#!/usr/bin/python3

# take in pdf, clean it up, spit out text

import PyPDF2


def get_user_info():
    '''
    helper for terminal interface

    asks for:
    1. name of person
    2. email of person 
    3. filepath
    4. role
    5. name of company
    6. name of hiring manager
    7. email of hiring manager
    8. name of recruiter
    9. email of recruiter
    '''
    info = input("Enter comma separated info: ")
    split_info = info.split(",")

    info_dict = {"person_name": split_info[0],
    "person_email": split_info[1],
    "path": split_info[2],
    "role": split_info[3],
    "company_name": split_info[4],
    "manager_name": split_info[5], 
    "manager_email": split_info[6],
    "recruiter_name": split_info[7],
    "recruiter_email": split_info[8]}
    
    return info_dict



def ingest_letter(path):
    '''
    return raw text of the pdf letter

    :param path: local filepath of the letter
    :return: {page_num: text, ...}
    '''

    try: 
        pdf_file_obj = open(path,'rb')
    except OSError as err:
        raise err
    
    text = {} # page_num: text
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    for i in range(pdf_reader.numPages):
        text[i] = pdf_reader.getPage(i).extractText()
    
    return text