from django.utils.deprecation import MiddlewareMixin
import re


class HtmlMinificationMiddleware(MiddlewareMixin):
    """ Used for Html minifcation """
    def process_response(self, request, response):
        if not response.streaming and response.has_header('Content-Type'):
                if 'text/html; charset=utf-8' in response.__getitem__('Content-Type'):
                    response.content = self.replace_byte_value(
                        response.content, ['\n', ''], [r'>(\s+)<', '><'])
        return response

    def replace_byte_value(self, byte, *vals):
        str_val = byte.decode('utf-8')
        for val in vals:
            p = re.compile(val[0])
            str_val = p.sub(val[1], str_val)
        return str.encode(str_val)
