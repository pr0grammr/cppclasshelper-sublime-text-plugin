class Template:

    def __init__(self):
        self._template_types = []

    @property
    def template_types(self):
        return self._template_types

    def add_template_type(self, template_type):
        self._template_types.append(template_type)

    def __str__(self):
        template = "template <{content}>"
        render = []

        for template_type in self._template_types:
            render.append(template_type)

        return template.format(content=', '.join(render))