# To use, you'll want to impor this from your own admin.py file:
# 
#     from tiledinline.admin import TiledInline
#     MyModelInline(TiledInline):
#         model = MyModel


from django.contrib import admin

class TiledInline(admin.options.InlineModelAdmin):
    template = 'admin/edit_inline/tiled.html'
    tiled_by_default = True
