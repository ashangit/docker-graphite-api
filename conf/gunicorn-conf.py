__author__ = 'nicolasfraison'

import os

workers = os.environ['WORKER_PROCESSES']
timeout = os.environ['TIMEOUT']
preload_app = True