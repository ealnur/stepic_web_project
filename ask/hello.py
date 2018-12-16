def application(env, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return "home/box/web/ask/hello.py!\n"#env['QUERY_STRING'].replace('&', '\n') + '\n'




