import os, sys, subprocess

# Set low priority on Windows
if 'win' in sys.platform:
	#sys.path.append( os.path.join( volume, path, 'site-packages' ) ) # path to site-packages where psutil resides, if not already installed
	import psutil
	proc = psutil.Process(os.getpid())
	#proc.set_nice(psutil.HIGH_PRIORITY_CLASS)
	#proc.set_nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
	proc.set_nice(psutil.IDLE_PRIORITY_CLASS)

p = subprocess.Popen( command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

sys.stdout.flush()
for line in iter(p.stdout.readline, b''):
	sys.stdout.flush()
	print(">>> " + line.rstrip())
