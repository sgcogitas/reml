import datetime
import json
from typing import TextIO
import eml_parser
import  tkinter as tk
from array import array
from tkinter import filedialog


def json_serial(obj):
  if isinstance(obj, datetime.datetime):
      serial = obj.isoformat()
      return serial

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(multiple=True)

print(file_path)

for t in file_path:
	with open(t, 'rb') as fhdl:
		raw_email = fhdl.read()
	
	ep = eml_parser.EmlParser()
	parsed_eml = ep.decode_email_bytes(raw_email)

	textfile = open(t + ".json", "w")
	textfile.write(json.dumps(parsed_eml, default=json_serial))
