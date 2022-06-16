from django.shortcuts import render

from django.http import HttpResponse

from myapp.models import Banner, Blurb, Book, HomeInfo

def index(request):
    return render(request, 'whale.html')

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book':book})

def other(request):
    return render(request, 'homepage.html')

def book(request):
	info = HomeInfo()
	info.tagline = "O Viado do gabriel"
	info.example_email = "daniel.barce@gmai.com"
	info.email_button = "danie@gmd"

	ab = Blurb()
	ab.title = "Memorias de alguem"
	ab.content = "Memoriass de alguem"
	ab.link = "www.wayo.com.br"
	ab.link_text = "wayo"
	blurbs = [ab, ab, ab]

	banner = Banner()
	banner.image = "https://instagram.fvix2-1.fna.fbcdn.net/v/t51.2885-19/268986926_1268996120233572_6001274512280062658_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fvix2-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=X2QQAXXGFVoAX-EGLz_&edm=AIQHJ4wBAAAA&ccb=7-4&oh=00_AT_B_qPgje0fONM8Y7v5TioSE8H5W1YeXgUHgfSG1IGy6w&oe=62860F9A&_nc_sid=7b02f1"
	banner.title = "O Sentido da vida é simples se a gente"

	triblurbs = makeTriples(blurbs)

	context = {		
		'banner'				: banner,		
		'welcomemsg'			: info.tagline,	
		'blurbs'				: triblurbs,
		'example_email'			: info.example_email,
		'email_button'			: info.email_button,
		'copyright'				: 'Pending',	
	}
	return render(request, 'book.html', context)

def makeTriples(l):
	if len(l) <= 3:
		return [l]

	l1 = l[::3]
	l2 = l[1::3]
	l3 = l[2::3]

	out = []
	for i in range(len(l3)):
		out.append( [l1[i],l2[i],l3[i]])

	if len(l1) > len(l3):
		out.append([l1[-1]])
	if len(l2) > len(l3):
		out[-1].append(l2[-1])
	return out