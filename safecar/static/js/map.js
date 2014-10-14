	document.write('<script src="https://maps.googleapis.com/maps/api/js?v=3.exp"></script>');
	
	function Map(selector) {
		this.element		=	$(selector)[0];
			
		this.init			=	function(lat, lng, zoom) {	
			var position	=	this.latLng(lat, lng);
				
			this.map		=	new google.maps.Map(this.element, 
									{
										zoom:	zoom,
										center:	position
									}
								);
							
			return this;
		}
		this.locate			=	function(lat, lng, zoom) {
			var position	=	this.latLng(lat, lng);
			
			if (this.marker)
				this.marker.setPosition(position);
			else {
				this.marker		=	new google.maps.Marker(
										{
											position:	position,
											map:		this.map,
											title:		'Carro',
											animation:	google.maps.Animation.DROP	
										});
			}
			
			this.map.setCenter(position);
			
			this.zoom(zoom);
			
			return this;
		}
		this.latLng			=	function(lat, lng) {
			return new google.maps.LatLng(lat, lng);
		}
		this.zoom			=	function(zoom) {
			if (zoom !== undefined)
				this.map.setZoom(zoom);
		}
		
		this.init(-23.557, -46.73, 11);
	}
	function $Map(selector) {
		return new Map(selector);
	}
