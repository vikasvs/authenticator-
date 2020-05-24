#!/usr/bin/python3

from .ingest import ingest_letter
from .verify import verify_text
from .send import send

#ex info line: Neil Palleti,vvsharma21@berkeley.edu,salesforce_offer.pdf,Software Engineer intern,Salesforce,Shivakarthik,kurnoolsaketh@berkeley.edu,idk,idk

HIRING_SAMPLE_CONTENT = "<strong>TEST HIRING MANAGER EMAIL</strong>"

def verify_and_send(form):
    #info = ingest.get_user_info()
    
    info = form.cleaned_data

    text = ingest_letter("documents/{}".format(info["offer_letter"]))

    verify_deets = [info["your_name"],info["company_name"],
    info["manager_name"],info["role"]]

    if verify_text(text, verify_deets):
        #send email to manager
        # TODO: send link to manager to access employee profile
        send(info["manager_email"],"[AUTHENTICATOR] THIS IS A TEST",HIRING_SAMPLE_CONTENT)
    else:
        print("FALSE")
        return False

    # send confirmation email to person
    info_values = list(info.values())
    content = "<strong>Here's what we receieved from you:</strong>\
        <br>your name: {}\
        <br>your email: {}\
        <br>role: {}\
        <br>company name: {}\
        <br>manager name: {}\
        <br>manager email: {}\
        <br>recruiter name: {}\
        <br>recruiter email: {}".format(info_values[0],
                                info_values[1],
                                info_values[3],
                                info_values[4],
                                info_values[5],
                                info_values[6],
                                info_values[7],
                                info_values[8])

    send(info["your_email"],"[AUTHENTICATOR] Confirmation",content)
    return True
    