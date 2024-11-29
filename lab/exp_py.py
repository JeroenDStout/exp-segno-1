import lab_helper
lab_helper.import_exp_pyd()
from lab_helper import exp_py as exp

# +
import json

my_first_row = exp.segno.fields_row()
print(my_first_row)
