#!/usr/bin/env python

from glob import glob
from model import denoiser
from utils import *

import os
import argparse
import tensorflow as tf

parser = argparse.ArgumentParser(description='')
parser.add_argument('--epoch', dest='epoch', type=int, default=50, help='# of epoch')
parser.add_argument('--batch_size', dest='batch_size', type=int, default=128, help='# images in batch')
parser.add_argument('--lr', dest='lr', type=float, default=0.001, help='initial learning rate for adam')
parser.add_argument('--phase', dest='phase', default='train', help='train or test')
parser.add_argument('--checkpoint_dir', dest='ckpt_dir', default='./checkpoint', help='models are saved here')
parser.add_argument('--sample_dir', dest='sample_dir', default='./sample', help='sample are saved here')
args = parser.parse_args()


sigma = 25

def denoiser_train(denoiser, lr):
    with load_data(filepath='./dataset/test_HD/*.jpg') as data:
        # if there is a small memory, please comment this line and uncomment the line99 in model.py
        data = data.astype(np.float32) / 255.0  # normalize the data to 0-1
        eval_files = glob('./dataset/test/*.jpg'.format(args.eval_set))
        # list of array of different size, 4-D, pixel value range is 0-255
        eval_data = load_images(eval_files)
        denoiser.train(data, eval_data, batch_size=args.batch_size, ckpt_dir=args.ckpt_dir, epoch=args.epoch, lr=lr,
                       sample_dir=args.sample_dir)


def denoiser_test(denoiser):
    test_files = glob('./data/test/*.jpg'.format(args.test_set))
    denoiser.test(test_files, ckpt_dir=args.ckpt_dir, save_dir=args.test_dir)


def main():
    print("*** Start main program ***")
    # if not os.path.exists(args.ckpt_dir):
    #    os.makedirs(args.ckpt_dir)
    # if not os.path.exists(args.sample_dir):
    #    os.makedirs(args.sample_dir)
    lr = args.lr * np.ones([args.epoch])
    lr[30:] = lr[0] / 10.0
    print("*** CPU band ***")
    with tf.Session() as sess:
        model = denoiser(sess, sigma)
        if args.phase == 'train':
            denoiser_train(model, lr=lr)
        elif args.phase == 'test':
            denoiser_test(model)
        else:
            print('!]Unknown phase')
            exit(0)


if __name__ == '__main__':
    main()
#!/usr/bin/env python

from glob import glob
from model import denoiser
from utils import *

import os
import argparse
import tensorflow as tf

parser = argparse.ArgumentParser(description='')
parser.add_argument('--epoch', dest='epoch', type=int, default=50, help='# of epoch')
parser.add_argument('--batch_size', dest='batch_size', type=int, default=128, help='# images in batch')
parser.add_argument('--lr', dest='lr', type=float, default=0.001, help='initial learning rate for adam')
parser.add_argument('--phase', dest='phase', default='train', help='train or test')
parser.add_argument('--checkpoint_dir', dest='ckpt_dir', default='./checkpoint', help='models are saved here')
parser.add_argument('--sample_dir', dest='sample_dir', default='./sample', help='sample are saved here')
args = parser.parse_args()


def denoiser_train(denoiser, lr):
    with load_data(filepath='./dataset/test_HD/*.jpg') as data:
        # if there is a small memory, please comment this line and uncomment the line99 in model.py
        data = data.astype(np.float32) / 255.0  # normalize the data to 0-1
        eval_files = glob('./dataset/test/*.jpg'.format(args.eval_set))
        # list of array of different size, 4-D, pixel value range is 0-255
        eval_data = load_images(eval_files)
        denoiser.train(data, eval_data, batch_size=args.batch_size, ckpt_dir=args.ckpt_dir, epoch=args.epoch, lr=lr,
                       sample_dir=args.sample_dir)


def denoiser_test(denoiser):
    test_files = glob('./data/test/*.jpg'.format(args.test_set))
    denoiser.test(test_files, ckpt_dir=args.ckpt_dir, save_dir=args.test_dir)


def main():
    print("*** Start main program ***")
    # if not os.path.exists(args.ckpt_dir):
    #    os.makedirs(args.ckpt_dir)
    # if not os.path.exists(args.sample_dir):
    #    os.makedirs(args.sample_dir)
    lr = args.lr * np.ones([args.epoch])
    lr[30:] = lr[0] / 10.0
    print("*** CPU band ***")
    with tf.Session() as sess:
        model = denoiser(sess)
        if args.phase == 'train':
            denoiser_train(model, lr=lr)
        elif args.phase == 'test':
            denoiser_test(model)
        else:
            print('!]Unknown phase')
            exit(0)


if __name__ == '__main__':
    main()
