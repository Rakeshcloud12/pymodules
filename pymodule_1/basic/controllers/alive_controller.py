from basic import logger


def is_alive():
    logger.info("Calling Keep Alive")
    return "Module_1 is alive {Some dummy data}", 200