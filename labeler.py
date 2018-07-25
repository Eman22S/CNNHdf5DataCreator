from random import shuffle
import glob
shuffle_data = True  # shuffle the addresses before saving
hdf5_path = 'classifier/train/dataset.hdf5'  # address to where you want to save the hdf5 file
images_path = 'classifier/train/women/*.jpg'
# read addresses and labels from the 'train' folder
addrs = glob.glob('classifier/train/women/*')

labels = [0 if 'woman' in addr else 1 for addr in addrs]  # 0 = Cat, 1 = Dog
# to shuffle data
if shuffle_data:
    c = list(zip(addrs, labels))
    shuffle(c)
    addrs, labels = zip(*c)

# Divide the hata into 60% train, 20% validation, and 20% test
train_addrs = addrs[0:int(0.6*len(addrs))]
train_labels = labels[0:int(0.6*len(labels))]
val_addrs = addrs[int(0.6*len(addrs)):int(0.8*len(addrs))]
val_labels = labels[int(0.6*len(addrs)):int(0.8*len(addrs))]
test_addrs = addrs[int(0.8*len(addrs)):]
test_labels = labels[int(0.8*len(labels)):]
