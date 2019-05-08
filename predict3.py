from tkinter import filedialog
from tkinter import *
import os
import logging
import tkinter.scrolledtext as tkst
import sys
from keras.models import load_model
import scipy.io as io
from sklearn.metrics import *
import numpy as np
import json

root = Tk()
model_file = StringVar()
data_file=StringVar()
evaluate_py=StringVar()
editArea = tkst.ScrolledText(
    wrap   = WORD,
    width  = 100,
    height = 10
)

def evaluate1(model_path, images, labels ):
#  model1 = load_model("sgd_tv_e10_vga_cnn_94_55.h5")
  print("#######################",model_path)
  model1 = load_model(model_path)
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
#  acc =f1 = pre = rec = 0
  results["Acc."]=acc
  results["F1 score"]=f1
  results["Precision"]=pre
  results["Recall"]=rec
  dir1 = os.path.dirname(model_path) ## directory of file
  print(dir1)
  results_file = dir1+"/test_classification.json"
  with open(dir1+"/test_classification.json", 'w') as outfile:  
    json.dump(results, outfile)
#  return acc,f1,pre,rec

def _main(data_path, model_path):
  print(data_path)
  dict1        = io.loadmat(data_path, variable_names=["test_img", "test_labels"])
  test_img     = dict1["test_img"]
  test_labels  = dict1["test_labels"]
  r = test_img/255
  test_labels = test_labels.astype(np.int)
  evaluate1(model_path, r, test_labels)


class WidgetLogger(logging.Handler):
    def __init__(self, widget):
        logging.Handler.__init__(self)
        self.widget = widget

    def emit(self, record):
        # Append message (record) to the widget
        self.widget.insert(INSERT, record + '\n')


def getDir():
	path = filedialog.askdirectory(title = "Select Folder")
	#print("######",path)
	return path

def getFile():
	path = filedialog.askopenfilename(title = "Select file")
	#print("######",path)
	return path

def setModel():
	model_file.set(getFile())
	print("#####",model_file.get())

def setTestDir():
	data_file.set(getFile())
	print("#####",data_file.get())

def evaluate():
	dir1 = os.path.dirname(model_file.get()) ## directory of file
	results = dir1+"/test_classification.json"
	print("$$$$$$###$$$$$$$$$", results)
	editArea.delete('1.0',END)
	if((not model_file.get()) or (not data_file.get())):
		editArea.insert(INSERT,"All arguments are necessary to run the evaluation script. Current status of parameters:")
		editArea.insert(INSERT,"\n1.model_file:"+model_file.get()+"\n3.data_file:"+data_file.get())
		return
	else:
		print("hi"," model_file:",model_file.get(), " data_file:", data_file.get())#, " evaluate_py:", evaluate_py.get())
	editArea.delete('1.0',END)
	editArea.insert(INSERT,"Running....evaluation")
	model_path = model_file.get()
	data_path = data_file.get()
	_main(data_path, model_path)
	with open(results, 'r') as f:
		editArea.delete('1.0',END)
		editArea.insert(INSERT,f.read())
	f.close()
	

Button(text='Select model file', command=setModel).pack(fill=X)
Button(text='Select dataset file', command=setTestDir).pack(fill=X)
Button(text='Evaluate model', command=evaluate).pack(fill=X)
editArea.pack(padx=10, pady=10, fill=BOTH, expand=True)
editArea.insert(INSERT,
"""\
Try Evaluate Function to get results here!
""")

mainloop()