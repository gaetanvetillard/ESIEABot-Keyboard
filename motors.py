# https://github.com/WiringPi/WiringPi-Python
# https://fr.pinout.xyz/pinout/wiringpi
from wiringpi import *
from time import sleep


# CONSTANTS
LEFT_MOTOR_PIN = 7  # GPIO  4, broche enable du moteur 1
L1_MOTOR_PIN = 0  # GPIO 17, entree 1 du moteur 1
L2_MOTOR_PIN = 3  # GPIO 22, entree 2 du moteur 1
RIGHT_MOTOR_PIN = 5  # GPIO 24, broche enable du moteur 2
R1_MOTOR_PIN = 4  # GPIO 23, entree 1 du moteur 2
R2_MOTOR_PIN = 6  # GPIO 25, entree 2 du moteur 2
TRIG_PIN = 1  # GPIO 18, TRIG_PIN ultrason
ECHO_PIN = 2  # GPIO 27, ECHO_PIN ultrason


def initRasp():
  wiringPiSetup()
  
  # on definit les GPIO en sortie pour le moteur 1
  pinMode (LEFT_MOTOR_PIN, 1)
  pinMode (L1_MOTOR_PIN, 1)
  pinMode (L2_MOTOR_PIN, 1)
  
  # on definit les GPIO en sortie pour le moteur 2
  pinMode (RIGHT_MOTOR_PIN, 1)
  pinMode (R1_MOTOR_PIN, 1)
  pinMode (R2_MOTOR_PIN, 1)

  # # Activation de la modulation de la puissance fournie aux moteurs
  softPwmCreate (LEFT_MOTOR_PIN, 0, 100)
  softPwmCreate (RIGHT_MOTOR_PIN, 0, 100)
  # Affectation des pins du capteur ultrason
  pinMode (TRIG_PIN, 1)
  pinMode (ECHO_PIN, 1)

  return 0


def leftForward():
  """Activate the left motor forward"""
  softPwmWrite(LEFT_MOTOR_PIN, 100)
  digitalWrite(L1_MOTOR_PIN, 1)
  digitalWrite(L2_MOTOR_PIN, 0)


def leftBackward():
  """Activate the left motor backward"""
  softPwmWrite(LEFT_MOTOR_PIN, 100)
  digitalWrite(L1_MOTOR_PIN, 0)
  digitalWrite(L2_MOTOR_PIN, 1)


def rightForward():
  """Activate the right motor forward"""
  softPwmWrite(RIGHT_MOTOR_PIN, 100)
  digitalWrite(R1_MOTOR_PIN, 1)
  digitalWrite(R2_MOTOR_PIN, 0)


def rightBackward():
  """Activate the right motor backward"""
  softPwmWrite(RIGHT_MOTOR_PIN, 100)
  digitalWrite(R1_MOTOR_PIN, 0)
  digitalWrite(R2_MOTOR_PIN, 1)


def forward():
  """Forward (z or up arrow key)"""
  leftForward()
  rightForward()


def backward():
  """Backward (s or down arrow key)"""
  leftBackward()
  rightBackward()


def leftSpin():
  """Left spin (q or left arrow key)"""
  rightForward()
  leftBackward()


def rightSpin():
  """Right spin (d or right arrow key)"""
  leftForward()
  rightBackward()


def stop():
  """Turn off all motors"""
  softPwmWrite(LEFT_MOTOR_PIN, 0)
  digitalWrite(L1_MOTOR_PIN, 0)
  digitalWrite(L2_MOTOR_PIN, 0)
  softPwmWrite(RIGHT_MOTOR_PIN, 0)
  digitalWrite(R1_MOTOR_PIN, 0)
  digitalWrite(R2_MOTOR_PIN, 0)