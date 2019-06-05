
from celery import Celery
from ihome.libs.yuntongxun.yunpian import YunPian


# 定义celery对象
celery_app = Celery("ihome", broker="redis://127.0.0.1:6379/1", backend="redis://127.0.0.1:6379/2")


@celery_app.task
def send_sms(mobile, code):
	"""发送短信的异步任务"""
	yun = YunPian()
	yun.send_code(mobile, code)


# celery开启的命令,	celery4.3版本启动有问题，先pip install eventlet 然后在启动任务命令后加 -P eventlet
# celery -A tasks worker -l info -P eventlet




# celery -A ihome.tasks.task_sms worker -l info -P eventlet

