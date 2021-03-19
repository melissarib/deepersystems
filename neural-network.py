# import elementary libraries
import os
import glob
import numpy as np
import pandas as pd

# loading data
df = pd.read_csv("train.truth.csv")

# check dataset information
df.head(50)
df.info()
len(os.listdir("train"))

# format file names
a = df["fn"].values[0].split(".")
a[0].split("_")[0]
os.listdir("train")[0]
folder = os.listdir("train")

# rename files
for i in range(len(os.listdir("train"))):
        data = str(fn[i]).split(".")
        number = data[0].split("_")[0]
        new_name = number + "_" + label[i] + ".jpg"
        os.rename("train/"+fn[i], "train/"+new_name)
        print("The file "+fn[i]+" was renamed to " + new_name)

# preprocessing data with scikit-learn and pillow libraries
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

def onehot_labels(values):
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values)
    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    return onehot_encoded

# adjust image dimensions
X = []
Y = []
width = 64
height = 64

for img in imgs:
    filename = os.path.basename(img)
    labels = filename.split("_")[-1].split(".")[0]
    im = np.array(Image.open(img).convert("L").resize((width, height)))
    im = im / 255
    X.append(im)
    Y.append(labels)

X = np.array(X)
train_X = X.reshape(X.shape[0], width, height, 1)
train_Y = onehot_labels(Y)

# building neural network model with Keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(width, height, 1)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.30))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.30))
model.add(Dense(4, activation='softmax'))

# check the summary model
# Total params: 7,392,260 && Trainable params: 7,392,260
model.summary()


# callback for more efficiency
from keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
es = EarlyStopping(monitor = 'loss', min_delta = 1e-10, patience = 10, verbose = 1)
mcp = ModelCheckpoint(filepath = 'over.h5', monitor = 'accuracy', save_best_only = True, verbose = 1)

# use the gradient descent (SGD) optimizer
model.compile(loss='categorical_crossentropy', optimizer='SGD', metrics=['accuracy'])

# train the model
model.fit(train_X, train_Y, epochs=100, batch_size=64, callbacks=[es,mcp])