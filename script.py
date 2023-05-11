import os
import pdfquery
import pandas as pd

for subdir, dirs, files in os.walk('pdfs'):
    for file in files:
        print(os.path.join(subdir, file))
