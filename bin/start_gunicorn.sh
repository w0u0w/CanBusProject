#!/bin/bash
	source /home/www/code/CanBusProject/env/bin/activate
	exec gunicorn -c "/home/www/code/CanBusProject/CanBusProject/CanBusProject/" CanBusProject.wsgi