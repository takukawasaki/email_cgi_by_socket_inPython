#!/usr/local/bin/python3

import argparse
import getpass
import poplib
import email.header
import email


POP3_SERVER = 'example.com'

def download_email(username): 
  mailbox = poplib.POP3_SSL(POP3_SERVER, '995') 
  mailbox.user(username)
  password = getpass.getpass(prompt="Enter your mail password: ") 
  mailbox.pass_(password) 
  num_messages = len(mailbox.list()[1])
  print("Total emails: {!s}".format(num_messages))
  print("Getting last message" )
  print(mailbox.retr(num_messages)[1])
  for j, i in enumerate(mailbox.retr(num_messages)[1]):
    size = len(mailbox.retr(num_messages)[1])
    if i.startswith(b'To:') or i.startswith(b'Received:') or j == size-1:
      print(i.decode('iso-2022-jp',"replace"))
      
  
  for msg in mailbox.retr(num_messages)[1]:
    print(msg.decode("iso-2022-jp","replace"))

  mailbox.quit()


def deletemail( srv,index ):
  print(srv.dele( index ))


    
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Email Download')
  parser.add_argument('--username', action="store", dest="username", default='@realm00.com')
  given_args = parser.parse_args() 
  username = given_args.username
  download_email(username)


