import os
import sys

from app import app

from livereload import Server


def main():

	server = Server(app.wsgi_app)
	server.watch(filepath='/'.join([os.getcwd(),'*']))
	server.serve(liveport=4999, host='127.0.0.1', port=5000)


if __name__ == '__main__':
	main()
