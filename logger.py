from datetime import datetime
import os


def logger(path):
    log_path = os.path.join(path, 'log.txt')

    def _logger(old_function):
        statistics = {}

        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            statistics['starting_time'] = datetime.now().ctime()
            statistics['name'] = old_function.__name__
            statistics['args'] = args
            statistics['kwargs'] = kwargs
            statistics['result'] = result
            with open(log_path, 'w', encoding='utf-8') as log:
                print(statistics, file=log)
            return result

        return new_function

    return _logger
