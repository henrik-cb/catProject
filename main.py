#!/usr/bin/python

#import relevant
#import RPi.GPIO as GPIO
import time
#import pyaudio
#import wave
import subprocess
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy
#import matplotlib.pyplot as plt



def snapshot(filename):
    print('Taking picture')
    bashCommand = "fswebcam -S 10 -r 1280x720 {}.jpg".format('/home/pi/Documents/CatProject/'+filename)
    subprocess.run(bashCommand.split())


def record(sec,filename):
    #sec = 5
    print('Recording {} seconds'.format(sec))
    bashCommand = "arecord --duration={} {}.wav".format(sec,'/home/pi/Documents/CatProject/'+filename)
    subprocess.run(bashCommand.split())

def squirt():
    #TODO squirt water i.e. turn on GPIO to relay for a few seconds
    print('nothing')

def testSound(filename):
    ### do fourier analysis on wav-file
    rate, data = wavfile.read(filename+ '.wav') # load the data
    wavPart = data
    wavNormalised=[(ele/2**8.)*2-1 for ele in wavPart] # this is 8-bit track, b is now normalized on [-1,1)
    wavFFT = fft(wavNormalised) # calculate fourier transform (complex numbers list)
    lenWav = round(wavFFT.size/2)
    realFFT = abs(wavFFT[:(lenWav - 1)])   # you only need half of the fft list (real signal symmetry)

    #TODO match d with prerecorded

    #log files for training of algorithm
    numpy.savetxt(filename + 'WAV.csv',wavNormalised)
    numpy.savetxt(filename + 'FFT.csv',realFFT)

    return False

def writeLog():
    #TODO write log with time, event and potential filename
    print('nothing')

#record(5,'test')
#testSound('test')
