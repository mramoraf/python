# import json
# import pyaudio

# from vosk import Model, KaldiRecognizer

# model = Model('semester 2\\class 5\\classwork\\vosk-model-uk-v3-lgraph')
# recognizer = KaldiRecognizer(model, 16000)
# words = pyaudio.PyAudio()
# stream = words.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

# stream.start_stream()

# def listen():
#     while True:
#         data = stream.read(4000, exception_on_overflow=False)
#         if (recognizer.AcceptWaveform(data)) and len(data)>0:
#             answer = json.loads(recognizer.Result())
#             if answer['text']:
#                 yield answer['text']



# for text in listen():
#     if text == 'футбол' or text == 'волейбол' or text == 'баскетбол':
#         print(f'Який ваш улюблений вид спорту?')

#     print(f'User: {text}')