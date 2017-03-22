import webapp2
import cgi
import caesar

def escape_html(s):
    return cgi.escape(s, quote=True)

def build_page(textarea_content):
    rot_label = "<label>Rotate by:</label>"
    rotation_input = "<input type='number' name='rotation'/>"

    message_label = "<label>Type a message:</label>"
    textarea = "<textarea name='text'>" + textarea_content + "</textarea>"

    submit = "<input type='submit'/>"
    form = ("<form method='post'>" +
            rot_label + rotation_input + "<br>" +
            message_label + textarea + "<br>" +
            submit + "</form>")

    header = "<h2>Web Caesar</h2>"

    return header + form

class MainHandler(webapp2.RequestHandler):
    def write_form(self, rot_text=""):
        escaped_text = escape_html(rot_text)
        self.response.write(build_page(escaped_text))

    def get(self):
        self.write_form()

    def post(self):
        user_text = self.request.get('text')
        if self.request.get('rotation'):
            user_rotation = int(self.request.get('rotation'))
        else: user_rotation = 0

        rot_text = caesar.encrypt(user_text, user_rotation)
        self.write_form(rot_text)

app = webapp2.WSGIApplication([('/', MainHandler),
                               ],
 debug=True)
