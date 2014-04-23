$(document).ready(function(){
	// Navbar menu JS
	$('.js-draggable').udraggable();
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

	$('.add-board-detail').show()
	$('.add-board').hide()
	$('.js-new-board').click(function(e){
		console.log("clicked")
		e.stopPropagation();
		$('.add-board').show()
		$('.add-entry').hide()
	})

	$('.js-stop-propagation').click(function(e){
		e.stopPropagation();
	})

	$('.js-open-header-menu').on('hidden.bs.dropdown', function () {
  		$('.add-board').hide()
		$('.add-entry').show()
	})

	var width = $(window).width(); 
	var height = $(window).height();
	var show_side_bar = false;
	var list_count = $('.list-board').length
	var lastScrollLeft = 0;
	$('.js-auto-resize-to-full-window').css({
		width:width,
		height:height
	})

	$('.side-bar').css({
		left: width
	})

	$('.js-resize-overflow').css({
		width: 270*list_count,
	})
	$('.side-bar').hide()
	$('.js-show-side-bar').click(function(e){
		console.log("clicked")
		show_side_bar = true
		$('.side-bar').show()
		$('.side-bar').animate({
			left:"-=246px"
		}, 200)
	})

	$('.js-close-side-bar').click(function(e){
		console.log("clicked")
		show_side_bar = false
		$('.side-bar').animate({
			left:"+=246px"
		}, 200)
		$('.side-bar').hide()
	})

	$(document).on("click",'.js-list-cards-add', function(e){
		console.log('clicked')
		var div_list_cards = $(this).parent().parent()
		$('.list-cards-add-form').hide()
		$('.js-list-cards-add').show()
		div_list_cards.find('.list-cards-add-form').show()
		div_list_cards.find('.js-list-cards-add').hide()
	})

	$('.list-cards-add-form').hide()
	$(document).on('click', '.list-cards-add-form .close', function(e){
		console.log("clicked")
		$('.list-cards-add-form').hide()
		$('.js-list-cards-add').show()
	})
	// Responsive Boards JS
	function resizeBoardPanel(e) {
		var new_width = $(window).width(); 
		var new_height = $(window).height();
		if (new_width < 750) {
			$('.board-group-list').children().width('75%')
		} else {
			$('.board-group-list').children().width('0%')
		}

		$('.js-auto-resize-to-full-window').css({
			width:new_width,
			height:new_height
		})
		if (show_side_bar) {
			$('.side-bar').css({
				left:new_width-246
			})
		}else{
			$('.side-bar').css({
				left:new_width
			})
		}
	}
	$(window).on("resize", resizeBoardPanel);
	$('.list-list-add-form').hide()
	$('.js-add-new-list').click(function(e){
		console.log("clicked")
		$(this).hide()
		$('.list-list-add-form').show()
	})
	$('.list-cards-add-form-control.close').click(function(e){
		console.log("clicked")
		$('.js-add-new-list').show()
		$('.list-list-add-form').hide()
	})
	$("form[name='edit-card-desc']").hide()
	$(document).on('click', '.js-show-edit-card-desc-form', function(e){
		console.log("clicked")
		$("form[name='edit-card-desc']").show()
		$('.card-description').hide()
	})
	$('.edit-card-desc-form-control > .close').click(function(e){
		console.log("clicked")
		$("form[name='edit-card-desc']").hide()
		$('.card-description').show()
	})
	$('.modal').on('hidden.bs.modal', function (e) {
  		$("form[name='edit-card-desc']").hide()
		$('.card-description').show()
		$(".edit-card-comment-form-control").hide()
		$(".js-card-comment-expand").animate({
			height:36
		}, 30)
	})
	$(".edit-card-comment-form-control").hide()
	$(".js-card-comment-expand").height(20)
	$(document).on('click', '.js-card-comment-expand', function(e){
		e.stopPropagation();
				$(".edit-card-comment-form-control").show()
		if($(this).height()<50){
			$(this).animate({
				height:"+=50px"
			}, 30)
		}

	})
	$(document).on('click', '.edit-card-comment-form-control > .close', function(e){
		e.stopPropagation();
		console.log("clicked")
		console.log($(".js-card-comment-expand").height())
		$(".edit-card-comment-form-control").hide()
		$(".js-card-comment-expand").animate({
			height:36
		}, 30)

	})
})
