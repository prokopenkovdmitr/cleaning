from django.shortcuts import render

def main(request):
	test = '1'
	test2 = '2'
	data = {
		'test': test,
		'test2': test2,
		}
	return render(request, 'main/main.html', {'data': data})


def electrician(request):
	test = '1'
	test2 = '2'
	data = {
		'test': test,
		'test2': test2,
		}
	return render(request, 'main/electrician.html', {'data': data})

def plumber(request):
	test = '1'
	test2 = '2'
	data = {
		'test': test,
		'test2': test2,
		}
	return render(request, 'main/plumber.html', {'data': data})

def cleaning(request):
	test = '1'
	test2 = '2'
	data = {
		'test': test,
		'test2': test2,
		}
	return render(request, 'main/cleaning.html', {'data': data})