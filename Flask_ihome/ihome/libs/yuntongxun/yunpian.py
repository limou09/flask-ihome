import random
import requests

#	云片网apikey和短信接口
#APIKEY = 'bac3ee2e9148cddb37a49a2249df73ee'
APIKEY = '593dfe293a137f0035395fbd85743ec8'
APIURL = 'https://sms.yunpian.com/v2/sms/single_send.json'

class YunPian():

	def __init__(self):
		self.apikey = APIKEY
		self.apiurl = APIURL

	@staticmethod
	def make_code():
		code = ''.join(random.sample('0123456789',4))
		print('make_code', code)
		return code

	def send_code(self, mobile, code):
		data = {
			'apikey':self.apikey,
			'mobile':mobile,
			'text':'您的验证码是{}'.format(code)
		}

		response = requests.post(url=self.apiurl, data=data)
		print("send_code", response.json())
		#	send_code {'code': 0, 'msg': '发送成功', 'count': 1, 'fee': 0.05, 'unit': 'RMB', 'mobile': '17600751930', 'sid': 40143391772}
		return response.json()

# #	测试代码
# if __name__ == '__main__':
# 	yun = YunPian()
# 	code = yun.make_code()
# 	yun.send_code('17600751930',code)
