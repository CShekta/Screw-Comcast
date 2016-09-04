import datetime
import re
import subprocess
import time
import tzlocal

def getCurrentSpeeds():
    try:
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
        return (downloadSpeed, uploadSpeed)
    except:
	return ( 0/0, 0/0 )


#print time.tzname
#print time.timezone
#print time.localtime()
#print time.time()
#print time.strftime("%a, %d %b %Y %H:%M:%S %z", time.localtime())
#print time.strftime('%Y-%m-%dT%H:%M:%S%z')
#print datetime.isoformat()

t = time.time()
dt = datetime.datetime.fromtimestamp(t, tzlocal.get_localzone())
timestamp = dt.isoformat()

print timestamp
