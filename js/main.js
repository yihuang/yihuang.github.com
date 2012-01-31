$(function() {
    var p = $('#content').position();
    $('#sidebar')
        .css('position', 'absolute')
        .css('left', p.left-$('#sidebar').width()-20)
        .css('top', p.top)
    var btneffect = $('<a href="#" class="apply-effects">toggle effects</a>').click(function() {
        $(this).parent().toggleClass('highlight effects');
        return false;
    })
    .appendTo($('.highlight'));
});
