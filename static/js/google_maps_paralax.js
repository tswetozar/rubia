var map;
      function initialize() {
        var mapOptions = {
          zoom: 14,
          center: new google.maps.LatLng(52.5498783, 13.425209099999961),
          mapTypeId: google.maps.MapTypeId.ROADMAP,
          scroll:{x:$(window).scrollLeft(),y:$(window).scrollTop()}
        };
        map = new google.maps.Map(document.getElementById('map_canvas'),
            mapOptions);
        new google.maps.Marker({map:map,position:map.getCenter()});
        var offset=$(map.getDiv()).offset();
        map.panBy(((mapOptions.scroll.x-offset.left)/3),((mapOptions.scroll.y-offset.top)/3));
      google.maps.event.addDomListener(window, 'scroll', function(){
      var scrollY=$(window).scrollTop(),
          scrollX=$(window).scrollLeft(),
          scroll=map.get('scroll');
      if(scroll){
        map.panBy(-((scroll.x-scrollX)/3),-((scroll.y-scrollY)/3));
      }
      map.set('scroll',{x:scrollX,y:scrollY})

      });
      }

      google.maps.event.addDomListener(window, 'load', initialize);
