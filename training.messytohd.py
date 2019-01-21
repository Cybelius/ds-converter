import tensorflow as tf

batch_size = 32
epoch_num = 50

saving_path = 'autoencoder_messy_to_hd/SavedModel/AutoencoderMessyToHd.ckpt'

saver_ = tf.train.Saver(max_to_keep=3)

batch_img = dataset_source[0:batch_size]
batch_out = dataset_target[0:batch_size]

num_batches = num_images // batch_size

sess = tf.Session()
sess.run(init)

for ep in range(epoch_num):
    batch_size = 0
    for batch_n in range(num_batches):  # batches loop

        _, c = sess.run([train_op, loss], feed_dict={ae_inputs: batch_img, ae_target: batch_out})
        print("Epoch: {} - cost = {:.5f}".format((ep + 1), c))

        batch_img = dataset_source[batch_size: batch_size + 32]
        batch_out = dataset_target[batch_size: batch_size + 32]

        batch_size += 32

    saver_.save(sess, saving_path, global_step=ep)

sess.close()
