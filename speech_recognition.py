import speech_recognition as sr

# mic = sr.Microphone()
r = sr.Recognizer()

print ('Listening....')

with mic as source:
	r.adjust_for_ambient_noise (source)
	audio = r.listen (source)