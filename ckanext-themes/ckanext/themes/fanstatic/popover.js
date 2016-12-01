"use strict";

ckan.module('popover', function ($, _) {
  return {
    initialize: function() {
      var img = '<img src="url"/>';
      var url = img.replace("url",this.options.contents);
      this.el.popover({html: true,
   //   title: url,
      content: url,
      placement: 'right',
      trigger: 'hover'});
    }
  };
});
