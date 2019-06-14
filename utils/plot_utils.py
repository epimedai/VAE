import numpy as np
import matplotlib.pyplot as plt

def plot_prediction(model, data, target_shape=(512, 512)):
    y_pred = model.predict(data)

    stacked = y_pred[0].reshape(target_shape)
    for i in range(1, nr_of_samples):
        stacked = np.vstack([stacked, y_pred[i].reshape(target_shape)])
    
    stacked_test = test_data[0].reshape(target_shape)
    for i in range(1, nr_of_samples):
        stacked_test = np.vstack([stacked_test, test_data[i].reshape(target_shape)])
    
    plt.figure(figsize=(20,20))
    plt.imshow(np.hstack([stacked_test, stacked]), cmap='gray')
    plt.yticks([])
    plt.xticks([256, 720], ['True', 'Predicted'], rotation=90)
    plt.show()