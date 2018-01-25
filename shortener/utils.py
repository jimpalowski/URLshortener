import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
	###new_code = ''
	#for x in range(size):
		#new_code += random.choic(chars)
	#return new_code	
	return ''.join(random.choice(chars) for x in range(size))


def create_shortcode(instance, size=SHORTCODE_MIN):
	new_code = code_generator(size=size)
	Klass = instance.__class__
	qs_exists = Klass.objects.filter(shortcode=new_code).exists()
	if qs_exists:
		return create_shortcode(size=size)
	return new_code		


