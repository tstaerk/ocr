import pypdf
import sys
import tabula

try:
  inputfile=open(sys.argv[1],"rb")
except:
  print("This program converts a PDF file to CSV. To start, provide a PDF file as parameter.")

from tabula import convert_into
convert_into(sys.argv[1], sys.argv[1]+".csv", output_format="csv")
