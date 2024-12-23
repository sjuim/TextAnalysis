import tarfile, io, os
from zipfile import ZipFile
import numpy as np

# this should do file preprocessing to open the nested tar and zip files (UNFINISHED)

def process_tar(dir_str, filename):
  path = dir_str + filename
  counts = np.array(6)
  # counts for each of the keywords

  print(filename)
  with tarfile.open(path, "r:") as tar:
      for val in tar.getmembers():
         string = val.name
         if "text" in string:
            print(tar.name + "/" + string)
            text_file = ZipFile(tar.name + "/" + string, 'r')
            #print("\t" + string)

      print(text_file.filename)
      # for f in text_file.extractall():
      #    print("\t\t" + f.name)
         # text_counts = search_words(f)
         # counts = counts + text_counts
         

def search_words(f):
  keywords = ['data science', 'machine learning', 'deep learning', 'artificial intelligence', 'applied statistics', 'regression']
  text_counts = np.array(6)

  file = open(f.name, "r")
  data = file.read()

  counter = 0
  for lookup in keywords:
     occurrences = data.count(lookup)
     text_counts[counter] = occurrences
     counter += 1

  return text_counts
     
     

def main():
   dir_str = "/Users/shreya/Documents/Cornell/Year 3 Semester 1/NLP Research/TextAnalysis/text_data_2024/"
   directory = os.fsencode(dir_str)

   for file in os.listdir(directory):
      filename = os.fsdecode(file)
      process_tar(dir_str, filename)
   
if __name__ == '__main__':
   main()