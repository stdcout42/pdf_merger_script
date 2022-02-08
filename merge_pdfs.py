import sys
from os import listdir
from os.path import isfile, join
from PyPDF2 import PdfFileMerger, PdfFileReader

def merge_files(pdfs_path):
  from os import listdir
  from os.path import isfile, join
  filenames = [f for f in listdir(pdfs_path) if isfile(join(pdfs_path, f))]
  pdf_files = [f for f in filenames if 'pdf' in f]
  pdf_files.sort()
  
  print(f'Merging in the following order: {pdf_files}')
  pdf_file_merger = PdfFileMerger() 

  output_name = f'{pdfs_path.replace("/", "") + "_merged.pdf"}'
  for f in pdf_files:
    pdf_file_merger.append(PdfFileReader(join(pdfs_path,f), 'rb'))
  pdf_file_merger.write(output_name)
  print(f'Output: {output_name}')



if __name__ == '__main__':
  if len(sys.argv) != 2:
    print(f'Usage:\n\t{sys.argv[0]} path_of_pdfs')
    sys.exit()
  merge_files(sys.argv[1])
