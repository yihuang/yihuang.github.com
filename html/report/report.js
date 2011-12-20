function findsection(n) {
    var p = n.parents('p.MsoNormal').eq(0);
    if( n.parents('table').length>0 ) {
        p = n.parents('table').eq(0).prev();
    }
    while(! /^\d+/.test(p.text())) {
        p = p.prev();
    }
    return p;
}

var marker = '¡õ';
var options = {};
var sectionid = {};
var sectioncounter = 0;
var votemap = {};

function sum(o) {
    var s = 0;
    $.each(o, function(k, v) {
        s += v;
    });
    return s;
}

function dump() {
    var buf = [];
    $.each(votemap, function(sec, m) {
        var s = sum(m);
        buf.push($('#'+sec).text().replace('\n', ' ')+'<br/>');
        buf.push('<ul>');
        $.each(m, function(no, n) {
            var p = (n*100/s).toFixed(1);
            buf.push('<li>(' + p +'%' + ') ' + $('#'+sec+'-'+no).text()+'</li>' );
        });
        buf.push('</ul>');
    });
    $('#result').html('<p>'+buf.join('')+'</p>');
}

$(function(){
    $('body').append('<div id="result"></div>');
    var texts = $('span').contents().filter(function(){return this.nodeType==Node.TEXT_NODE;});
    texts.each(function(){
        var parts = $(this).text().split(marker);
        var newContent = [parts[0]];
        if( parts.length>1 ) {
            var section = findsection($(this))[0];
            var title = $(section).text();
            var id = sectionid[title];
            if( ! id ) {
                var id = 'section' + sectioncounter;
                section.id = id;
                sectionid[title] = id;
                options[id] = 0;
                sectioncounter += 1;
            }
            $.each(parts.slice(1), function(idx){
                newContent.push('<span id="'+id+'-'+options[id]+'" data-section="'+id+'" title="0/0" class="option">'+marker+this+'</span>') ;
                options[id] += 1;
            });
        }
        $(this).replaceWith(newContent.join(''));
    });
    var votes = 0;
    $('span.option').hover(function(){
        $(this).css('border', '1px solid red');
    }, function(){
        $(this).css('border', '1px solid transparent');
    }).click(function(){
        var no = this.id.split('-')[1];
        var section = $(this).data('section');
        var m = votemap[section];
        if(!m) {
            votemap[section] = {};
            m = votemap[section];
        }
        if( no in m ) {
            m[no] += 1;
        }
        else {
            m[no] = 1;
        }
        dump();
    });
});
