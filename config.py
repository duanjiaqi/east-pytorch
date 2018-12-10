#data
dataroot='../data_new'  #./data/train/img      ./data/train/gt
# dataroot='../data_1517'  #./data/train/img      ./data/train/gt
test_img_path='../data/test/img'

name = 'original_newmodel'
# name = 'ttt'
parameter_path = './parameter/' + name  # !!!!!!!!!!改改改!!!!!!!!!!!!
result = './result/' + name
log_path = './log/' + name

lr = 0.0001
gpu_ids = [0, 1]
gpu = 2
init_type = 'xavier'

resume = False
checkpoint = ''# should be file
train_batch_size  = 28
num_workers = 14

print_freq = 10
eval_iteration = 10
save_iteration = 10
max_epochs = 10000







