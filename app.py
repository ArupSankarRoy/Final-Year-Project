import torch
import cv2
import flask
import numpy
import pandas
import matplotlib
import seaborn
import mediapipe

libraries = {

    'torch':torch.__version__,
    'numpy':numpy.__version__,
    'pandas':pandas.__version__,
    'matplotlib':matplotlib.__version__,
    'seaborn':seaborn.__version__,
    'mediapipe':mediapipe.__version__
    
}
with open('requirements.txt' , 'w') as r:
    for lib , version in libraries.items():
        r.write(f'{lib}=={version}\n')