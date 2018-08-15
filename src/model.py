import config as c
import logging
import datetime as dt
import os
from pathlib import Path
import random


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
		input = random.randint(-10,10)
		if input >= 0:
			return input**2
			LOGGER.info('Execute succeed\n')
		else:
			num_try += 1
	if num_try >= c.try_limit:
		LOGGER.error('Two many tries\n')
		raise ValueError('Invalid input')



if __name__ == "__main__":
	main()
