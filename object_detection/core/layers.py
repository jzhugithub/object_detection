import tensorflow as tf
slim = tf.contrib.slim

def area_conv2d11(inputs, inputs_hwc, num_outputs, scope=None):
    '''
    Implement area conv2d with ksizes=[1, 1, 1, 1], strides=[1, 1, 1, 1]
    One can cooperate with `tf.extract_image_patches` to change ksizes and strides

    :param inputs: A 4-D Tensor with shape [batch, height, width, in_channels]
    :param inputs_hwc: A list of length 3: [height, width, in_channels]
    :param num_outputs: Integer, the number of output filters.
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