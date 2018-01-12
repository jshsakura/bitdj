from django.forms import widgets
from django.template import loader
from django.utils.safestring import mark_safe


class SimpleMDEWidget(widgets.Textarea):
    # 템플릿 파일이 앱 안에 존재하도록 했다. 이는 별도의 앱으로 제작할 때 동작한다.
    template_name = 'simplemde/simplemde.html'

    # static/simplemde 디렉토리 안에 있는 CSS와 자바스크립트 파일을 불러온다.
    # simplemde.min.css와 simplemde.min.js 파일은 SimpleMDE에서 배포하는 파일이다.
    class Media:
        css = {
            'all': (
                'simplemde/simplemde.min.css',
                'simplemde/custom.css',
            )
        }
        js = (
            'simplemde/simplemde.min.js',
        )

    def __init__(self, attrs=None, wrapper_class='simplemde-box', options=''):
        # 템플릿을 출력할 때 wrapper_class와 options 변수를 넘겨주기 위해 가져온다.
        self.wrapper_class = wrapper_class
        self.options = options

        super(SimpleMDEWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None, renderer=None):
        context = {
            'widget': {
                'name': name,
                'value': value,
                'wrapper_class': self.wrapper_class,
                'options': self.options,
            }
        }

        # 템플릿을 렌더링한다.
        template = loader.get_template(self.template_name).render(context)

        # 템플릿 파일의 문자열을 이스케이프하고 반환한다.
        return mark_safe(template)