import sys

import logbook


level = logbook.TRACE
# level = logbook.ERROR
#log_filename = 'app.log'
log_filename = None

if not log_filename:
    logbook.StreamHandler(sys.stdout, level=level).push_application()
else:
    logbook.TimedRotatingFileHandler(log_filename, level=level).push_application()


app_log = logbook.Logger('App')

# actions are:
# notice / info / trace / warn / error / critical
app_log.notice('some notice message')
app_log.error('some error message')
