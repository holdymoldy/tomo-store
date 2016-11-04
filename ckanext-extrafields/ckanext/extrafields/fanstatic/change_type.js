"use strict"

ckan.module('change_type', function ($, _) {
  return {
    initialize: function() {
      $.proxyAll(this, /_on/);
      this.el.on('click', this._onClick);
      }

     _onClick: function      

      var test = "hello";
      document.getElementById('output').value = test;
    }

  }


}

//function func(type){
  //  var test = "hello";
  //  var pass = "goodbye";
  //  if (type == "raw") {
  //      document.getElementById("output").value = test;
  //  }
  //  else {
  //      document.getElementById("output").value = pass;
  //  }

    //var value = sel.options[sel.selectedIndex];
    //val display = opt.text;
    //document.getElementById('output').value = display;
//}

//function func(){
  //  var test = "hello";
  //  document.getElementById('output').value = test;
//}

