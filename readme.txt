Just slap this app into your INSTALLED_APPS list in settings.py.

To use the TiledInline, use something like the following code:

  from tiledinline.admin import TiledInline
  # ...
  class MyModelInline(TiledInline):
      model = MyModel
	  
	  # `tiled_by_default` is implicitly True by default.
	  tiled_by_default = True