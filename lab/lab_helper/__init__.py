def import_exp_pyd():
  global exp_py
  import os
  import sys
  import glob
  import shutil
  import datetime

  relevant_files = [ "exp_py*.pyd", "exp_py.pdb" ]
  
  rel_dir      = os.path.realpath(os.path.dirname(__file__) + "/../..")
  cache_dir    = rel_dir + '/lab/pyd_cache/'

  selected_files = [ glob.glob(rel_dir + '/*/bin/RelWithDebInfo/' + f)[0] for f in relevant_files ]
  asset_folder   = None # os.path.realpath(os.path.dirname(glob.glob(rel_dir + '/*/assets/')[0]))
  
  if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
  if cache_dir not in sys.path:
    sys.path.insert(0, cache_dir)

  for f in relevant_files:
    old_cache = glob.glob(cache_dir + f)
      
    for old in old_cache:
      if '.old~' in old:
        continue
      try:
        os.remove(old)
      except OSError:
        shutil.move(old, old + ".old~" + str(datetime.datetime.now().timestamp()))
        pass
          
  for f in selected_files:
    shutil.copyfile(f, cache_dir + os.path.basename(f))
         
  import exp_py
