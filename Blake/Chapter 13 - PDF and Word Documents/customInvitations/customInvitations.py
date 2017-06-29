#! python3
# customInvitation.py - Read in text file of guests from the command line, then generate a Word document with custom
# invitations.
# Since Python-Docx can use only those styles that already exist in the
# Word document, you will have to first add these styles to a blank Word file
# and then open that file with Python-Docx.

import sys,os,docx

invitationListFilePath = os.path.abspath(sys.argv[1])
invitationListFile = open(invitationListFilePath)
invitationList = invitationListFile.read()

templateFile = "InvitationTemplate.docx"
doc = docx.Document(templateFile)

