import logging

def mi_funcion():  
    logging.warning('esto es un warning')
    logging.info('esto es un info') 
    logging.debug('esto es un debug')
    logging.error('esto es un error')
    logging.critical('esto es un critical')


logging.basicConfig(handlers=[
                            logging.FileHandler(
                                        filename="test-log.log", 
                                        encoding='utf-8', 
                                        mode='a+'
                                    )
                            ],
                    format='%(asctime)s, %(levelname)-8s, [%(filename)s:%(funcName)s:%(lineno)s], %(message)s',
                    datefmt='%Y-%m-%d, %H:%M:%S, %A', 
                    level=logging.DEBUG)


mi_funcion()
