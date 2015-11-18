var j = 0 ;
$('#plus').click(function(){
    for (var i=0; i<2; i++) {
        var elem = document.createElement('div') ;
        elem.id = 'fila'+j+''+i ;
        elem.className = 'fila' ;
        elem.innerHTML = '<select name="" id=""><option value="">Seleccionar cuenta</option></select>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text">' ;
        $('#'+i+'-cuenta').append(elem) ;
        }
    j++ ;
}) ;

$('#less').click(function(){
    for (var i=0; i<2; i++) {
        $('#fila'+j+''+i).removeClass('fila') ;
        $('#fila'+j+''+i).addClass('fila-remove') ;
    }
    j-- ;
}) ;

