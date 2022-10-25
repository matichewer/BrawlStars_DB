import logging as log

def mi_funcion():  
    log.warning('esto es un warning')
    log.info('esto es un info') 
    log.debug('esto es un debug')
    log.error('esto es un error')
    log.critical('esto es un critical')


log.basicConfig(filename='example.log', 
                    encoding='utf-8', 
                    level=log.DEBUG,
                    format='%(asctime)s, %(levelname)-8s, [%(filename)s:%(funcName)s:%(lineno)d], %(message)s',
                    datefmt='%Y-%m-%d, %H:%M:%S')

mi_funcion()
