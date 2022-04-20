Saving model and loading a model:
model.save("<name>.h5")
// check if this file is stored locally or not
model = tf.keras.models.load_model("file path")
print(model.layers) // to confirm if the model still have same number of layers
model.evaulate(X_test,Y_test) // to confirm if the model still gives same accuray

 