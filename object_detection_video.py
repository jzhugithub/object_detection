#! /usr/bin/env python
# -*- coding=utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import cv2
import numpy as np
import math
import time
from object_detection_image import DetectImage


class DetectVideo(object):
    # parameters need to modify
    # video
    video_input_path = '/home/zj/database/record_fisheye_2_25/fisheye_2_25_20_07/fisheye_2_25_20_07_square.avi'
    show_video_flag = True
    save_video_flag = False
    video_rate_defult = 30
    video_output_path = os.path.join(os.path.abspath('./video_output'), 'out.avi')
    VIDEO_WINDOW_NAME = 'detect_result'
    # detect
    # Create DetectImage class
    OBJECT_DETECTION_PATH = '/home/zj/program/models/object_detection'
    # Path to frozen detection graph. This is the actual model that is used for the object detection.
    PATH_TO_CKPT = '/home/zj/database/fisheye2_data/model/ssd0129/frozen_inference_graph.pb'
    # PATH_TO_CKPT = '/home/zj/database_temp/faster_rcnn_resnet101_coco_11_06_2017/frozen_inference_graph.pb'
    # List of the strings that is used to add correct label for each box.
    PATH_TO_LABELS = '/home/zj/database_temp/fisheye2_data_set/fisheye2_label_map.pbtxt'
    # PATH_TO_LABELS = '/home/zj/my_workspace/object_detection/object_detection/data/mscoco_label_map.pbtxt'
    NUM_CLASSES = 2


    # parameters do not need to modify
    # video
    video_cap = 'VideoCapture'
    video_open_flag = False
    video_rate = -1
    video_hight = -1
    video_width = -1
    video_writer = 'VideoWriter'
    # frame
    src = np.array([])
    dst = np.array([])
    # detect
    di = 'DetectImage'

    # get_hz
    frame_count = -1
    start_time = 0

    def __init__(self):
        # video
        self.video_cap = cv2.VideoCapture(self.video_input_path)
        if not self.video_cap.isOpened():
            self.video_open_flag = False
            print('video open error')
            return
        self.video_open_flag = True
        print('video is open')
        self.video_rate = self.video_cap.get(cv2.cv.CV_CAP_PROP_FPS)
        if math.isnan(self.video_rate):
            self.video_rate = self.video_rate_defult
            print('video_rate is nan, using video_rate_defult: % s' % self.video_rate_defult)
        else:
            print('video_rate: %s' % self.video_rate)
        self.video_width = self.video_cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
        print('video_width: %s' % self.video_width)
        self.video_hight = self.video_cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
        print('video_hight: %s' % self.video_hight)
        if self.save_video_flag:
            self.video_writer = cv2.VideoWriter(self.video_output_path, cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'),
                                                int(self.video_rate), (int(self.video_width), int(self.video_hight)))
        if self.show_video_flag:
            cv2.namedWindow(self.VIDEO_WINDOW_NAME)
        # detect
        self.di = DetectImage(self.PATH_TO_CKPT, self.PATH_TO_LABELS, self.NUM_CLASSES)

    def __del__(self):
        cv2.destroyAllWindows()

    def run(self):
        stop = False
        # count = 1
        while not stop:
            # video
            success, self.src = self.video_cap.read()
            if not success:
                print('video end')
                break
            # count += 1
            # if count < 2500 or count > 3700:
            #     continue

            update, hz = self.get_hz()
            if update:
                print('hz: %s' % hz)

            # detect
            # self.src_3 = cv2.resize(self.src_3,(160, 120))
            cv2.cvtColor(self.src,cv2.cv.CV_BGR2RGB,self.src)# since opencv use bgr, but tensorflow use rbg
            self.dst = self.di.run_detect(self.src)[0]
            cv2.cvtColor(self.dst, cv2.cv.CV_RGB2BGR,self.dst)# since opencv use bgr, but tensorflow use rbg
            # self.dst = self.src[60:1020, 420:1380,:]
            
            # save and show video
            if self.save_video_flag:
                self.video_writer.write(self.dst)
            if self.show_video_flag:
                cv2.imshow(self.VIDEO_WINDOW_NAME, self.dst)
                # cv2.waitKey(1)
            # stop video vis keyboard
            if cv2.waitKey(1) >= 0:
                stop = True

    def get_hz(self):
        self.frame_count += 1
        update = False
        hz = -1

        if self.frame_count == 0:
            self.start_time = time.time()
            return update, hz

        if self.frame_count % 10 == 0:
            update = True
            hz = 10 / (time.time() - self.start_time)
            self.start_time = time.time()

        return update, hz


if __name__ == '__main__':
    print('opencv: ' + cv2.__version__)
    dv = DetectVideo()
    if dv.video_open_flag:
        dv.run()
