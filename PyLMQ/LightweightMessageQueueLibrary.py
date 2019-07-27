#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests


class LightweightMessageQueueLibrary:

	def __init__(self, hosts='http://localhost:3000'):
		if type(hosts) is not list:
			hosts = [hosts]
		self._hosts = hosts

	def help(self, host_index=0):
		req = requests.get('%s/help' % self._hosts[host_index])
		if req.status_code == 200:
			return req.text
		else:
			raise Exception(req.status_code, req.text)

	def list(self, host_index=0):
		req = requests.get('%s/list' % self._hosts[host_index])
		if req.status_code == 200:
			return req.text
		else:
			raise Exception(req.status_code, req.text)

	def count(self, queue, host_index=0):
		req = requests.get('%s/count/%s' % (self._hosts[host_index], queue))
		if req.status_code == 200:
			return int(req.text)
		else:
			raise Exception(req.status_code, req.text)

	def skip(self, queue, number, host_index=0):
		req = requests.get('%s/skip/%s/%s' % (self._hosts[host_index], queue, number))
		if req.status_code == 200:
			return 0
		else:
			raise Exception(req.status_code, req.text)

	def set(self, queue, message, host_index=0):
		req = requests.get('%s/set/%s/%s' % (self._hosts[host_index], queue, message))
		if req.status_code == 200:
			return 0
		else:
			raise Exception(req.status_code, req.text)

	def get(self, queue, host_index=0):
		req = requests.get('%s/get/%s' % (self._hosts[host_index], queue))
		if req.status_code == 200:
			return {
				'uid': req.headers.get('Uid', None),
				'message': req.text
			}
		else:
			raise Exception(req.status_code, req.text)

	def circle_get(self, queues, last_index=0):
		last_exception = Exception('Nothing!')
		indices = list(range(last_index + 1, len(queues))) + list(range(0, last_index + 1))
		for index in indices:
			try:
				host_index, queue, active = queues[index]
				if not active:
					continue
				output = self.get(queue, host_index)
				return index, output
			except Exception as exception:
				last_exception = exception
		raise last_exception

	def fetch(self, queue, host_index=0):
		req = requests.get('%s/fetch/%s' % (self._hosts[host_index], queue))
		if req.status_code == 200:
			return {
				'uid': req.headers.get('Uid', None),
				'message': req.headers.get('Message', None),
				'content': req.content
			}
		else:
			raise Exception(req.status_code, req.text)

	def circle_fetch(self, queues, last_index=0):
		last_exception = Exception('Nothing!')
		indices = list(range(last_index + 1, len(queues))) + list(range(0, last_index + 1))
		for index in indices:
			try:
				host_index, queue, active = queues[index]
				if not active:
					continue
				output = self.fetch(queue, host_index)
				return index, output
			except Exception as exception:
				last_exception = exception
		raise last_exception

	def download(self, message, host_index=0):
		req = requests.get('%s/download/%s' % (self._hosts[host_index], message))
		if req.status_code == 200:
			return req.content
		else:
			raise Exception(req.status_code, req.text)

	def delete(self, queue, host_index=0):
		req = requests.get('%s/delete/%s' % (self._hosts[host_index], queue))
		if req.status_code == 200:
			return 0
		else:
			raise Exception(req.status_code, req.text)


if __name__ == "__main__":
	lmql = LightweightMessageQueueLibrary()
	try:
		res = lmql.help()
		print(res)
	except Exception as exception:
		print(exception)
