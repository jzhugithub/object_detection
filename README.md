# object_detection

## Before Start

Follow `Tensorflow Object Detection API` in `tensorflow/models` to prepare environment before running.

Tensorflow Object Detection API: https://github.com/tensorflow/models/tree/master/object_detection .

**Note**: Protobuf should be 2.6 version, you can get version by `protoc --version`, upgrade Protobuf by website: http://blog.csdn.net/sparkexpert/article/details/73456767 .

## object_detection_tutorial.py

Load images to detect. 

Modify from `tensorflow/models/object_detection/object_detection_tutorial.ipynb`.

Use `skimage.io` to read image which is faster than `PIL`.

## object_detection_image.py

Load images to detect. 

Contain a class of object_detection named `DetectImage`.

**Note**: Before using DetectImage, `OBJECT_DETECTION_PATH`, `PATH_TO_CKPT`, `PATH_TO_LABELS` and `NUM_CLASSES` should be modified.

## object_detection_video.py

Load a video or camera to detect. 

**Note**: 
1. OpenCV with ffmpeg is needed. 
2. Some parameters need to modify, you can find them all in DetectVideo class. 

## create_tf_record.py

Some parameters need to modify, you can find them at the head of file which labeled as `# modify`.