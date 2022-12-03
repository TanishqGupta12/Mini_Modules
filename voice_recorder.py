import sounddevice as sd

from scipy.io.wavfile import write

fs=44100

second=int(input("Enter the time duration in second"))

print("Recording...................\n")

record_voice=sd.rec(int(second * fs ) , samplerate= fs , channels=2)

sd.wait()

write("out.wav" , fs , record_voice)

print("Finished.....\n Please check if/............")
