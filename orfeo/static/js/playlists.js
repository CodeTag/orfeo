$('.list-add').on('click', function(event){
  event.preventDefault();
  var that = $(this);
  $.ajax({type:'POST', url:'playlist/addSong', data:$(this).data()}).done(function(response, result){
    if(result==='success'){
      that.addClass('list-group-item-success');
    }
  });
});
