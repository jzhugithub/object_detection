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
| frequency                   |                                          |

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
| frequency                |                                          |





## SSD area conv



## SSD retina



## SSD gradient conv

