import tarfile, io, os
from zipfile import ZipFile
import numpy as np

def process_text(text):
   print(text)

def iterate_texts(dir_str):
   for sub_dir in os.listdir(dir_str):
      if os.path.isdir(dir_str + "/" + sub_dir):
         for file in os.listdir(dir_str + "/" + sub_dir):
            if os.path.isdir(dir_str + "/" + sub_dir + "/" + file):
                for text in os.listdir(dir_str + "/" + sub_dir + "/" + file):
                   process_text(text)

def main():
   dir_str = "/Users/shreya/Documents/Cornell/Year 3 Semester 1/NLP Research/TextAnalysis/text_data_2024"

   iterate_texts(dir_str)
   
   
if __name__ == '__main__':
   main()