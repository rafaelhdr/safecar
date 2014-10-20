	document.write('<script src="https://maps.googleapis.com/maps/api/js?v=3.exp"></script>');
	
	function Map(selector) {
		this.element		=	$(selector)[0];
			
		this.center			=	function() {
			this.map.setCenter(Map.latLng(this.lat, this.lng));
			
			return this;
		}
		this.init			=	function(lat, lng, zoom) {
			var position	=	Map.latLng(lat, lng);
			
			this.setLatLng(lat, lng, false);
			this.setZoom(zoom, false);
				
			this.map		=	new google.maps.Map(this.element, 
									{
										zoom:	zoom,
										center:	position
									}
								);
							
			return this;
		}
		this.locate			=	function(lat, lng, zoom) {
			this.setLatLng(lat, lng, true);
			this.zoom(zoom, true);
			
			return this;
		}
		this.setLat			=	function(lat, update) {
			this.lat		=	1 * lat;
			
			if (update || update === undefined)
				this.updateLatLng();
		}
		this.setLatLng		=	function(lat, lng, update) {
			this.setLat(lat, false);
			this.setLng(lng, false);
			
			if (update || update === undefined)
				this.updateLatLng();
		}
		this.setLng			=	function(lng, update) {
			this.lng		=	1 * lng;
			
			if (update || update === undefined)
				this.updateLatLng();
		}
		this.setZoom		=	function(zoom, update) {
			this.z			=	1 * zoom;
			
			if (update || update === undefined)
				this.updateZoom();
		}
		this.updateLatLng	=	function() {
			var position	=	Map.latLng(this.lat, this.lng);
			
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
		}
		this.updateZoom		=	function() {
			this.map.setZoom(this.z);
		}
		this.zoom			=	function(zoom) {
			if (zoom !== undefined)
				this.setZoom(zoom, true);
			
			return this;
		}
		
		//this.init(-23.557, -46.73, 11);
		this.init(0, 0, 1);
	}
	Map.latLng				=	function(lat, lng) {
		return new google.maps.LatLng(lat, lng);
	}
	function $Map(selector) {
		return new Map(selector);
	}