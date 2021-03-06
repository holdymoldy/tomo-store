import ckan.plugins as p
import ckan.plugins.toolkit as tk


class ExtrafieldsPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)

    def _modify_package_schema(self, schema):
	schema.update({'image_display_url': [tk.get_validator('ignore_missing'),\
				tk.get_converter('convert_to_extras')]})
	schema.update({'facility': [tk.get_validator('ignore_missing'),\
				tk.get_converter('convert_to_extras')]})
	schema.update({'beamline': [tk.get_validator('ignore_missing'),\
				tk.get_converter('convert_to_extras')]})
	schema.update({'owner': [tk.get_validator('ignore_missing'),\
				tk.get_converter('convert_to_extras')]})
	schema.update({'collector': [tk.get_validator('ignore_missing'),\
				tk.get_converter('convert_to_extras')]})
	schema['resources'].update({'name':[tk.get_validator('ignore_missing')],
				'recon_alg':[tk.get_validator('ignore_missing')],
				'person':[tk.get_validator('ignore_missing')],
				'hardware':[tk.get_validator('ignore_missing')]})	

	return schema

    def create_package_schema(self):
	schema = super(ExtrafieldsPlugin,self).create_package_schema()
	schema = self._modify_package_schema(schema)
	return schema
   
    def update_package_schema(self):
	schema = super(ExtrafieldsPlugin,self).update_package_schema()
	schema = self._modify_package_schema(schema)
	return schema

    def show_package_schema(self):
	schema = super(ExtrafieldsPlugin,self).show_package_schema()
        schema.update({'image_display_url': [tk.get_converter('convert_from_extras'),\
					tk.get_validator('ignore_missing')]})
	schema.update({'facility': [tk.get_converter('convert_from_extras'),\
				    tk.get_validator('ignore_missing')]})
	schema.update({'beamline': [tk.get_converter('convert_from_extras'),\
				    tk.get_validator('ignore_missing')]})
	schema.update({'owner': [tk.get_converter('convert_from_extras'),\
				    tk.get_validator('ignore_missing')]})
	schema.update({'collector': [tk.get_converter('convert_from_extras'),\
				    tk.get_validator('ignore_missing')]})
	schema['resources'].update({'name':[tk.get_validator('ignore_missing')],
				'recon_alg':[tk.get_validator('ignore_missing')],
				'person':[tk.get_validator('ignore_missing')],
				'hardware':[tk.get_validator('ignore_missing')]})	

	return schema

    def is_fallback(self):
	return True

    def package_types(self):
	return []

    def update_config(self, config):
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
        tk.add_resource('fanstatic', 'extrafields')
