import tensorflow as tf
kaldi_module = tf.load_op_library("../build/libkaldi_readers.so")

def main():
    value_rspecific = "./data/matrix.nocompress.ark:59"
    rspec = tf.constant(value_rspecific, tf.string)
    feats_raw_value = kaldi_module.read_kaldi_matrix(rspec)
    feats_value = kaldi_module.decode_kaldi_matrix(feats_raw_value, tf.float32)
    feats_value.set_shape([None, 4])
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    feats = sess.run(feats_value)
    print(feats.shape)
    print(feats)


if __name__ == "__main__":
    main()