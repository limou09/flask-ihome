# flask-ihome

使用flask完成的一个移动端租房系统，整个系统涉及到了redis缓存、验证码、短信验证码、csrf机制、图片存储服务、celery任务队列、支付宝支付接口等技术。项目采用restful风格进行编码.

实现功能：
  
  1.登录注册，使用captcha模块生成图片验证码，使用celery实现异步执行云片第三方短信服务发送短信。
  
  2.个人信息，将用户头像和房间图片存储至七牛云存储。
  
  3.城区信息，采用redis做缓存。解决缓存数据的同步问题，保证mysql和redis数据的一致性。
  
  4.发布房源，只有实名认证过的用户才有发布房源的权限
  
  5.房屋管理，完成数据的页面渲染。实现对用户的身份识别，如果是此房间的发布人（房东）不可以进行预定房间操作，如果是其他用户可以完成预定操作。
  
  6.房屋列表，实现数据的页面渲染。对数据实现limit分页和数据排序（入住最多，最新发布，价格最低...）。redis局部缓存的实现
  
  7.订单，使用js动态完成金额计算。订单页面用户提交订单生成一串订单号，后端计算订单金额将订单信息转发到支付宝接口用户进行付费操作，房东可以接单也可以拒单
  
目录结构：

Flask_ihome/

├─ihome # 项目主程序

│  ├─api_1_0  # v1.0版本

│  │  ├─keys  # 支付宝支付公钥私钥

│  │  ├─__init__.py 

│  │  ├─houses.py # 房屋管理

│  │  ├─orders.py # 订单

│  │  ├─passprot.py # 用户，登录注册

│  │  ├─pay.py # 发起支付请求，保存支付结果

│  │  ├─profile.py # 个人信息

│  │  ├─verify_code.py # 验证码

│  ├─libs # 第三方服务

│  │  ├─yuntongxun  #短信服务

│  │  │  └─yunpian.py 短信接口

│  ├─static # 静态文件  

│  ├─tasks  # 异步任务

│  │  └─__init__.py

│  │  └─task_sms.py 短信异步任务

│  ├─utils

│  │  ├─captcha # 第三方图片验证码

│  │  ├─commons.py # 公用方法（检测登录状态，正则转换器）

│  │  ├─image_storage.py # 将文件存储至七牛云

│  │  ├─response_code.py # 项目中所需的自定义状态码

│  │  ├─1.png # 将1.png当做一个容器，将需要上传到七牛的图片先存放至本地 然后在上传到云服务

│  │  └─__init__.py

│  ├─constants.py  # 项目中所有的常量

│  ├─models.py  # 模型类

│  ├─web_html.py  # 提供静态文件，给页面添加csrf机制

├─logs  # 存放项目日志文件

├─migrations  #执行迁移自动生成的文件

├─config.py  #配置文件

├─manage.py  #项目入口文件

└─requirements.txt  # 项目所属依赖
    


基本使用：

  python manage.py runserver 
  
  在manage.py文件的同级目录下启动celery,celery4.0+版本后启动celery任务有点问题 需要在启动命令后面 加-P eventlet参数
  
  -P eventlet参数 需要安装  pip install eventlet
  
  celery -A ihome.tasks.task_sms worker -l info -P eventlet
