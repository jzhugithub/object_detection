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



| items                     | values                               |
| ------------------------- | ------------------------------------ |
| name                      | ssd1228                              |
| config file               | ssd_mobilenet_v1_fisheye_1228.config |
| super config name         | ssd_mobilenet_v1_fisheye_1023.config |
| time                      | 2017.12.28                           |
| classes                   | person, irobot                       |
| decay_steps               | 500                                  |
| data_augmentation_options | resize_image{600}                    |
| data_augmentation_options | random_vertical_flip                 |
| data_augmentation_options | random_rotate90                      |
| data_augmentation_options | random_crop_pad_image                |
| num_steps                 | 20000                                |
| min loss                  | 3.950                                |
| eval mAP@0.5IOU           | 0.8755                               |
| train mAP@0.5IOU          | 0.9301                               |
| frequency                 | 8-22Hz                               |



| items             | values                                   |
| ----------------- | ---------------------------------------- |
| name              | ssd0250104                               |
| config file       | ssd_mobilenet_v1_025_fisheye_0104.config |
| super config name | ssd_mobilenet_v1_fisheye_1228.config     |
| time              | 2018.01.04                               |
| classes           | person, irobot                           |
| feature_extractor | min_depth: 8                             |
| feature_extractor | depth_multiplier: 0.25                   |
| num_steps         | 50k                                      |
| min loss          | 5.394                                    |
| eval mAP@0.5IOU   | 0.8546                                   |
| train mAP@0.5IOU  | 0.8753                                   |
| frequency         | 11-38Hz                                  |



| items             | values                                   |
| ----------------- | ---------------------------------------- |
| name              | ssd05voc0112                             |
| config file       | ssd_mobilenet_v1_05_voc12_0112.config    |
| super config name | ssd_mobilenet_v1_05_re_voc12_0111.config |
| time              | 2018.1.12                                |
| classes           | 20                                       |
| feature_extractor | type: 'ssd_mobilenet_v1'                 |
| num_steps         | 74.45k                                   |
| min loss          | 5.395                                    |
| eval mAP@0.5IOU   | 0.3614                                   |
| train mAP@0.5IOU  | 0.7284                                   |
| frequency         |                                          |



## SSD area conv

| items             | values                                  |
| ----------------- | --------------------------------------- |
| name              | ssdac1212                               |
| config file       | ssd_mobilenet_v1_ac_fisheye_1212.config |
| super config name | ssd_mobilenet_v1_fisheye_1023.config    |
| time              | 2017.12.12                              |
| classes           | person, irobot                          |
| box_predictor     | areaconv_box_predictor{}                |
| num_steps         | 24000                                   |
| min loss          | 3.3                                     |
| eval mAP@0.5IOU   | 0.6913                                  |
| train mAP@0.5IOU  | 0.9024                                  |
| frequency         | 9-18Hz                                  |



| items                     | values                                  |
| ------------------------- | --------------------------------------- |
| name                      | ssdac1226                               |
| config file               | ssd_mobilenet_v1_ac_fisheye_1226.config |
| super config name         | ssd_mobilenet_v1_ac_fisheye_1212.config |
| time                      | 2017.12.26                              |
| classes                   | person, irobot                          |
| data_augmentation_options | resize_image{600}                       |
| data_augmentation_options | random_vertical_flip                    |
| data_augmentation_options | random_rotate90                         |
| data_augmentation_options | random_crop_pad_image                   |
| num_steps                 | 34k                                     |
| min loss                  | 1.78                                    |
| eval mAP@0.5IOU           | 0.8524                                  |
| train mAP@0.5IOU          | 0.8982                                  |
| frequency                 | 9-18Hz                                  |



## SSD retina

| items             | values                                  |
| ----------------- | --------------------------------------- |
| name              | ssdre0108                               |
| config file       | ssd_mobilenet_v1_re_fisheye_0108.config |
| super config name | ssd_mobilenet_v1_fisheye_1228.config    |
| time              | 2018.1.8                                |
| classes           | person, irobot                          |
| feature_extractor | type: 'ssd_mobilenet_v1_retinanet'      |
| num_steps         | 11.82k                                  |
| min loss          | 1,9                                     |
| eval mAP@0.5IOU   | 0.8950                                  |
| train mAP@0.5IOU  | 0.9214                                  |
| frequency         | 8-17Hz                                  |



| items                                  | values                                  |
| -------------------------------------- | --------------------------------------- |
| name                                   | ssdre0110                               |
| config file                            | ssd_mobilenet_v1_re_fisheye_0110.config |
| super config name                      | ssd_mobilenet_v1_re_fisheye_0108.config |
| time                                   | 2018.1.10                               |
| classes                                | person, irobot                          |
| anchor_generator{ssd_anchor_generator} | min_scale: 0.04                         |
| num_steps                              | 10.97k                                  |
| min loss                               | 2.14                                    |
| eval mAP@0.5IOU                        | **0.9793**                              |
| train mAP@0.5IOU                       | **0.9864**                              |
| frequency                              | 8-22Hz                                  |

## 

| items             | values                                   |
| ----------------- | ---------------------------------------- |
| name              | ssd05revoc0111                           |
| config file       | ssd_mobilenet_v1_05_re_voc12_0111.config |
| super config name | ssd_mobilenet_v1_voc12.config            |
| time              | 2018.1.11                                |
| classes           | 20                                       |
| feature_extractor | type: 'ssd_mobilenet_v1_retinanet'       |
| num_steps         | 53.88k                                   |
| min loss          | 4.953                                    |
| eval mAP@0.5IOU   | 0.3256                                   |
| train mAP@0.5IOU  | 0.5218                                   |
| frequency         |                                          |



| items             | values                                   |
| ----------------- | ---------------------------------------- |
| name              | ssd05re0111                              |
| config file       | ssd_mobilenet_v1_05_re_fisheye_0111.config |
| super config name | ssd_mobilenet_v1_re_fisheye_0110.config  |
| time              | 2018.1.11                                |
| classes           | person, irobot                           |
| feature_extractor | depth_multiplier:0.5                     |
| num_steps         | 8665                                     |
| min loss          | 3.397                                    |
| eval mAP@0.5IOU   | 0.8953                                   |
| train mAP@0.5IOU  | 0.9574                                   |
| frequency         | 9-33Hz                                   |



| items                | values                                   |
| -------------------- | ---------------------------------------- |
| name                 | ssd05re0112                              |
| config file          | ssd_mobilenet_v1_05_re_fisheye_0112.config |
| super config name    | ssd_mobilenet_v1_05_re_fisheye_0111.config |
| time                 | 2018.1.12                                |
| classes              | person, irobot                           |
| fine_tune_checkpoint | ssd05revoc0111/model.ckpt                |
| num_steps            | 18.01k                                   |
| min loss             | 3.345                                    |
| eval mAP@0.5IOU      | 0.9633                                   |
| train mAP@0.5IOU     | 0.9848                                   |
| frequency            | 8-29Hz                                   |



| items                | values                                   |
| -------------------- | ---------------------------------------- |
| name                 | ssd05re0112_2                            |
| config file          | ssd_mobilenet_v1_05_re_fisheye_0112_2.config |
| super config name    | ssd_mobilenet_v1_05_re_fisheye_0112.config |
| time                 | 2018.1.12                                |
| classes              | person, irobot                           |
| ssd_anchor_generator | reduce_boxes_in_lowest_layer:false       |
| ssd_anchor_generator | aspect_ratios:0.5,1.0,2.0                |
| num_steps            | 25k                                      |
| min loss             | 3.433                                    |
| eval mAP@0.5IOU      | 0.9599                                   |
| train mAP@0.5IOU     | 0.9876                                   |
| frequency            | 7-30Hz                                   |



| items               | values                                   |
| ------------------- | ---------------------------------------- |
| name                | ssd05_400re0113                          |
| config file         | ssd_mobilenet_v1_05_400_re_fisheye_0113.config |
| super config name   | ssd_mobilenet_v1_05_re_fisheye_0112_2.config |
| time                | 2018.1.13                                |
| classes             | person, irobot                           |
| fixed_shape_resizer | 400,400                                  |
| num_steps           | 20k                                      |
| min loss            | 3.641                                    |
| eval mAP@0.5IOU     | 0.9353                                   |
| train mAP@0.5IOU    | 0.9799                                   |
| frequency           | 7-27Hz                                   |



## SSD gradient conv

| items             | values                                  |
| ----------------- | --------------------------------------- |
| name              | ssdgc0102                               |
| config file       | ssd_mobilenet_v1_gc_fisheye_0102.config |
| super config name | ssd_mobilenet_v1_ac_fisheye_1226.config |
| time              | 2018.01.02                              |
| classes           | person, irobot                          |
| box_predictor     | gradientconv_box_predictor              |
| decay_steps       | 500                                     |
| num_steps         | 12000                                   |
| min loss          | 3.6                                     |
| eval mAP@0.5IOU   | 0.8751                                  |
| train mAP@0.5IOU  | 0.93                                    |
| frequency         | 8-21Hz                                  |



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



