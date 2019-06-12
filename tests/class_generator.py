import sys, os, json

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


import klass as c

def test():
    pass


class ClassGenerator:

    def __init__(self, filename):
        self.filename = filename
        self.klass = None
        with open(self.filename, 'r') as file:
            self.data = json.load(file)

    def generate(self):

        self.klass = c.Klass(self.data["name"])

        generated_methods = self._generate_methods(self.klass)
        self.klass = generated_methods["class"]

        if self.data["template"]:
            self.klass.template = self._create_class_template()

        return generated_methods["obj"]

    def _create_class_template(self):
        template = c.Template()

        for tpl in self.data["template"]:
            template.add_template_type(c.TemplateType(tpl["typename"], tpl["datatype"]))

        return template

    def _generate_methods(self, klass):

        obj = []

        for method in self.data["methods"]:
            m = c.Method()
            m.name = method["name"]
            m.return_type = method["return_type"]
            m.related_class = klass

            if method["template"]:
                template = c.Template()

                for tpl in method["template"]:
                    template.add_template_type(c.TemplateType(tpl["typename"], tpl["datatype"]))
                    m.template = template

            if method["arguments"]:
                for arg in method["arguments"]:
                    a = c.Argument()
                    a.identifier = arg["identifier"]
                    a.datatype = arg["datatype"]
                    m.add_argument(a)

            klass.add_method(m)
            obj.append({
                "method": m,
                "expected": method["expected"]
            })

        return {
            "class": klass,
            "obj": obj
        }
