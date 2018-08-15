import config as c
import logging
import datetime as dt
import os
from pathlib import Path


def main():
	date = dt.datetime.now().strftime('%y-%m-%d')
	time = dt.datetime.now().strftime('%y-%m-%d %H:%M:%S')
	logfile_name = './log/' + date + '_log.log'
	logfile_path = Path(logfile_name)
	copy = 1
	while logfile_path.exists():
		logfile_name = './log/' + date + '_log_' + str(copy) + '.log' 
		copy += 1
		logfile_path = Path(logfile_name)
	logging.basicConfig(filename=logfile_name, 
		level=logging.INFO)
	LOGGER = logging.getLogger(__name__)
	LOGGER.info('Model Execute at: ' + time  + '\n')
	LOGGER.info('Model execute\n')
	num_try = 0
	while(num_try <= c.try_limit):
		nb = input('enter a number:')
		try:
			nb = float(nb)
			print(nb)
			if nb <= c.low_bar:
				print('low')
			elif nb >= c.high_bar:
				print('high')
			else:
				print('median')
			LOGGER.info('Execute succeed\n')
			break	
		except:
			num_try += 1
	if num_try >= c.try_limit:
		LOGGER.error('Two many tries\n')



if __name__ == "__main__":
	main()
