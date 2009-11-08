from django.contrib import admin

class TiledInline(admin.options.InlineModelAdmin):
	template = 'admin/edit_inline/tiled.html'
	tiled_by_default = True