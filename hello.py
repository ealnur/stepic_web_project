def application(env, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return "Hello World!\n"#env['QUERY_STRING'].replace('&', '\n') + '\n'




