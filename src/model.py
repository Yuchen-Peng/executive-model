import src.config as c
import logging
import datetime as dt
import os

def main():
	logging.basicConfig(filename='./log/log.log', 
		level=logging.INFO)
	LOOGER = logging.getLogger(__name__)
	LOGGER.info('Model execute\n')
	num_try = 0
	while(num_try <= c.try_limit):
		nb = input('enter a number')
		try:
			nb = float(nb)
			if nb <= c.lowbar:
				print('low')
			elif nb >= c.highbar:
				print('high')
			else:
				print('median')
			LOGGER.info('Execute succeed\n')
			break	
		except:
			num_try += 1
	LOGGER.error('Two many tries\n')



if __name__ == "__main__":
	main()
