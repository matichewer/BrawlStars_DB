import logging
from logging.config import fileConfig
import os
from pathlib import Path
import sys

def mi_funcion():  
    log.warning('esto es un warning')
    log.info('esto es un info') 
    log.debug('esto es un debug')
    log.error('esto es un error')
    log.critical('esto es un critical')
    print(Path(__file__).stem)



fileConfig('log-config.ini', defaults={ 'file-name': Path(__file__).stem })
log = logging.getLogger()


mi_funcion()