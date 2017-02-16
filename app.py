#!/usr/bin/env python3

from flask import Flask, jsonify, render_template, request
import nmap, whois

app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/nmap/')
def nmap_home():
  return render_template('scan_input.html')

""" NMAP scan using CIDR notation to check a target Range """
@app.route('/user_scan_results/')
def scan_results():
	nm = nmap.PortScanner()
	ip = request.args.get('ip', '192.168.0.1')
	ports = request.args.get('ports', '21-80')
	cidr = request.args.get('cidr','32')
	flags = request.args.get('flags', '-v')
	context={'nm': nm.scan(hosts=ip+'/'+cidr, arguments=flags+' '+'-p'+ports)}
	#add context values and context parameter to render_template call
	return render_template('nmap.html', **context)

if __name__ == '__main__':
	app.run(debug=True)


