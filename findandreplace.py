#!/usr/bin/python3
import os
import sys
import fileinput
from Tkinter import *

fields = ('Text To Replace', 'Replace With', 'Text File')

def findreplace(entries):
  textToSearch=entries['Text To Replace'].get()
  print("Text", textToSearch)
  fileToSearch=entries['Text File'].get()
  print("Text file", fileToSearch)
  textToReplace=entries['Replace With'].get()
  print("Replace", textToReplace)
  tempFile = open( fileToSearch, 'r+' )
  for line in fileinput.input( fileToSearch ):
    if textToSearch in line :
      print('Found and Replaced!')
  f = open(fileToSearch,'r')
  filedata = f.read()
  f.close()  
  newdata = filedata.replace(textToSearch,textToReplace)
  f = open(fileToSearch,'w')
  f.write(newdata)
  f.close()



def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

if __name__ == '__main__':
  root = Tk()
  ents = makeform(root, fields)
  root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
  b1 = Button(root, text='Replace',
         command=(lambda e=ents: findreplace(e)))
  b1.pack(side=LEFT, padx=5, pady=5)
  b3 = Button(root, text='Quit', command=root.quit)
  b3.pack(side=LEFT, padx=5, pady=5)
  root.mainloop()
