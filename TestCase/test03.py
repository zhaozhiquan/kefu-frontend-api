# coding=utf-8
import unittest
import os
from time import sleep
import requests as re
import random
import public.methods as t
import public.case_xls as xl
class API3(unittest.TestCase,t.Methods,xl.Case_xls):
	u'''我的问题详情'''
	def setUp(self):
		self.headers = {self.get_row(0, 11)[0]: self.get_row(0, 11)[1]}  # headers
		self.url = self.get_row(4,1)[1]
		self.key = self.get_row(4,2)        # key
	def tearDown(self):
		pass

	def test_01(self):
		u'''我的问题详情,正确参数'''
		questions_id = self.get_questions_id2()
		#################获取我的问题id
		value = self.get_row(4,3)
		data = {}
		data[self.key[2]] = self.get_token()
		data[self.key[3]] = questions_id
		request = self.apicall(value[1],self.url,None,self.headers,data)
		print request.status_code
		self.assertEqual(request.status_code, int(value[8]))
		print request.json()
		self.assertEqual(request.json()['data']['meta']['id'], questions_id)


	def test_02(self):
		u'''我的问题详情,错误参数'''
		value = self.get_row(4, 4)
		data = {}
		data[self.key[2]] = self.get_token()
		data[self.key[3]] = ''
		request = self.apicall(value[1], self.url, None, None, data)
		print request.status_code
		self.assertEqual(request.status_code, int(value[8]))
		print request.json()
		self.assertEqual(request.json()['error_code'], int(value[9]))