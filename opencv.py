import os
import sys
import cv2
import numpy as np
import logging
import shutil

def detect(img):
  gray = to_grayscale(img)

  # todo
  
  return []

def to_grayscale(img):
  gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
  gray = cv2.equalizeHist(gray)
  return gray

if __name__ == "__main__":
  # todo, probably
  print 'done'

