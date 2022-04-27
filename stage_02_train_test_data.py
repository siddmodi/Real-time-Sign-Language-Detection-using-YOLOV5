import os
import shutil

IMAGE_PATH='CollectedImages'
data_dir = 'Data'
train = 'train'
test = 'test'
images = 'images'
labels = 'labels' 
train_dir = os.path.join(data_dir,'train\\images')                      # 'Data\\train\\images\\'
test_dir = os.path.join(data_dir,'test\\images')                        # 'Data\\test\\images\\'
no_of_training_files = 8                                                # <<---- Rest consider as testing
classes=['Hello','Yes','No','Thanks','IloveYou','Please']

os.makedirs(data_dir)

os.makedirs(os.path.join(data_dir,train))
os.makedirs(os.path.join(data_dir,train,images))
os.makedirs(os.path.join(data_dir,train,labels))

os.makedirs(os.path.join(data_dir,test))
os.makedirs(os.path.join(data_dir,test,images))
os.makedirs(os.path.join(data_dir,test,labels))


for i in classes:
    path = os.path.join(IMAGE_PATH,i)
    files = os.listdir(path)[0:no_of_training_files]

    if len(files)<=0:
        print('No Files Present')
    else:
        for eachfilename in files:
            src = IMAGE_PATH+'\\'+i+'\\'+eachfilename
            dst = train_dir + eachfilename
            shutil.copy(src,dst)
            print("File moved:",eachfilename)
            os.remove(src)

for i in classes:
    path = os.path.join(IMAGE_PATH,i)
    files = os.listdir(path)

    if len(files)<=0:
        print('No Files Present')
    else:
        for eachfilename in files:
            src = IMAGE_PATH+'\\'+i+'\\'+eachfilename
            dst = test_dir + eachfilename
            shutil.copy(src,dst)
            print("File moved:",eachfilename)
            os.remove(src)
shutil.rmtree(IMAGE_PATH)


# To run :--->  python stage_02_train_test_data.py