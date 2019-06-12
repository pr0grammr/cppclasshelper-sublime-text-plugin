import sys, os

sys.path.append(os.path.realpath(__file__))


import klass as c

klass1 = c.Klass("User")

template1 = c.Template()
template1.add_template_type(c.TemplateType('typename', 'T'))

method1 = c.Method()
method1.template = template1
method1.return_type = 'T'
method1.related_class = klass1
method1.name = 'get'

klass1.add_method(method1)


def test_render():
    assert str(method1) == "template <typename T> T User::get() {}"
