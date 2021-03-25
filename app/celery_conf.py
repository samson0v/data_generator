from .settings import TIME_ZONE, USE_TZ


accept_content = ['json']
task_serializer = 'json'
result_serializer = 'json'

task_ignore_result = True

if USE_TZ:
    enable_utc = True
    timezone = TIME_ZONE

worker_disable_rate_limits = True
worker_hijack_root_logger = False

broker_url = 'amqp://test:test@52.15.48.191:4369/myvhost'
# broker_url = 'redis://:foobared@3.137.186.254:6379/0'
