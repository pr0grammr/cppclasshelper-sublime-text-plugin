from .klass import *


class ClassParser:

    @classmethod
    def parse(cls, input_obj):
        """
        create python classes from tokenized JSON object
        :param input_obj:
        :return: Klass
        """

        klass = Klass(input_obj["name"])

        klass.namespace = input_obj["namespace"]

        if input_obj["methods"]:
            for method in cls._parse_methods(input_obj["methods"]):
                method.related_class = input_obj["name"]
                klass.add_method(method)

        klass.template = TemplateParser().parse(input_obj["template"])

        return klass

    @classmethod
    def _parse_methods(cls, input_methods):
        for method in input_methods:
            method = MethodParser().parse(method)

            yield method


class MethodParser:

    @classmethod
    def parse(cls, input_method):
        method = Method()

        method.name = input_method["name"]
        method.template = TemplateParser().parse(input_method["template"])
        method.is_const = input_method["is_const"]
        method.is_pure_virtual = input_method["is_pure_virtual"]

        for argument in input_method["arguments"]:
            method.add_argument(argument)

        method.return_type = input_method["return_type"]

        return method


class TemplateParser:

    @classmethod
    def parse(cls, input_obj):

        if input_obj is None:
            return

        template = Template()

        for template_type in input_obj:
            template_type_class = TemplateType(template_type["typename"], template_type["datatype"])
            template.add_template_type(template_type_class)

        return template