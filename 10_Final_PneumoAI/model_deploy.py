from keras.preprocessing import image
from keras.models import Sequential, model_from_json
import numpy as np

import json

def build_model():
  with open('model_results/model.json', 'r') as json_file:
    architecture = json.load(json_file)
    model = model_from_json(json.dumps(architecture))

  model.load_weights('model_results/model_weight.h5')
  model._make_predict_function()
  return model

def load_image(img_path):
  img = image.load_img(img_path, target_size=(150, 150, 3))
  img = image.img_to_array(img)
  img = np.expand_dims(img, axis=0)
  img /= 255.
  return img

def predict_image(model, img_path, biggest_result=False, show_result=False):
  new_image = load_image(img_path)
  pred = model.predict(new_image)
  predicton = "Normal" if (pred.argmax(axis=-1)==0) else "Pneumonia"
  pred_text = ("Prediction: %s"%(predicton))

  if show_result:
    img = mpimg.imread(img_path)
    imgplot = plt.imshow(img, cmap='bone')
    plt.title(pred)
    plt.show()

  return pred_text
