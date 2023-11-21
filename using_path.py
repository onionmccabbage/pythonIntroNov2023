# we can always see where python will look for any import
import sys
# it is a reelly good idea to share a location for useful in-house libraries
# then add that path to sys,path

# we can add places that Python should look for imports
sys.path.append('D:\\pythonIntroNov2023\\useful\\subpack') # or use /
import more #  this will resolve

print( sys.path )

print(more.here()) # this is found on our path