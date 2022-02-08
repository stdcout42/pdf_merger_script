# pdf_merger_script
A python script using Py2PDF2 to merge pdfs in a given folder.

Only tested on **Linux**.

## How to use
1. Clone repo or just download the script `merge_pdfs.py`
2. Install [Py2PDF2](https://pypi.org/project/PyPDF1/) using `pip install pypdf2`
3. Have all your pdf files placed in a folder, for example the folder could be called `1_1/` . If you need your files to be order, make sure to name them for lexicographical order. (ie, `1_1_1.pdf` , `1_1_2.pdf` etc)
4. Run `python merge_pdfs.py 1_1/` 
