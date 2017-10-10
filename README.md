# object_detection

## Before Start

**To Train Model**

Look at my `Evernote` for details.

Follow `Tensorflow Object Detection API` in `tensorflow/models` to prepare environment before running.

Tensorflow Object Detection API: https://github.com/tensorflow/models/tree/master/research/object_detection .

**Note**

Protobuf should be 2.6 version, you can get version by `protoc --version`, upgrade Protobuf by website: http://blog.csdn.net/sparkexpert/article/details/73456767 .

**To Use Own Model**

1. cd to `my_workspace/object_detection`, input: `protoc object_detection/protos/*.proto --python_out=.`
2. open `.bashrc` and add `export PYTHONPATH=/home/zj/my_workspace/object_detection:$PYTHONPATH`
3. cd to `my_workspace/object_detection` to test installation of own model, input: `python object_detection/builders/model_builder_test.py`

## object_detection_tutorial.py

Load images to detect. 

Modify from `tensorflow/models/research/object_detection/object_detection_tutorial.ipynb`.

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

## configs/

Some .config files write by me.

## object_detection/

Copy from `Tensorflow Object Detection API` in `tensorflow/models` and add my own codes.
