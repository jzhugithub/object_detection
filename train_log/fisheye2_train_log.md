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
| frequency                 | tx2:0.0626                               |



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





##  