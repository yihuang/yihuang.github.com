$(function() {
    var btneffect = $('<a href="#" class="apply-effects">toggle effects</a>').click(function() {
        $(this).parent().toggleClass('highlight effects');
        return false;
    })
    .appendTo($('.highlight'));
});
