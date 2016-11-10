import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic.action.get as lastresort

def get_packages():
    packages = toolkit.get_action('current_package_list_with_resources')(data_dict={'limit':10000})
#    packages = toolkit.get_action('current_package_list_with_resources')(context={'limit':1000, 'offset':1000},data_dict={'sort':'package_count desc','all_fields':True})
    return packages

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
