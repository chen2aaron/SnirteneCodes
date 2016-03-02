import logging


logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s %(asctime)s %(name)s:%(lineno)d] %(message)s',
)
logging.warning('warning')
logger = logging.getLogger('main')

def main():
    logger.error('error')


if __name__ == '__main__':
    main()
