__author__ = 'TIF'


def footer():
    print 'footer'


class Renderer(object):
    def __init__(self):
        self.header = ''
        self.paragraph = ''

    def header(self, header):
        self.header = header

    def paragraph(self, paragraph):
        self.paragraph = paragraph

    def footer(self):
        pass


class Page(object):
    def __init__(self, title, renderer):
        if not isinstance(renderer, Renderer):
            raise TypeError("Excepted object of type Render,got{}".format(type(renderer).__name__))
        self.title = title
        self.renderer = renderer
        self.paragraphs = []

    def add_paragraph(self, paragraph):
        self.paragraphs.append(paragraph)

    def render(self):
        self.renderer.header(self.title)
        for paragraph in self.paragraphs:
            self.renderer.paragraph(paragraph)
        self.renderer.footer()
