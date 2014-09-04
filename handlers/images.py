import StringIO
import hashlib

from tornado.web import HTTPError
from PIL import Image, ImageDraw, ImageColor

from base import BaseHandler


class ImageHandler(BaseHandler):
    def _make_hex_from_string(self, some_string=None):
        if not some_string:
            return "#000000"

        m = hashlib.md5()
        m.update(some_string)
        return "#{0}".format(m.hexdigest()[:6])

    def get(self, image_name, image_type):
        if image_type not in ("gif", "png", "jpg"):
            raise HTTPError(404)

        if image_type == "png":
            size = (50, 50)
            color = ImageColor.getrgb(self._make_hex_from_string(image_name))
            im = Image.new('RGB', size, color)
            self.set_header('Content-Type', 'image/png')

            output = StringIO.StringIO()
            im.save(output, format='PNG')
            contents = output.getvalue()
            output.close()
            self.write(contents)
        else:
            raise HTTPError(404)
