import csv,sys
from datetime import datetime

filename = sys.argv[1]
#time_opt = sys.argv[2]
'''
with open(filename,'rb') as f:
	reader = csv.reader(f)
	i = 0
	line = reader.next()
	print line[0]
	for row in reader:
		if i == 5:
			break
		else:
			i = i +1
		print datetime.fromtimestamp(float(row[0]))
'''

def opencsv(filename):
	f = open(filename,'rb')
	reader = csv.reader(f)
	return reader


def ochl_min(reader,minutes):
	#OCHL for btc data in x minute segments of time
	ochl = []
	current_line = reader.next()
	print "current line: {}".format(current_line)
	current_time = float(current_line[0])
	o = float(current_line[1])
	c = float(current_line[1])
	h = float(current_line[1])
	l = float(current_line[1])

	block = minutes * 60
	end = current_time + block
	print "block: {}\nend: {}".format(block,end)

	for row in reader:
		time = float(row[0])
		price = float(row[1])
		if time <= end:
			if price > h:
				h = float(row[1])
			if price < l:
				l = float(row[1])
			c = float(row[1])

		else:
			end= "{}".format(datetime.fromtimestamp(end))
			ochl.append([end,o,c,h,l])
			end = time + block
			o = float(row[1])
			c = float(row[1])
			h = float(row[1])
			l = float(row[1])	
			print "End block time: {}".format(datetime.fromtimestamp(end))

	return ochl

reader = opencsv(filename)
ochl = ochl_min(reader, 1440)

i = 0
for x in ochl:
	if i == 1000:
		break
	else:
		i = i + 1
	print x
