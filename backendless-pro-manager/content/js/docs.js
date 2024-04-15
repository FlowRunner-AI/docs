 // Handle code tabs

this.Tabs = (function() {
  Tabs.prototype.navTabs = null;
  Tabs.prototype.panels = null;
  function Tabs(elem) {
    this.navTabs = elem.getElementsByTagName( "li" );// getElementsByClassName('nav-item');
    this.panels = [];

    for( var i = 0; i < this.navTabs.length; i++ ) {
       var linkId = this.navTabs[ i ].children[ 0 ].getAttribute( "href" );

       if( linkId.lastIndexOf("#", 0) === 0 )
           linkId = linkId.substring( 1 );

       this.panels.push( document.getElementById( linkId ) );

    }
   // this.panels = elem.getElementsByClassName('tab-pane');
    this.bind();
  };
  Tabs.prototype.show = function(index) {
    var activePanel, activeTab;
    for (var i = 0, l = this.navTabs.length; i < l; i++) {
      this.navTabs[i].classList.remove('active');
    }
    activeTab = this.navTabs[index];
    activeTab.classList.add('active');
    for (var i = 0, l = this.panels.length; i < l; i++) {
      this.panels[i].classList.remove('active');
    }
    activePanel = this.panels[index];
    return activePanel.classList.add('active');
  };
  Tabs.prototype.bind = function() {
    var _this = this;
    for (var i = 0, l = this.navTabs.length; i < l; i++) {
      (function(elem, index) {
        elem.addEventListener('click', function(evt) {
          evt.preventDefault();
          return _this.show(index);
        });
      })(this.navTabs[i], i);
    }
  };
  return Tabs;
})();

document.addEventListener('DOMContentLoaded', function() {
  var nodes = document.getElementsByClassName('nav-tabs');
  for (var i = 0, l = nodes.length; i < l; i++) {
    new Tabs(nodes[i]);
  }

    var docsSelector = document.getElementById('docselector')
  docsSelector.value = document.location.pathname.split('/')[2]

  docsSelector.addEventListener('change', function(event) {
    var pathEntries = location.pathname.split('/')
    pathEntries[2] = event.target.value
    location.pathname = pathEntries.join('/')
  })

    var tour = new Tour({
       steps: [
         {
           element: "#docselector",
           title: "Documentation Selector",
           content: "Use this selector to switch between different Backendless documentation sets, this includes docs for Android, iOS, JS, .NET, Business Logic, Codeless, etc.",
           backdrop: true,
           placement: "auto"
         },
         {
           element: ".md-search__form",
           title: "Search the Docs!",
           content: "Backendless documentation is indexed so you can quickly find what you're looking for.",
           backdrop: true,
           placement: "auto"
         },
       ]});

    // Initialize the tour
     tour.init();

    // Start the tour
     tour.start();
});    

jQuery(document).ready(function($){

  $(document).on('click','.menu-item-has-children', function()
  {
      $(this).toggleClass('active');
  });

  $(document).on('click','.header__burger', function()
  {
      $('body').toggleClass('show-menu');
      $('#menu-header-menu').toggleClass('container');
  });

  $(window).on('hashchange', function(){
      if($('body').hasClass('show-menu'))
      {
          $('.header__burger').trigger('click');
      }
  });

});