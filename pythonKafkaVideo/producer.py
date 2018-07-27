# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:56:03 2017

@author
"""
#import numpy as np
import cv2

#import time

from pykafka import KafkaClient
#import logging as log
#log.basicConfig(level= log.DEBUG)

client = KafkaClient(hosts="192.168.134.101:9092")

# Assign a topic
topic_in = input('Topic name: ')
topic = client.topics[topic_in.encode('utf-8')]
producer=topic.get_sync_producer(max_request_size=2000000)

def video_emitter(video,motion_dec,producer):
    # Open the video
    try:

        if video == '0':
            video=0
        else:
            video='video.mp4'
        video = cv2.VideoCapture(video)
        fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
        print(' emitting.....')
        msgsizes=[]
        # read the file
        while (video.isOpened):
            # read the image in each frame
            success, image = video.read()
            if motion_dec == 1:
                image = fgbg.apply(image)
#            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # check if the file has read to the end
            if not success:
                break
            # convert the image png
            ret, jpeg = cv2.imencode('.jpg', image)
            msg=None
            # Convert the image to bytes and send to kafka
            if msg==jpeg.tobytes():
                print("skip")
                continue
            else:
                msg=jpeg.tobytes()
            msgsizes.append(len(msg))
            producer.produce(msg)
            cv2.imshow('framein',image)
#            time.sleep(.5)
            if cv2.waitKey(1) & 0xFF == 27:
                break

        video.release()
        cv2.destroyAllWindows()
        #producer.stop()
        print('done emitting',sum(msgsizes)/1000/1000,len(msgsizes),max(msgsizes)/1000/1000)
    except Exception as e:
        video.release()
        cv2.destroyAllWindows()
        print(e)
if __name__ == '__main__':
    vname=input("Select video source (0 = live / 1 = file): ")
    motion_dec=int(input('Use foreground extraction? (1 = yes / 0 = no)'))
    video_emitter(vname,motion_dec,producer)
