#!/usr/bin/python3

import ingest
import verify
import send

#ex info line: Neil Palleti,vvsharma21@berkeley.edu,salesforce_offer.pdf,Software Engineer intern,Salesforce,Shivakarthik,kurnoolsaketh@berkeley.edu,idk,idk

if __name__ == "__main__":
    info = ingest.get_user_info()
    text = ingest.ingest_letter(info["path"])

    verify_deets = [info["person_name"],info["company_name"],
    info["manager_name"],info["role"]]

    if verify.verify_text(text, verify_deets):
        # send email to manager
        send.send(info["manager_email"],"[AUTHENTICATOR] THIS IS A TEST",send.HIRING_SAMPLE_CONTENT)

        # send confirmation email to person
        info_values = list(info.values())
        content = "<strong>Here's what we receieved from you:</strong>\
            <br>your name: {}\
            <br>your email: {}\
            <br>filepath: {}\
            <br>role: {}\
            <br>company name: {}\
            <br>manager name: {}\
            <br>manager email: {}\
            <br>recruiter name: {}\
            <br>recruiter email: {}".format(info_values[0],
                                    info_values[1],
                                    info_values[2],
                                    info_values[3],
                                    info_values[4],
                                    info_values[5],
                                    info_values[6],
                                    info_values[7],
                                    info_values[8])

        send.send(info["person_email"],"[AUTHENTICATOR] Confirmation",content)
    
    else:
        print("REJECTED\n")