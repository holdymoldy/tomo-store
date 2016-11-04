"use strict";

ckan.module('popover', function ($, _) {
  return {
    initialize: function() {
//      var url = '<img src="http://www.legalsportsreport.com/wp-content/uploads/2015/11/Gary-Johnson-DFS-opinion.jpg"/>';
      var url=this.options.contents.split(",")[0].split("[u");
      var img='<img src=' + url + '/>';
      this.el.popover({html: true,
      title: url,
      content: img,
      placement: 'right',
      trigger: 'hover'});
    }
  };
});
