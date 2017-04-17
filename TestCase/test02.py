# coding=utf-8
import unittest
import os
from time import sleep
import requests as re
import random
import public.methods as t
import public.case_xls as xl
class API2(unittest.TestCase,t.Methods,xl.Case_xls):
	u'''提交问题,我的问题列表'''
	def setUp(self):
		self.headers = {self.get_row(0, 11)[0]: self.get_row(0, 11)[1]}  # headers
		self.url = self.get_row(3,1)[1]
		self.key = self.get_row(3,2)        # key
	def tearDown(self):
		pass

	def test_01(self):
		u'''提交问题,正确必填参数'''
		value = self.get_row(3,3)
		data = {}
		data[self.key[2]] = self.get_token()
		data[self.key[3]] = random.choice(xrange(100000000000))
		data[self.key[4]] = int(value[4])
		request = self.apicall('POST', self.url,data,self.headers)
		print request.status_code
		self.assertEqual(request.status_code, int(value[8]))
		print (request.json())
		self.assertIsNotNone(request.json()['data']['id'])

	def test_02(self):
		u'''提交问题,错误必填(question)参数'''
		value = self.get_row(3,4)
		data = {}
		data[self.key[2]] = self.get_token()
		data[self.key[3]] = None
		request = self.apicall(value[1], self.url, data, self.headers)
		print request.status_code
		self.assertEqual(request.status_code, int(value[8]))
		print (request.json())
		self.assertEqual(request.json()['error_code'],int(value[9]))

	def test_03(self):
		u'''我的问题列表,正确必填参数'''
		value = self.get_row(3, 5)
		data = {}
		data[self.key[2]] = self.get_token()
		request = self.apicall(value[1], self.url, None, self.headers, data)
		print request.status_code
		self.assertEqual(request.status_code, int(value[8]))
		print request.json()
		self.assertIsNotNone(request.json()['data'][0]['id'])


	def test_04(self):
		u'''我的问题列表,正确选填参数'''
		value = self.get_row(3, 6)
		data = {}
		data[self.key[2]] = self.get_token()
		data[self.key[5]] = 2
		data[self.key[6]] = 1
		request = self.apicall(value[1], self.url, None, self.headers, data)
		print request.status_code
		self.assertEqual(request.status_code, int(value[8]))
		print request.json()
		self.assertEqual(len(request.json()['data']), int(value[9]))


	def test_05(self):
		u'''我的问题列表,错误选填参数(pagesize)'''
		value = self.get_row(3, 7)
		data = {}
		data[self.key[2]] = self.get_token()
		data[self.key[5]] = value[5]
		request = self.apicall(value[1], self.url, None, self.headers, data)
		print request.status_code
		self.assertEqual(request.status_code, int(value[8]))
		print request.json()
		self.assertIsNotNone(request.json()['error_code'], int(value[9]))


	def test_06(self):
		u'''我的问题列表,错误选填参数(current)'''
		value = self.get_row(3, 8)
		data = {}
		data[self.key[2]] = self.get_token()
		data[self.key[6]] = value[6]
		request = self.apicall(value[1], self.url, None, self.headers, data)
		print request.status_code
		self.assertEqual(request.status_code, int(value[8]))
		print request.json()
		self.assertIsNotNone(request.json()['error_code'], int(value[9]))