from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from cms_sorl_pictures.models import SorlPicture
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
        
        picture_options = {}
        if instance.crop:
            picture_options['crop'] = instance.crop
        if instance.upscale:
            picture_options['upscale'] = 'TRUE'
        else:
            picture_options['upscale'] = 'FALSE'
        if instance.quality:
            picture_options['quality'] = instance.quality
        if instance.progressive:
            picture_options['progressive'] = 'TRUE'
        else:
            picture_options['progressive'] = 'FALSE'
        if instance.format:
            picture_options['format'] = instance.format
        if instance.colorspace:
            picture_options['format'] = instance.colorspace
        if instance.orientation:
            picture_options['orientation'] = 'TRUE'
        else:
            picture_options['orientation'] = 'FALSE'
        
        picture_dimensions = "200x200"
        if instance.height or instance.width:
            picture_dimensions = str(instance.width) + "x" + str(instance.height)
        
        context.update({
            'picture': instance,
            'picture_dimensions': picture_dimensions,
            'picture_options': picture_options,
            'link': link, 
            'placeholder': placeholder
        })
        return context 
    
    def icon_src(self, instance):
        # TODO - possibly use 'instance' and provide a thumbnail image
        return settings.STATIC_URL + u"cms/images/plugins/image.png"
 
plugin_pool.register_plugin(SorlPicturePlugin)
