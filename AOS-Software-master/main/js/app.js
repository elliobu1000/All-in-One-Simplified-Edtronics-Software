// activate the button on click 
$(".menu-button").click(function (){
	$('.menu-button').removeClass('active');
	var $this = $(this);
	if (!$this.hasClass('active')) {
		$this.addClass('active');
	}
})