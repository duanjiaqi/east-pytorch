import torch
import os
import config as cfg
import shutil
import datetime
from utils.util import *
# this is for weight
def save_checkpoint(state, epoch, filename='checkpoint.pth.tar'):
    """[summary]

    [description]

    Arguments:
        state {[type]} -- [description] a dict describe some params
        is_best {bool} -- [description] a bool value

    Keyword Arguments:
        filename {str} -- [description] (default: {'checkpoint.pth.tar'})
    """
    weight_dir = cfg.parameter_path
    print('weight_dir is {}'.format(weight_dir))

    if not os.path.exists(weight_dir):
        os.mkdir(weight_dir)

    filename = 'epoch_'+str(epoch)+'_checkpoint.pth.tar'
    file_path = os.path.join(weight_dir, filename)
    torch.save(state, file_path)
    print('weight file {} is saved at {}'.format(filename, file_path))

def save_loss_info(losses, epoch, current_batch, loader, path='./log.txt'):
    path = os.path.abspath(path)
    if not os.path.isfile(path):
        os.mknod(path)

    with open(path, 'a') as f:
        line = 'Epoch: [{0}][{1}/{2}]\t Loss {loss.val:.4f} ({loss.avg:.4f})\n'.format(epoch,current_batch, len(loader), loss = losses)
        f.write(line)





