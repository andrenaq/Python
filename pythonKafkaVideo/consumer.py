# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:57:47 2017

@author
"""
from flask import Flask, Response
from kafka import KafkaConsumer
#import logging as log
#log.basicConfig(level= log.DEBUG)

topic = input('Topic name: ')

#connect to Kafka server and pass the topic we want to consume
consumer = KafkaConsumer(topic, group_id='view', bootstrap_servers=['192.168.134.101:9092'])
#Continuously listen to the connection and print messages as recieved
app = Flask(__name__)

@app.route('/')
def index():
    # return a multipart response
    return Response(kafkastream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
def kafkastream():
    for msg in consumer:
        yield (b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + msg.value + b'\r\n\r\n')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)