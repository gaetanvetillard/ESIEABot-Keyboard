from motors import *
import tty, sys, termios

if initRasp():
  print("Erreur lors de l'initialisation de la carte")
else:
  print("Ok")

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
x = 0
while 1:
  x=sys.stdin.read(1)[0]

  if x:
    if x == "z": forward()
    elif x == "s": backward()
    elif x == "q": leftSpin()
    elif x == "d": rightSpin()
    elif x == "t": stop()
  else: 
    stop()
  
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)