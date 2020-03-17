import speech_recognition as sr
import multiprocessing
import time


def record(conn, r):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=2)
        print('nayn')
        conn.send(audio)
        conn.close()

def transcript(conn, r):
    while True:
        audio = conn.recv()
        transcript_str = r.recognize_google(audio, language='ru-RU')
        print (transcript_str)
        break

if __name__ == '__main__':
    r = sr.Recognizer()
    one_conn, two_conn = multiprocessing.Pipe()

    while True:
        p1 = multiprocessing.Process(target=record, args=(one_conn, r))
        p2 = multiprocessing.Process(target=transcript, args=(two_conn, r))
        p1.start()
        p2.start()
        p1.join()
        p2.join()



# import multiprocessing
#
# def one(conn, msgs):
#     for i in range(4):
#         for j in msgs:
#             conn.send(j)
#     conn.close()
#
# def two(conn, i):
#     while 1:
#         i += 1
#         j = conn.recv()
#         print(str(i) + ': ' + j)
#
# i = 0
# msgs = ['kill me!', 'lalala', 'all people lalkas']
# one_conn, two_conn = multiprocessing.Pipe()
#
# p1 = multiprocessing.Process(target=one, args=(one_conn, msgs))
# p2 = multiprocessing.Process(target=two, args=(two_conn, i))
# p1.start()
# p2.start()
# p1.join()
# p2.join()
#
