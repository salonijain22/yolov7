from re import DEBUG, sub
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename, send_from_directory
import os
import subprocess
import glob
import os
import sys
sys.path.append('yolov7')

from detect import status,image_stat
import argparse
import time
from pathlib import Path
import cv2
import torch
import numpy as np
import torch.backends.cudnn as cudnn
from numpy import random
from PIL import Image
from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel

app = Flask(__name__)


uploads_dir = os.path.join(app.instance_path, 'uploads')

os.makedirs(uploads_dir, exist_ok=True)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/detect", methods=['POST'])
def detect():
    if not request.method == "POST":
        return
    video = request.files['video']
    video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
    print(video)
    print("filename",secure_filename(video.filename))
    subprocess.run("ls", shell=True)
    # subprocess.run(['python3', 'detect.py','--weights','runs\train\exp\weights\epoch_001.pt','--conf','0.1' ,'--source', os.path.join(uploads_dir, secure_filename(video.filename))],shell=True)
    subprocess.run(['python','detect.py','--weights','runs/train/exp/weights/epoch_001.pt','--conf','0.1','--source',os.path.join(uploads_dir, secure_filename(video.filename))],shell=True)
    return secure_filename(video.filename)
    # obj = secure_filename(video.filename)
    # print("image_status")
    # return image_status
    
@app.route("/")
def image_status():
    return status

    


# @app.route("/",methods=["GET"])
# def download_file():
#     if not request.method=="GET":
#         return
#     list_of_folders = glob.glob('runs/detect/*')
#     latest_folder = max(list_of_folders, key=os.path.getmtime)
#     latest_file = send_file(latest_folder, as_attachment=True)
    
#     return  "CBBA000303082_2.jpg"
    # print("hello")












# @app.route('/return-files', methods=['GET'])
# def return_file():
#     # logger.info('Checking file to download..')
#     list_of_folders = glob.glob('runs/detect/*')
#     latest_folder = max(list_of_folders,key=os.path.getmtime)
#     latest_file = max(latest_folder,key=os.path.getmtime)
#     # logger.info(latest_file)
#     print(latest_file)
#     try:
#         return send_file('runs\detect\exp3\CBBA000272003_3.jpg',as_attachment=True)
#         # return send_from_directory(loc, obj)
#     except Exception as e:
#         return str(e)

# @app.route('/return-files', methods=['GET'])
# def return_file():
#     list_of_folders = glob.glob('runs/detect/*')
#     list_of_files = glob.glob(list_of_folders,key=os.path.getctime)
#     # list_of_files = glob.glob('runs/detect/*') # * means all if need specific format then *.csv
    
#     latest_file = max(list_of_files, key=os.path.getctime)
#     print(latest_file)
    
#     # obj = request.args.get('obj')
#     # loc = os.path.join("static", obj)
#     # print(loc)
#     # subprocess.run(['python3', 'bounding_boxes.py'],shell=True)
#     try:
        
#         return send_from_directory(list_of_files,latest_file)
#         send_file(latest_file)
#         # return send_from_directory(loc, obj)
#     except Exception as e:
#         return str(e)

@app.route('/display/<filename>')
def display_image(filename):
	print('display_video filename: ' + filename)
	return redirect(url_for('static/filename', code=200))
@app.route("/opencam", methods=['GET'])
def opencam():
    print("here")
    subprocess.run(['python3', 'detect.py', '--source', '0'])
    return "done"
    

