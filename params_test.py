#from dict_math import label_dict
random_sample = True
best_accuracy = 0
keep_ratio = True
adam = True
adadelta = False
saveInterval = 1
valInterval = 20000
n_test_disp = 40
displayInterval = 100
experiment = './expr/vgg16py/'
dict_path = "./index_dict.txt"
#alphabet = dict_path
test_img = "/data/xiaoya/crnn_chinese/data/select_paisou/img/"
crnn = 'model/crnn_Rec_done_10_899.pt'
beta1 =0.5
lr = 0.00019
niter = 300
nh =309 
imgW = 32 
imgH = 1024
val_batchSize = 1
batchSize = 128
workers = 6
std = 0.193
mean = 0.588
topnum = 10
