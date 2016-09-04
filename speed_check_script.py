import re
import subprocess

def getCurrentSpeeds:
	p = subprocess.Popen(['speedtest-cli'], stdout=subprocess.PIPE,
		                                stderr=subprocess.PIPE);

	out, err = p.communicate()

	#print "result: "
	#print out

	#print "error: "
	#print err

	downloadMatch = re.search('Download: (\d+\.\d+) Mbit\/s',out)
	downloadSpeed = float(downloadMatch.group(1))

	#print "download match: ", downloadMatch

	uploadMatch = re.search('Upload: (\d+\.\d+) Mbit\/s',out)
	uploadSpeed = float(uploadMatch.group(1))

	#print "upload match: ", uploadMatch

	#print downloadSpeed, " down, ", uploadSpeed, " up"

