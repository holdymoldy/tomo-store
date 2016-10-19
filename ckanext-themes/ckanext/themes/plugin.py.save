import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def get_packages():
    return toolkit.get_action('current_package_list_with_resources')(data_dict={'all_fields':True})

class ThemesPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    plugins.implements(plugins.ITemplateHelpers)    

    # IConfigurer

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'themes')
    
    def get_helpers(self):
	return {'packages':get_packages}
