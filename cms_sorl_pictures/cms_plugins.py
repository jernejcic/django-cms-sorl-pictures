from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from skiandsnow.cms_sorl_pictures.models import SorlPicture
from django.conf import settings

class SorlPicturePlugin(CMSPluginBase):
    model = SorlPicture
    name = _("Sorl Picture")
    render_template = "cms/plugins/sorl_picture.html"
    text_enabled = True
    
    def render(self, context, instance, placeholder):
        if instance.url:
            link = instance.url
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""
        context.update({
            'picture': instance,
            'link': link, 
            'placeholder': placeholder
        })
        return context 
    
    def icon_src(self, instance):
        # TODO - possibly use 'instance' and provide a thumbnail image
        return settings.STATIC_URL + u"cms/images/plugins/image.png"
 
plugin_pool.register_plugin(SorlPicturePlugin)
