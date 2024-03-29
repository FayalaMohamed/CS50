#CS50AI - Week 5 - Traffic
##Task:
Write an AI to identify which traffic sign appears in a photograph, using a tensorflow convolutional neural network.

##Background:
As research continues in the development of self-driving cars, one of the key challenges is computer vision, allowing these cars to develop an understanding of their environment from digital images. In particular, this involves the ability to recognize and distinguish road signs – stop signs, speed limit signs, yield signs, and more.

In this project, you’ll use TensorFlow to build a neural network to classify road signs based on an image of those signs. To do so, you’ll need a labeled dataset: a collection of images that have already been categorized by the road sign represented in them.

Several such data sets exist, but for this project, we’ll use the German Traffic Sign Recognition Benchmark (GTSRB) dataset, which contains thousands of images of 43 different kinds of road signs.

##Specification:
Complete the implementation of load_data and get_model in traffic.py.

The load_data function should accept as an argument data_dir, representing the path to a directory where the data is stored, and return image arrays and labels for each image in the data set.
You may assume that data_dir will contain one directory named after each category, numbered 0 through NUM_CATEGORIES - 1. Inside each category directory will be some number of image files.
Use the OpenCV-Python module (cv2) to read each image as a numpy.ndarray (a numpy multidimensional array). To pass these images into a neural network, the images will need to be the same size, so be sure to resize each image to have width IMG_WIDTH and height IMG_HEIGHT.
The function should return a tuple (images, labels). images should be a list of all of the images in the data set, where each image is represented as a numpy.ndarray of the appropriate size. labels should be a list of integers, representing the category number for each of the corresponding images in the images list.
Your function should be platform-independent: that is to say, it should work regardless of operating system. Note that on macOS, the / character is used to separate path components, while the \ character is used on Windows. Use os.sep and os.path.join as needed instead of using your platform’s specific separator character.
The get_model function should return a compiled neural network model.
You may assume that the input to the neural network will be of the shape (IMG_WIDTH, IMG_HEIGHT, 3) (that is, an array representing an image of width IMG_WIDTH, height IMG_HEIGHT, and 3 values for each pixel for red, green, and blue).
The output layer of the neural network should have NUM_CATEGORIES units, one for each of the traffic sign categories.
The number of layers and the types of layers you include in between are up to you. You may wish to experiment with:
different numbers of convolutional and pooling layers
different numbers and sizes of filters for convolutional layers
different pool sizes for pooling layers
different numbers and sizes of hidden layers
dropout
In a separate file called README.md, document (in at least a paragraph or two) your experimentation process. What did you try? What worked well? What didn’t work well? What did you notice?
Ultimately, much of this project is about exploring documentation and investigating different options in cv2 and tensorflow and seeing what results you get when you try them!

##Model Experimentation Process:
I began by testing the same model the handwriting recognition:
``` python
# Convolutional layer. Learn 32 filters using a 3x3 kernel
tf.keras.layers.Conv2D(
    32, (3, 3), activation="relu", input_shape=(28, 28, 1)
),

# Max-pooling layer, using 2x2 pool size
tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

# Flatten units
tf.keras.layers.Flatten(),

# Add a hidden layer with dropout
tf.keras.layers.Dense(128, activation="relu"),
tf.keras.layers.Dropout(0.5),

# Add an output layer with output units for all 10 digits
tf.keras.layers.Dense(10, activation="softmax")
```

But this model gave a very poor result of around 5% in trainig and tests. So the next step I tried was adding some dense layers.
I added two dense layers before the max-pooling layer and 3 after the flatten layer
``` python
#before the max-poolin layer
tf.keras.layers.Dense(32, activation="relu"),
tf.keras.layers.Dropout(0.3),
tf.keras.layers.BatchNormalization(),
tf.keras.layers.Dense(32, activation="relu"),
tf.keras.layers.Dropout(0.3),
tf.keras.layers.BatchNormalization(),
```
``` python
#after the flatten layer
tf.keras.layers.Dense(2048, activation="relu"),
tf.keras.layers.Dropout(0.3),
tf.keras.layers.BatchNormalization(),
tf.keras.layers.Dense(1024, activation="relu"),
tf.keras.layers.Dropout(0.3),
tf.keras.layers.BatchNormalization(),
tf.keras.layers.Dense(512, activation="relu"),
tf.keras.layers.Dropout(0.3),
tf.keras.layers.BatchNormalization(),
```

I also added another Conv2D layer after the first one and tried to maximize the accuracy of both training and tests by changing the number of units in each layer and adding a BatchNormalization layer after each dense and conv2d layer. The best result I found with a model this complex had around 93% of accuracy after the 10 epochs of training but was actually overfitting the training data as it had a lower accuracy for test data at 80%. Thi model had also a lot of parameters. At some point it had around 8 million of parameters and each epoch took about 2 minutes to finish so I had to begin rebuilding a model a little bit simpler an dnot overfitting the training data.

So I kept the 2 conv2d layers, the max-pooling layer, the flatten layers and only one hidden dense layer.

``` python
tf.keras.layers.Conv2D(64, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
tf.keras.layers.BatchNormalization(),

# Flatten layers
tf.keras.layers.Flatten(),

# Add A Dense Hidden layer with 512 units and 50% dropout
tf.keras.layers.Dense(512, activation="relu"),
tf.keras.layers.Dropout(0.5),

# Add Dense Output layer with 43 output units
tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
```

This model did very well both in training and tests with 98%.