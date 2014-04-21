$(document).ready(function(){
	// Navbar menu JS
	$('.js-open-header-menu').on('show.bs.dropdown', function () {
		var overhead = $(document).width(); 
		/* fix the 1px off bug */
		if($(this).hasClass("header-user-add")){
			overhead = overhead + 1
		}

		$('.header-dropdown-menu').css({
			width: 285,
			left: overhead-288
		})
	})

	$('.js-new-board').click(function(e){
		console.log("clicked")
		e.stopPropagation();
		$('.add-board-detail').show()
		$('.add-entry').hide()
	})

	$('.js-stop-propagation').click(function(e){
		e.stopPropagation();
	})

	$('.js-new-group').click(function(e){
		console.log("clicked")
		e.stopPropagation();
		$('.add-group-detail').show()
		$('.add-entry').hide()
	})

	$('.js-open-header-menu').on('hidden.bs.dropdown', function () {
  		$('.add-board-detail').hide()
		$('.add-entry').show()
		$('.add-group-detail').hide()
	})

	// Responsive Boards JS
	function resizeBoardPanel(e) {
		var width = $(window).width()
		console.log(width)
		console.log($('.container-fluid').width())
		if (width < 750) {
			console.log($('.board-group-list'))
			$('.board-group-list').children().width('75%')
		} else {
			$('.board-group-list').children().width('0%')
		}
	}
	$(window).on("resize", resizeBoardPanel);
})
