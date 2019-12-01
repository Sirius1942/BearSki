from BearSki.utils.logger import SkiLogger

if __name__ == '__main__':
    log = SkiLogger("name")
    log.debug('debug信息')
    log.info('info信息')
    log.war('warning信息')
    log.error('error信息')
    log.critical('critical信息')