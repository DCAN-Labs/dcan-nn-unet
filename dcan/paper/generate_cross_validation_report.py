from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("dcan.paper"),
    autoescape=select_autoescape()
)

template = env.get_template("10FoldValidationResults.md")

print(template.render(the="variables", go="here"))
