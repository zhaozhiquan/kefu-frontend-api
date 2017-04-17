# coding=utf-8
import unittest
import os
from time import sleep
import requests as re
import random
import public.methods as t
import public.case_xls as xl
class API5(unittest.TestCase,t.Methods,xl.Case_xls):
	u'''提交图片'''
	def setUp(self):
		self.headers = {self.get_row(0, 11)[0]: self.get_row(0, 11)[1]}  # headers
		self.url = self.get_row(6,1)[1]
		self.key = self.get_row(6,2)        # key
	def tearDown(self):
		pass

	def test_01(self):
		u'''提交图片,正确参数'''
		value = self.get_row(6,3)
		f = open('/Users/zhaozhiquan/automation/kefu-frontend-api/TestCase/1.html','r')
		base = f.read()
		data ={}
		data[self.key[2]] = self.get_token()
		data[self.key[3]] =base
		request = self.apicall(value[1], self.url, data, self.headers)
		f.close()
		print request.status_code
		self.assertEqual(request.status_code,int(value[8]))
		print request.json()
		self.assertIsNotNone(request.json()['data']['id'])

	def test_02(self):
		u'''提交图片,错误(image)参数'''
		value = self.get_row(6, 4)
		data ={}
		data[self.key[2]] = self.get_token()
		data[self.key[3]] =value[3]
		request = self.apicall(value[1], self.url, data, self.headers)
		print request.status_code
		self.assertEqual(request.status_code,int(value[8]))
		print request.json()
		self.assertEqual(request.json()['error_code'], 20001)