var j = 1;
var x = 2 ;
$('#plus').click(function(){
    for (var i=0; i<2; i++) {
        var form = $('#a').clone() ;
        form.attr({'id':j+''+i}) ;
        form.find('select').attr({'id': 'cuenta'+(x), 'name' : 'cuenta'+(x)}) ;
        form.find('input').attr({'id' : 'monto'+(x), 'name' : 'monto'+(x)})
        $('#'+i+'-cuenta').append(form) ;
        x++ ;
        }
    j++ ;
    $('#for').attr({"value" : j}) ;
}) ;

$('#less').click(function(){
    for (var i=0; i<2; i++) {
        $('#'+j+''+i).removeClass('fila') ;
        $('#'+j+''+i).addClass('fila-remove') ;
    }
    j-- ;
    $('#for').attr({"value" : j}) ;
}) ;

//$('#form2').clone().appendTo('#'+i+'-cuenta') ;
//var elem = document.createElement('div') ;
//        elem.id = 'fila'+j+''+i ;
//        elem.className = 'fila' ;
//        var select = $('#form2').clone() ;
//        select.id = 'cuenta'+j ;
//        $('#'+i+'-cuenta').append(elem) ;
