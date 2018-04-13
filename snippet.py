from datetime import datetime, timedelta
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
if __name__ == '__main__':
    from optparse import OptionParser
    now = datetime.now()
    parser = OptionParser()
    parser.add_option('-d', '--datetime', dest='stat_time',
                      default=now.strftime(TIME_FORMAT),
                      help='stat time, format: %s' % TIME_FORMAT)
    options, _ = parser.parse_args()
    print datetime.strptime(options.stat_time, TIME_FORMAT)
