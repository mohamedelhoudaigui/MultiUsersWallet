from flask import jsonify

def route_handling(query, interactor_function):
	try:
		if not query:
			return jsonify({
				'success': False, 
				'message': 'No query provided'
			}), 400

		result = interactor_function(query)
		return jsonify({
			'success': True,
			'data': result
		}), 200

	except Exception as e:
		print(f"exception in route: {str(e)}")
		return jsonify({
			'success': False,
			'message': 'An error occurred',
			'error': str(e)
		}), 500