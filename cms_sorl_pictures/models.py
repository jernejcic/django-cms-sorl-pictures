from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page
from os.path import basename

class SorlPicture(CMSPlugin):
    """
    A Picture with or without a link
    """
    CENTER = "center"
    LEFT = "left"
    RIGHT = "right"
    FLOAT_CHOICES = ((CENTER, _("center")),
                     (LEFT, _("left")),
                     (RIGHT, _("right")),
                     )
    
    PNG = "PNG"
    JPEG = "JPEG"
    FORMAT_CHOICES = ((PNG, _("png")),
                      (JPEG, _("jpeg")),
                      )
    
    RGB = "RGB"
    GRAY = "GRAY"
    COLORSPACE_CHOICES = ((RGB, _("rgb")),
                          (GRAY, _("gray")),
                          )
    
    BOTTOM = "bottom"
    TOP = "top"
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    #SMART = "smart" # Doesn't seem to be working.
    NOOP = "noop"
    CROP_CHOICES = ((NOOP, _("noop")),
                    (CENTER, _("center")),
                    (TOP, _("top")),
                    (RIGHT, _("right")),
                    (BOTTOM, _("bottom")),
                    (LEFT, _("left")),
                    )
    
    
    image = models.ImageField(_("image"), upload_to=CMSPlugin.get_media_path)
    url = models.CharField(_("link"), max_length=255, blank=True, null=True, help_text=_("if present image will be clickable"))
    page_link = models.ForeignKey(Page, verbose_name=_("page"), null=True, blank=True, help_text=_("if present image will be clickable"))
    alt = models.CharField(_("alternate text"), max_length=255, blank=True, null=True, help_text=_("textual description of the image"))
    longdesc = models.CharField(_("long description"), max_length=255, blank=True, null=True, help_text=_("additional description of the image"))
    float = models.CharField(_("side"), max_length=10, blank=True, null=True, choices=FLOAT_CHOICES)
    width = models.IntegerField(_("width"), blank=True, null=True, help_text=_("in pixels; the max width that you want to display the image at"))
    height = models.IntegerField(_("height"), blank=True, null=True, help_text=_("in pixels; the max height that you want to display the image at"))
    crop = models.CharField(_("crop"), max_length=20, blank=True, null=True, choices=CROP_CHOICES, help_text=_("requires a width and height; 'noop' to simply scale the photo to fit, 'center' to scale and crop from the center from the smallest dimensions, 'top' to cut off the bottom, 'bottom', 'left, 'right', etc.; an incorrect value in this field will prevent the image from displaying"))
    upscale = models.BooleanField(_("upscale"), default=False, help_text=_("if the image is smaller then the defined dimensions, it will be enlarged to fit"))
    quality = models.IntegerField(_("quality"), blank=True, null=True, help_text=_("value from 0 - 100; if defined will determing the quality of the image; hire quality results in larger file sizes"))
    progressive = models.BooleanField(_("progressive"), default=True, help_text=_("save jpeg's as progressive jpeg's"))
    format = models.CharField(_("format"), max_length=10, blank=True, null=True, choices=FORMAT_CHOICES)
    colorspace = models.CharField(_("colorspace"), max_length=10, blank=True, null=True, help_text=_("create thumbnails in color or grayscale"), choices=COLORSPACE_CHOICES)
    orientation = models.BooleanField(_("orientation"), default=True, help_text=_("orient the thumbnails using the source image's EXIF tags for orientation"))
    
    def __unicode__(self):
        if self.alt:
            return self.alt[:40]
        elif self.image:
            # added if, because it raised attribute error when file wasn't defined
            try:
                return u"%s" % basename(self.image.path)
            except:
                pass
        return "<empty>"
