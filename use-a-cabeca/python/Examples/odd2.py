import time
from datetime import datetime
from random import randint


odds = [1, 3, 5, 7 , 9, 11, 13, 15, 17, 19,
	  21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
	  41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

#
for i in range(5):
	right_this_minute = datetime.today().minute

	if(right_this_minute in odds):
		print('Este minuto parece com ímpar.')
	else:
		print('Não é um minuto ímpar.')

	# Módulo time, com o submódulo sleep, com uma variação de valorese entre 1 e 60 do módulo random com o randint.
	time.sleep(randint(1, 60))