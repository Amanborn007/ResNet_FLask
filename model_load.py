from keras.applications.resnet50 import ResNet50

model = ResNet50(weights='imagenet')
model.save(r'F:\My_Hand_Face_Model')
print('Model loaded. Check http://127.0.0.1:5000/')
