#!/usr/bin/python

#import relevant
import RPi.GPIO as GPIO
import time
import pyaudio
import wave
from scipy.fftpack import fft
from scipy.io import wavfile



def snapshot(filename):
    print('Taking picture')
    bashCommand = "fswebcam -r 1280x720 {}.jpg".format('/home/pi/Documents/CatProject/'+filename)
    #TODO take a picture, save with filename


def record(filename):
    #TODO save a short wav file

def squirt():
    #TODO squirt water

def testSound(filename):
    #TODO analysis on sound, return TRUE if the cats are up to no good!

    ### do fourier analysis on wav-file
    data = wavfile.read(filename+ '.wav') # load the data
    a = data.T[0] # this is a two channel soundtrack, I get the first track
    b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    c = fft(b) # calculate fourier transform (complex numbers list)
    d = len(c)/2  # you only need half of the fft list (real signal symmetry)

def writeLog():
    #TODO write log with time, event and potential filename

snapshot('test')
