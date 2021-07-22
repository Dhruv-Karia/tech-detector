import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from ai import get_yolo_net, yolo_forward, yolo_save_img
from utils import get_base_url, allowed_file, and_syntax