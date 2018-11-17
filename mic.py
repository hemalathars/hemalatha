import speech_recognition as speech_recognition

#record audio
r = sr .recognizer()
with sr .microphone() as source:
	r .adjust_for ambidient_noise(source,duration=5)
	r.dynamic_energy_threshold = true
	print("say something!")
	audio = r .listen(source)

# speech recognition using google speech recognition
try:
	# for testing purpose, we're just using the default API key
	# to use another APY key, use r .recognize_google(audio, key="google_speech_recognition_API_key")
	print("you said: " + r.recognize_google(audio))
except sr .unknownvalueerror:
	print("google speech recognition could not understand audio")
except sr .requesterror as e:
	print("could not request results from google speech recognition service; {0}" .format(e))


