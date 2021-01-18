
from configuration import Configuration
from concurrent import futures


def get_executor(configuration: Configuration) -> futures.Executor:
    if configuration.multiproc_enabled:
        return futures.ProcessPoolExecutor(max_workers=configuration.multiproc_num_processes)
    else:
        return futures.ThreadPoolExecutor(max_workers=1)
