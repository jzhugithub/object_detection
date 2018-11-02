# train log

## SSD

| items                       | values                                   |
| --------------------------- | ---------------------------------------- |
| name                        | ssd0129                                  |
| config file                 | ssd_mobilenet_v1_fisheye2_0129.config    |
| super config name           | ssd_mobilenet_v1_fisheye_1228.config     |
| time                        | 2018.1.29                                |
| classes                     | ir, ob                                   |
| unmatched_threshold         | 0.5                                      |
| ssd_anchor_generator        | min_scale: 0.1, max_scale: 0.3,aspect_ratios:1,2,0.5,3,0.33 |
| fixed_shape_resizer         | 512, 512                                 |
| convolutional_box_predictor | 0                                        |
| feature_extractor           | type: 'ssd_mobilenet_v1'                 |
| feature_extractor           | depth_multiplier: 1.0                    |
| hard_example_miner          | min_negatives_per_image: 1               |
| min_negatives_per_image     | 1                                        |
| decay_steps                 | 2000                                     |
| decay_factor                | 0.9                                      |
| fine_tune_checkpoint        | coco                                     |
| data_augmentation_options   | random_horizontal_flip, ssd_random_crop  |
| train_input_reader          | train_origin                             |
| num_steps(time)             | 34.49k(12:49)                            |
| min loss                    | 1.911                                    |
| train mAP@0.5IOU            | 0.9466                                   |
| eval mAP@0.5IOU             | 0.9214                                   |
| test mAP@0.5IOU             | 0.9368                                   |
| frequency                   | tx2:0.0938                               |

## 

| items                    | values                                   |
| ------------------------ | ---------------------------------------- |
| name                     | ssd050130                                |
| config file              | ssd_mobilenet_v1_05_fisheye2_0130.config |
| super config name        | ssd_mobilenet_v1_fisheye2_0129.config    |
| time                     | 2018.1.30                                |
| classes                  | ir, ob                                   |
| **feature_extractor**    | **min_depth: 8, depth_multiplier: 0.5**  |
| **fine_tune_checkpoint** | **voc**                                  |
| num_steps(time)          | 22.61k(7:12)                             |
| min loss                 | 3.262                                    |
| train mAP@0.5IOU         | 0.8713                                   |
| eval mAP@0.5IOU          | 0.8615                                   |
| test mAP@0.5IOU          | 0.8779                                   |
| frequency                | 0.0697                                   |



## SSD retina

## 

| items                     | values                                   |
| ------------------------- | ---------------------------------------- |
| name                      | ssd05re0131                              |
| config file               | ssd_mobilenet_v1_05_re_fisheye2_0131.config |
| super config name         | ssd_mobilenet_v1_05_fisheye2_0130.config |
| time                      | 2018.1.31                                |
| classes                   | ir, ob                                   |
| unmatched_threshold       | 0.5                                      |
| ssd_anchor_generator      | min_scale: 0.1, max_scale: 0.3,aspect_ratios:1,2,0.5,reduce_boxes_in_lowest_layer: false |
| fixed_shape_resizer       | 512, 512                                 |
| retinanet_box_predictor   | **use_depthwise_before_predictor: true, share_parameter: true, num_layers_before_predictor: 2** |
| feature_extractor         | type: '**ssd_mobilenet_v1_retinanet**', depth_multiplier: 0.5 |
| classification_loss       | **weighted_focal{alpha: 0.25, gamma: 2.0}** |
| hard_example_miner        | **None**                                 |
| batch_size                | 24                                       |
| initial_learning_rate     | 0.0001(0-800 step), 0.004(800- step)     |
| decay_steps               | 2000                                     |
| decay_factor              | 0.9                                      |
| fine_tune_checkpoint      | voc(not all parameters)                  |
| data_augmentation_options | **random_horizontal_flip**               |
| train_input_reader        | train_origin                             |
| num_steps(time)           | 4k                                       |
| min loss                  | 0.7619                                   |
| train mAP@0.5IOU          | 0.3593                                   |
| eval mAP@0.5IOU           | 0.3610                                   |
| test mAP@0.5IOU           |                                          |
| frequency                 |                                          |

 

| items                     | values                                   |
| ------------------------- | ---------------------------------------- |
| name                      | ssd05re0202                              |
| config file               | ssd_mobilenet_v1_05_re_fisheye2_0202.config |
| super config name         | ssd_mobilenet_v1_05_re_fisheye2_0131.config |
| time                      | 2018.2.2                                 |
| classes                   | ir, ob                                   |
| unmatched_threshold       | 0.5                                      |
| ssd_anchor_generator      | min_scale: 0.1, max_scale: 0.3,aspect_ratios:1,2,0.5,reduce_boxes_in_lowest_layer: false |
| fixed_shape_resizer       | 512, 512                                 |
| retinanet_box_predictor   | use_depthwise_before_predictor: true, share_parameter: **false,** num_layers_before_predictor: 2 |
| feature_extractor         | type: 'ssd_mobilenet_v1_retinanet', depth_multiplier: 0.5 |
| classification_loss       | weighted_focal{alpha: 0.25, gamma: 2.0}  |
| hard_example_miner        | None                                     |
| batch_size                | **20**                                   |
| initial_learning_rate     | 0.0001(0-1k step), 0.004(800- step)      |
| decay_steps               | 2000                                     |
| decay_factor              | 0.9                                      |
| fine_tune_checkpoint      | voc(not all parameters)                  |
| data_augmentation_options | random_horizontal_flip，**ssd_random_crop** |
| train_input_reader        | train_origin                             |
| num_steps(time)           | 67k                                      |
| min loss                  | 1.033                                    |
| train mAP@0.5IOU          | 0.9809                                   |
| eval mAP@0.5IOU           | 0.9400                                   |
| test mAP@0.5IOU           | 0.9434                                   |
| frequency                 | tx2:0.0626  titan:0.0164                 |



| items                     | values                                   |
| ------------------------- | ---------------------------------------- |
| name                      | ssd05re0203                              |
| config file               | ssd_mobilenet_v1_05_re_fisheye2_0202.config |
| super config name         | ssd_mobilenet_v1_05_re_fisheye2_0203.config |
| time                      | 2018.2.3                                 |
| classes                   | ir, ob                                   |
| unmatched_threshold       | 0.5                                      |
| ssd_anchor_generator      | min_scale: 0.1, max_scale: 0.3,aspect_ratios:1,2,0.5,reduce_boxes_in_lowest_layer: false |
| fixed_shape_resizer       | 512, 512                                 |
| retinanet_box_predictor   | use_depthwise_before_predictor: true, share_parameter: false, num_layers_before_predictor: 2 |
| feature_extractor         | type: 'ssd_mobilenet_v1_retinanet', depth_multiplier: 0.5 |
| classification_loss       | weighted_focal{alpha: 0.25, gamma: 2.0}  |
| hard_example_miner        | None                                     |
| batch_size                | 20                                       |
| initial_learning_rate     | 0.004                                    |
| decay_steps               | 2000                                     |
| decay_factor              | 0.9                                      |
| fine_tune_checkpoint      | voc(not all parameters)                  |
| data_augmentation_options | **resize_image, random_horizontal_flip, random_vertical_flip, random_rotate90, random_crop_pad_image** |
| train_input_reader        | **train**                                |
| num_steps(time)           | 100k                                     |
| min loss                  | 1.126                                    |
| train mAP@0.5IOU          | 0.9234                                   |
| eval mAP@0.5IOU           | 0.9328                                   |
| test mAP@0.5IOU           | 0.9347                                   |
| frequency                 |                                          |





| items                     | values                                   |
| ------------------------- | ---------------------------------------- |
| name                      | ssd05re0208                              |
| config file               | ssd_mobilenet_v1_05_re_fisheye2_0203.config |
| super config name         | ssd_mobilenet_v1_05_re_fisheye2_0208.config |
| time                      | 2018.2.8                                 |
| classes                   | ir, ob                                   |
| unmatched_threshold       | 0.5                                      |
| ssd_anchor_generator      | min_scale: 0.1, max_scale: 0.3,aspect_ratios:1,2,0.5,reduce_boxes_in_lowest_layer: false |
| fixed_shape_resizer       | 512, 512                                 |
| retinanet_box_predictor   | use_depthwise_before_predictor: true, share_parameter: false, num_layers_before_predictor: 2 |
| feature_extractor         | type: 'ssd_mobilenet_v1_retinanet', depth_multiplier: 0.5 |
| classification_loss       | weighted_focal{alpha: 0.25, gamma: 2.0}  |
| hard_example_miner        | None                                     |
| batch_size                | 20                                       |
| initial_learning_rate     | 0.004                                    |
| decay_steps               | 2000                                     |
| decay_factor              | 0.9                                      |
| fine_tune_checkpoint      | voc(not all parameters)                  |
| data_augmentation_options | **random_horizontal_flip, random_vertical_flip, random_rotate90, ssd_random_crop** |
| train_input_reader        | **train_origin**                         |
| num_steps(time)           | 50k                                      |
| min loss                  | 1.098                                    |
| train mAP@0.5IOU          | 0.9194                                   |
| eval mAP@0.5IOU           | 0.9241                                   |
| test mAP@0.5IOU           | 0.9389                                   |
| frequency                 | tx:0.0631                                |

## 

| items                     | values                                   |
| ------------------------- | ---------------------------------------- |
| name                      | ssd05re0215                              |
| config file               | ssd_mobilenet_v1_05_re_fisheye2_0208.config |
| super config name         | ssd_mobilenet_v1_05_re_fisheye2_0215.config |
| time                      | 2018.2.15                                |
| classes                   | ir, ob                                   |
| unmatched_threshold       | 0.5                                      |
| ssd_anchor_generator      | min_scale: 0.1, max_scale: 0.3,aspect_ratios:1,2,0.5,reduce_boxes_in_lowest_layer: false |
| fixed_shape_resizer       | **400,400**                              |
| retinanet_box_predictor   | use_depthwise_before_predictor: true, share_parameter: false, num_layers_before_predictor: 2 |
| feature_extractor         | type: 'ssd_mobilenet_v1_retinanet', depth_multiplier: 0.5 |
| classification_loss       | weighted_focal{alpha: 0.25, gamma: 2.0}  |
| hard_example_miner        | None                                     |
| batch_size                | 20                                       |
| initial_learning_rate     | 0.004                                    |
| decay_steps               | 2000                                     |
| decay_factor              | 0.9                                      |
| fine_tune_checkpoint      | voc(not all parameters)                  |
| data_augmentation_options | random_horizontal_flip, random_vertical_flip, random_rotate90, ssd_random_crop |
| train_input_reader        | train_origin                             |
| num_steps(time)           | 50k                                      |
| min loss                  | 1.262                                    |
| train mAP@0.5IOU          | 0.8782                                   |
| eval mAP@0.5IOU           | 0.8659                                   |
| test mAP@0.5IOU           | 0.8627                                   |
| frequency                 | tx:0.0555                                |



| items                     | values                                   |
| ------------------------- | ---------------------------------------- |
| name                      | ssd05re0607                              |
| config file               | ssd_mobilenet_v1_05_re_fisheye2_0607.config |
| super config name         | ssd_mobilenet_v1_05_re_fisheye2_0208.config |
| time                      | 2018.6.7                                 |
| classes                   | ir, ob                                   |
| unmatched_threshold       | 0.5                                      |
| ssd_anchor_generator      | min_scale: 0.1, max_scale: 0.3,aspect_ratios:1,2,0.5,reduce_boxes_in_lowest_layer: false |
| fixed_shape_resizer       | 512, 512                                 |
| retinanet_box_predictor   | use_depthwise_before_predictor: true, share_parameter: false, num_layers_before_predictor: 2 |
| feature_extractor         | type: 'ssd_mobilenet_v1_retinanet', depth_multiplier: 0.5 |
| classification_loss       | weighted_focal{alpha: 0.25, gamma: 2.0}  |
| hard_example_miner        | None                                     |
| batch_size                | 20                                       |
| initial_learning_rate     | 0.004                                    |
| decay_steps               | 2000                                     |
| decay_factor              | 0.9                                      |
| fine_tune_checkpoint      | voc(not all parameters)                  |
| data_augmentation_options | **resize_image, random_horizontal_flip, random_vertical_flip, random_rotate90, random_crop_pad_image** |
| train_input_reader        | **train_origin**                         |
| num_steps(time)           | 50k                                      |
| min loss                  | 0.9792                                   |
| train mAP@0.5IOU          | 0.9427                                   |
| eval mAP@0.5IOU           | 0.9459                                   |
| test mAP@0.5IOU           | 0.9423                                   |
| frequency                 |                                          |



## Faster-RCNN



| items                     | values                                   |
| ------------------------- | ---------------------------------------- |
| name                      | fastermobilevoc1017                      |
| config file               | faster_rcnn_mobilenet_v1_voc12_1017.config |
| super config name         | faster_rcnn_resnet50_pets.config         |
| time                      | 2018.10.25                               |
| classes                   | voc                                      |
| fixed_shape_resizer       | 512, 512                                 |
| feature_extractor         | type: 'faster_rcnn_mobilenet_v1'         |
| hard_example_miner        | None                                     |
| batch_size                | 1                                        |
| initial_learning_rate     | 0.0003                                   |
| fine_tune_checkpoint      | imagenet                                 |
| data_augmentation_options | random_horizontal_flip                   |
| num_steps(time)           | 50k                                      |
| min loss                  | 0.25                                     |
| train mAP@0.5IOU          | 0.494                                    |
| eval mAP@0.5IOU           | 0.383                                    |
| test mAP@0.5IOU           |                                          |
| frequency(Titan)          |                                          |
| graphics memory(Titan)    |                                          |
| frequency(TX2)            |                                          |
| graphics memory(TX2)      |                                          |
|                           |                                          |
|                           |                                          |
|                           |                                          |
|                           |                                          |



| items                     | values                                   |
| ------------------------- | ---------------------------------------- |
| name                      | fastermobilefisheye1025                  |
| config file               | faster_rcnn_mobilenet_v1_fisheye2_1025.config |
| super config name         | faster_rcnn_mobilenet_v1_voc12_1017.config |
| time                      | 2018.10.29                               |
| classes                   | ir, ob                                   |
| fixed_shape_resizer       | 512, 512                                 |
| feature_extractor         | type: 'faster_rcnn_mobilenet_v1'         |
| hard_example_miner        | None                                     |
| batch_size                | 1                                        |
| initial_learning_rate     | 0.00003                                  |
| fine_tune_checkpoint      | voc                                      |
| data_augmentation_options | random_horizontal_flip                   |
| num_steps(time)           | 220k                                     |
| min loss                  | 0.06                                     |
| train mAP@0.5IOU          | 0.931                                    |
| eval mAP@0.5IOU           | 0.903                                    |
| test mAP@0.5IOU           |                                          |
| frequency(Titan)          | 0.0226                                   |
| graphics memory(Titan)    | 11776-610M=11G                           |
| frequency(TX2)            | out of resources                         |
| graphics memory(TX2)      | out of resources                         |
|                           |                                          |
|                           |                                          |
|                           |                                          |
|                           |                                          |





| items                     | values                                   |
| ------------------------- | ---------------------------------------- |
| name                      | fasterres50fisheye1029                   |
| config file               | faster_rcnn_resnet50_fisheye2_1029.config |
| super config name         | faster_rcnn_mobilenet_v1_fisheye2_1025.config |
| time                      | 2018.10.29                               |
| classes                   | ir, ob                                   |
| fixed_shape_resizer       | 512, 512                                 |
| feature_extractor         | type: 'faster_rcnn_resnet50’             |
| hard_example_miner        | None                                     |
| batch_size                | 1                                        |
| initial_learning_rate     | 0.00003                                  |
| fine_tune_checkpoint      | coco                                     |
| data_augmentation_options | random_horizontal_flip                   |
| num_steps(time)           | 60k                                      |
| min loss                  | 0.037                                    |
| train mAP@0.5IOU          | 0.971                                    |
| eval mAP@0.5IOU           | 0.963                                    |
| test mAP@0.5IOU           |                                          |
| frequency(Titan)          | 0.0959                                   |
| graphics memory(Titan)    | 11G                                      |
| frequency(TX2)            | out of resources                         |
| graphics memory(TX2)      | out of resources                         |
|                           |                                          |
|                           |                                          |
|                           |                                          |
|                           |                                          |



| items                     | values                                   |
| ------------------------- | ---------------------------------------- |
| name                      | fasterres50400fisheye1030                |
| config file               | faster_rcnn_resnet50_400_fisheye2_1030.config |
| super config name         | faster_rcnn_resnet50_fisheye2_1029.config |
| time                      | 2018.10.30                               |
| classes                   | ir, ob                                   |
| fixed_shape_resizer       | 400,400                                  |
| feature_extractor         | type: 'faster_rcnn_resnet50‘             |
| hard_example_miner        | None                                     |
| batch_size                | 1                                        |
| initial_learning_rate     | 0.00003                                  |
| fine_tune_checkpoint      | coco                                     |
| data_augmentation_options | random_horizontal_flip                   |
| num_steps(time)           | 20k                                      |
| min loss                  | 0.086                                    |
| train mAP@0.5IOU          | 0.934                                    |
| eval mAP@0.5IOU           | 0.921                                    |
| test mAP@0.5IOU           |                                          |
| frequency(Titan)          | 0.0905                                   |
| graphics memory(Titan)    | 11G                                      |
| frequency(TX2)            | out of resources                         |
| graphics memory(TX2)      | out of resources                         |
|                           |                                          |
|                           |                                          |
|                           |                                          |
|                           |                                          |



| items                     | values                                   |
| ------------------------- | ---------------------------------------- |
| name                      | fastermobile400fisheye1030               |
| config file               | faster_rcnn_mobilenet_v1_400_fisheye2_1030.config |
| super config name         | faster_rcnn_mobilenet_v1_fisheye2_1025.config |
| time                      | 2018.10.30                               |
| classes                   | ir, ob                                   |
| fixed_shape_resizer       | 400, 400                                 |
| feature_extractor         | type: 'faster_rcnn_mobilenet_v1'         |
| hard_example_miner        | None                                     |
| batch_size                | 1                                        |
| initial_learning_rate     | 0.00003                                  |
| fine_tune_checkpoint      | voc                                      |
| data_augmentation_options | random_horizontal_flip                   |
| num_steps(time)           | 220k                                     |
| min loss                  | 0.085                                    |
| train mAP@0.5IOU          | 0.884                                    |
| eval mAP@0.5IOU           | 0.861                                    |
| test mAP@0.5IOU           |                                          |
| frequency(Titan)          | 0.0214                                   |
| graphics memory(Titan)    | 11G                                      |
| frequency(TX2)            | out of resources                         |
| graphics memory(TX2)      | out of resources                         |
|                           |                                          |
|                           |                                          |
|                           |                                          |
|                           |                                          |

## YOLO

| items                     | values                                   |
| ------------------------- | ---------------------------------------- |
| name                      | yolov3fisheye1101                        |
| time                      | 2018.11.1                                |
| classes                   | ir, ob                                   |
| fixed_shape_resizer       | 512, 512                                 |
| feature_extractor         | yolov3                                   |
| batch_size                | 64                                       |
| initial_learning_rate     | 0.01                                     |
| fine_tune_checkpoint      | coco                                     |
| data_augmentation_options | yolo                                     |
| num_steps(time)           | 1500                                     |
| min loss                  |                                          |
| train mAP@0.5IOU          | 0.998 / ir, 0.994 / ob    0.994 / ir, 0.983 / ob 6:4=0.989 |
| eval mAP@0.5IOU           | 0.998 / ir, 0.997 / ob    0.980 / ir, 0.950 / ob 6:4=0.968 |
| test mAP@0.5IOU           |                                          |
| frequency(Titan)          | 0.0379                                   |
| graphics memory(Titan)    | 2499-628M = 1871M                        |
| frequency(TX2)            | 2.1Hz                                    |
| graphics memory(TX2)      |                                          |
|                           |                                          |
|                           |                                          |
|                           |                                          |
|                           |                                          |
|                           |                                          |
|                           |                                          |
|                           |                                          |



| items                     | values                           |
| ------------------------- | -------------------------------- |
| name                      | yolov3400fisheye1101             |
| time                      | 2018.11.1                        |
| classes                   | ir, ob                           |
| fixed_shape_resizer       | 416, 416                         |
| feature_extractor         | yolov3                           |
| batch_size                | 64                               |
| initial_learning_rate     | 0.01                             |
| fine_tune_checkpoint      | coco                             |
| data_augmentation_options | yolo                             |
| num_steps(time)           | 1500                             |
| min loss                  |                                  |
| train mAP@0.5IOU          | 0.981 / ir, 0.964 / ob 6:4=0.974 |
| eval mAP@0.5IOU           | 0.956 / ir, 0.919 / ob 6:4=0.941 |
| test mAP@0.5IOU           |                                  |
| frequency(Titan)          | 0.0375                           |
| graphics memory(Titan)    | 2489M-628M = 1861M               |
| frequency(TX2)            | 2.4Hz                            |
| graphics memory(TX2)      |                                  |
|                           |                                  |
|                           |                                  |
|                           |                                  |
|                           |                                  |
|                           |                                  |
|                           |                                  |
|                           |                                  |



## 

##  