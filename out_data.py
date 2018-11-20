import tensorflow as tf
import numpy as np
from tensorflow.python import pywrap_tensorflow
with tf.Session() as sess:
    # new_saver = tf.train.import_meta_graph('model.ckpt.meta')
    # for var in tf.trainable_variables():
    #     print(var.name)
    checkpoint_path = "./model.ckpt"
    reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
    var_to_shape_map = reader.get_variable_to_shape_map()

    # new_saver.restore(sess, "./model.ckpt")
    # all_vars = tf.trainable_variables()
    for key_i in var_to_shape_map:
        # name = v
        fname = key_i[18:] + '.prototxt'
        fname = fname.replace('/','_')
        print(fname)
        # v_4d = np.array(sess.run(v))
        v_4d=reader.get_tensor(key_i)
        print(v_4d.shape)
        if v_4d.ndim == 5:
                v_4d = np.swapaxes(v_4d, 0, 4)  # swap O,T
                v_4d = np.swapaxes(v_4d, 1, 3)  # swap I, H
                v_4d = np.swapaxes(v_4d, 2, 4)  # swap W, T
                print(v_4d.shape)
                f = open(fname, 'w')
                vshape = v_4d.shape[:]
                v_1d = v_4d.reshape(
                    v_4d.shape[0] * v_4d.shape[1] * v_4d.shape[2] * v_4d.shape[3] * v_4d.shape[4])  # v_1d.shape=(5184,)
                f.write(' blobs {\n')
                for vv in v_1d:
                    f.write('    data: %8f' % vv)
                    f.write('\n')
                f.write('    shape {\n')
                for s in vshape:
                    f.write('      dim: ' + str(s))  # print dims
                    f.write('\n')
                f.write('    }\n')
                f.write('  }\n')
        elif v_4d.ndim == 1 :#do not swap
                f = open(fname, 'w')
                f.write('  blobs {\n')
                for vv in v_4d:
                    f.write('    data: %.8f' % vv)
                    f.write('\n')
                f.write('    shape {\n')
                f.write('      dim: ' + str(v_4d.shape[0]))  # print dims
                f.write('\n')
                f.write('    }\n')
                f.write('  }\n')
        f.close()
