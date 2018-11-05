#!/usr/bin/env bash

PIPELINE_CONFIG_PATH=/home/zj/my_workspace/object_detection/configs/ssd_mobilenet_v1_fisheye2_1105.config
# PATH_TO_YOUR_PIPELINE_CONFIG, example: data/pipeline.config

CHECKPOINT_DIR=/home/zj/my_workspace/fisheye_object_detect/models/model/train
# PATH_TO_TRAIN_DIR, example: models/model/train

EVAL_DIR=/home/zj/my_workspace/fisheye_object_detect/models/model
# PATH_TO_EVAL_DIR, example: models/model
# Note: There is no 'eval' or 'eval_train' at the end of path


while(true)
do
python my_workspace/object_detection/object_detection/eval_once.py \
    --logtostderr \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --checkpoint_dir=${CHECKPOINT_DIR} \
    --eval_dir=${EVAL_DIR}/eval

python my_workspace/object_detection/object_detection/eval_once.py \
    --eval_training_data=True \
    --logtostderr \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --checkpoint_dir=${CHECKPOINT_DIR} \
    --eval_dir=${EVAL_DIR}/eval_train
echo 'wait next turn'
sleep 500
done

