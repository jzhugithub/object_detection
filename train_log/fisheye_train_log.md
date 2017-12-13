# train log

## SSD

| items                   | values                               |
| ----------------------- | ------------------------------------ |
| name                    | ssd1023a                             |
| config file             | ssd_mobilenet_v1_fisheye_1023.config |
| super config name       | ssd_mobilenet_v1_zmart_0917.config   |
| time                    | 2017.10.23                           |
| classes                 | person, irobot                       |
| ssd_anchor_generator    | min_scale: 0.1, max_scale: 0.3       |
| fixed_shape_resizer     | 512, 512                             |
| min_negatives_per_image | None                                 |
| decay_steps             | 300                                  |
| num_steps               | 15000                                |
| min loss                | 2.496                                |
| eval mAP@0.5IOU         | 0.8567                               |
| train mAP@0.5IOU        | 0.9713                               |
| frequency               | 8-22Hz                               |

## SSD area conv

| items             | values                                  |
| ----------------- | --------------------------------------- |
| name              | ssdac1212                               |
| config file       | ssd_mobilenet_v1_ac_fisheye_1212.config |
| super config name | ssd_mobilenet_v1_fisheye_1023.config    |
| time              | 2017.12.12                              |
| classes           | person, irobot                          |
| box_predictor     | areaconv_box_predictor{}                |
| num_steps         | 18000                                   |
| min loss          | 3.3                                     |
| eval mAP@0.5IOU   | 0.4624                                  |
| train mAP@0.5IOU  | 0.8342                                  |
| frequency         |                                         |
|                   |                                         |
|                   |                                         |

## Faster R-CNN

| items                     | values                                   |
| ------------------------- | ---------------------------------------- |
| name                      | fr1025a                                  |
| config file               | faster_rcnn_resnet50_fisheye_1025.config |
| super config name         | faster_rcnn_resnet50_zmart_0920.config   |
| time                      | 2017.10.25                               |
| classes                   | person, irobot                           |
| keep_aspect_ratio_resizer | max_dimension: 512                       |
| manual_step_learning_rate | step: 0, step: 5000, step: 10000         |
| ssd_random_crop           | new add                                  |
| num_steps                 | 15000                                    |
| min loss                  | 0.4                                      |
| eval mAP@0.5IOU           | 0.62                                     |
| train mAP@0.5IOU          | 0.62                                     |



| items                         | values                                   |
| ----------------------------- | ---------------------------------------- |
| name                          | fr1026a                                  |
| config file                   | faster_rcnn_resnet50_fisheye_1025.config |
| super config name             | fr1025a                                  |
| time                          | 2017.10.26                               |
| first_stage_nms_iou_threshold | 0.6                                      |
| first_stage_max_proposals     | 50                                       |
| second_stage_batch_size       | 50                                       |
| iou_threshold                 | 0.4                                      |
| max_detections_per_class      | 20                                       |
| max_total_detections          | 50                                       |
| manual_step_learning_rate     | step: 0, step: 10000, step: 20000        |
| num_steps                     | 30000                                    |
| min loss                      | 0.38                                     |
| eval mAP@0.5IOU               | 0.81                                     |
| train mAP@0.5IOU              | 0.87                                     |
| frequency                     | 6-12Hz                                   |



