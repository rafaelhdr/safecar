$(window).load(function(e) {
	//url, interval, init callback, periodic callback
	$Map('#map').getJSON('/api/car/set-location', 1000, function() {
		this.center();
		this.setZoom(14);
	});
});