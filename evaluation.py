from keras.models import load_model
import scipy.io as io
from sklearn.metrics import *
import numpy as np
import sys
import gflags
import json
import os

FLAGS = gflags.FLAGS
gflags.DEFINE_string('model', "./sgd_tv_e10_vga_cnn_94_55.h5", 'Model')
gflags.DEFINE_string('data', "./dict5000.mat", 'Input data mat file')

def evaluate(model_path, images, labels ):
  model1 = load_model("sgd_tv_e10_vga_cnn_94_55.h5")
  print("#######################",model_path)
  model1 = load_model("model.h5")
  predictions = model1.predict(images)
  y_true = labels
  y_pred = np.round(predictions).astype(np.int)
  acc = accuracy_score(y_true, y_pred)
  f1 = f1_score(y_true, y_pred, average='binary')
  pre = precision_score(y_true, y_pred, average='binary')
  rec = recall_score(y_true, y_pred, average='binary')
  del model1, predictions, y_true, y_pred
  print("Acc.", acc)
  print("F1 score", f1)
  print("Precision", pre)
  print("Recall", rec)
  results = {}
  acc =f1 = pre = rec = 0
  results["Acc."]=acc
  results["F1 score"]=f1
  results["Precision"]=pre
  results["Recall"]=rec
  dir1 = os.path.dirname(model_path) ## directory of file
  print(dir1)
  with open(dir1+"/test_classification.json", 'w') as outfile:  
    json.dump(results, outfile)
#  return acc,f1,pre,rec

def _main():
  data_path = FLAGS.data
  print(FLAGS.data)
  dict1        = io.loadmat(data_path, variable_names=["test_img", "test_labels"])
  test_img     = dict1["test_img"]
  test_labels  = dict1["test_labels"]
  r = test_img/255
  test_labels = test_labels.astype(np.int)
  model_path = FLAGS.model
  evaluate(model_path, r, test_labels)

def main(argv):
    # Utility main to load flags
    try:
      argv = FLAGS(argv)  # parse flags
    except gflags.FlagsError:
      print ('Usage: %s ARGS\\n%s' % (sys.argv[0], FLAGS))
      sys.exit(1)
    _main()


if __name__ == "__main__":
    main(sys.argv)