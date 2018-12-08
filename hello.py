def application(env, start_response):
	start_response('200 OK', [('Content/type', 'text/plain')])
	return [i + '\n' for i in env['QUERY_STRING'].split('&')]
#	[i + '\n' for i in env['QUERY_STRING'].split(&)]



