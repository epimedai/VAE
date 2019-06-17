import numpy as np
import matplotlib.pyplot as plt

def plot_prediction(model, data, target_shape=(512, 512)):
    y_pred = model.predict(data)
    nr_of_samples = data.shape[0]
    stacked = y_pred[0].reshape(target_shape)
    for i in range(1, nr_of_samples):
        stacked = np.hstack([stacked, y_pred[i].reshape(target_shape)])
    
    stacked_test = data[0].reshape(target_shape)
    for i in range(1, nr_of_samples):
        stacked_test = np.hstack([stacked_test, data[i].reshape(target_shape)])
    
    plt.figure(figsize=(15,15))
    plt.imshow(np.vstack([stacked_test, stacked]), cmap='gray')
    plt.xticks([])
    plt.yticks([256, 720], ['True', 'Predicted'])
    plt.show()