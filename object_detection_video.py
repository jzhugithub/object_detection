#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
import math
from object_detection_image import DetectImage


class DetectVideo(object):
    # parameters need to modify
    # video
    video_input_path = os.path.join(os.path.abspath('./video_input'), '328.avi')
    show_video_flag = True
    save_video_flag = False
    video_rate_defult = 30
    video_output_path = os.path.join(os.path.abspath('./video_output'), 'out.avi')
    VIDEO_WINDOW_NAME = 'detect_result'
    # detect
    # Create DetectImage class
    OBJECT_DETECTION_PATH = '/home/zj/program/models/object_detection'
    # Path to frozen detection graph. This is the actual model that is used for the object detection.
    PATH_TO_CKPT = os.path.join(OBJECT_DETECTION_PATH, 'ssd_mobilenet_v1_coco_11_06_2017/frozen_inference_graph.pb')
    # List of the strings that is used to add correct label for each box.
    PATH_TO_LABELS = os.path.join(OBJECT_DETECTION_PATH, 'data/mscoco_label_map.pbtxt')
    NUM_CLASSES = 90


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
        while not stop:
            # video
            success, self.src = self.video_cap.read()
            if not success:
                print('video end')
                break

            # detect
            # self.src_3 = cv2.resize(self.src_3,(160, 120))
            self.dst = self.di.run_detect(self.src)[0]

            # save and show video
            if self.save_video_flag:
                self.video_writer.write(self.dst)
            if self.show_video_flag:
                cv2.imshow(self.VIDEO_WINDOW_NAME, self.dst)
                # cv2.waitKey(1)
            # stop video vis keyboard
            if cv2.waitKey(1) >= 0:
                stop = True


if __name__ == '__main__':
    print('opencv: ' + cv2.__version__)
    dv = DetectVideo()
    if dv.video_open_flag:
        dv.run()
