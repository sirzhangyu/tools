#coding: utf-8

# use logging
import logging
logging.exception('customised comments')

# without logging
import traceback
def log_traceback(ex, ex_traceback=None):
    if ex_traceback is None:
        ex_traceback = ex.__traceback__
    tb_lines = [ line.rstrip('\n') for line in
                traceback.format_exception(ex.__class__, ex, ex_traceback)]
    exception_logger.log(tb_lines)
# except Exception as ex:
# Pythoh 3
log_traceback(ex)
# Python 2
_, _, ex_traceback = sys.exc_info()
log_traceback(ex, ex_traceback)
