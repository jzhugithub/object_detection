import tensorflow as tf

slim = tf.contrib.slim
import numpy as np


def area_conv2d11(inputs, inputs_hwc, num_outputs, scope=None):
    '''
    Implement area conv2d with ksizes=[1, 1, 1, 1], strides=[1, 1, 1, 1]
    One can cooperate with `tf.extract_image_patches` to change ksizes and strides

    :param inputs: A 4-D Tensor with shape [batch, height, width, in_channels]
    :param inputs_hwc: A list of length 3: [height, width, in_channels]
    :param num_outputs: Integer, the number of output filters.
    :param scope: String, scope name.
    :return: A 4-D Tensor with shape [batch, height, width, num_outputs]
    '''

    with tf.variable_scope(scope):
        inputs_height = inputs_hwc[0]
        inputs_width = inputs_hwc[1]
        inputs_channel = inputs_hwc[2]
        inputs_reshape1 = tf.reshape(tensor=inputs,
                                     shape=[-1, inputs_height * inputs_width, 1, inputs_channel],
                                     name='reshape1')
        inputs_transpose = tf.transpose(a=inputs_reshape1,
                                        perm=[0, 3, 2, 1],
                                        name='transpose')
        inputs_separable = tf.contrib.layers.separable_conv2d(inputs=inputs_transpose,
                                                              num_outputs=None,
                                                              kernel_size=[inputs_channel, 1],
                                                              depth_multiplier=num_outputs,
                                                              padding='VALID',
                                                              activation_fn=None,
                                                              normalizer_fn=None,
                                                              scope='separable')
        outputs = tf.reshape(tensor=inputs_separable,
                             shape=[-1, inputs_height, inputs_width, num_outputs],
                             name='reshape2')
        return outputs


def create_mask4(inputs_hwc):
    '''
    create ratio mask for four kernels.
    
    :param inputs_hwc: A list of length 3: [height, width, in_channels]
    :return: A dict of four ratio mask.
    '''

    if inputs_hwc[0] != inputs_hwc[1]:
        raise ValueError('create_mask4() only support same height and width now')

    # mask00_init = np.zeros(inputs_hwc, np.float32)
    mask00_init = 1e-6 * np.ones(inputs_hwc, np.float32)
    for row in range(inputs_hwc[0] - 1):
        for col in range(inputs_hwc[1] - row - 1):
            mask00_init[row, col, :] = 1.0 * (inputs_hwc[0] - row - col - 1) / (inputs_hwc[0] - 1)
    mask01_init = mask00_init[::-1, :, :]
    mask10_init = mask00_init[:, ::-1, :]
    mask11_init = mask00_init[::-1, ::-1, :]

    mask00_init_sum = mask00_init + mask01_init + mask10_init + mask11_init

    mask00 = mask00_init / mask00_init_sum
    mask01 = mask01_init / mask00_init_sum
    mask10 = mask10_init / mask00_init_sum
    mask11 = mask11_init / mask00_init_sum

    return {'mask00': mask00,
            'mask01': mask01,
            'mask10': mask10,
            'mask11': mask11}


def gradient_conv2d411(inputs, inputs_hwc, num_outputs, scope=None):
    '''
    Implement gradient conv2d with ksizes=[1, 1, 1, 1], strides=[1, 1, 1, 1]
    
    :param inputs: A 4-D Tensor with shape [batch, height, width, in_channels]
    :param inputs_hwc: A list of length 3: [height, width, in_channels]
    :param num_outputs: Integer, the number of output filters.
    :param scope: String, scope name.
    :return: A 4-D Tensor with shape [batch, height, width, num_outputs]
    '''

    with tf.variable_scope(scope):
        with slim.arg_scope([slim.conv2d],
                            kernel_size=[1, 1],
                            padding="SAME",
                            activation_fn=None,
                            normalizer_fn=None,
                            normalizer_params=None):
            if inputs_hwc[0] == 1 or inputs_hwc[1] == 1:
                return slim.conv2d(
                    inputs=inputs,
                    num_outputs=num_outputs,
                    scope='conv2d')
            else:
                # create ratio masks
                masks = {}
                for key, masknp in create_mask4([inputs_hwc[0], inputs_hwc[1], num_outputs]).items():
                    masks[key] = (tf.constant(masknp, dtype=tf.float32, name=key))

                # create net
                net = []
                for key, mask in masks.items():
                    net.append(tf.expand_dims(mask, 0) * slim.conv2d(inputs=inputs,
                                                                     num_outputs=num_outputs,
                                                                     scope='conv2d_%s' % key))
                return sum(net)
