

var j = 1 ;
$('#plus').click(function(){
    for (var i=0; i<2; i++) {
        var elem = document.createElement('div') ;
        elem.id = 'fila'+j+''+i ;
        elem.className = 'fila' ;
        elem.innerHTML = '<select name="" id=""><option value="">Seleccionar cuenta</option></select>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text">' ;
        $('#'+i+'-cuenta').append(elem) ;
        }
    j++ ;
    $('#for').attr({"value" : j}) ;
}) ;

$('#less').click(function(){
    for (var i=0; i<2; i++) {
        var x = j-1 ;
        $('#fila'+x+''+i).removeClass('fila') ;
        $('#fila'+x+''+i).addClass('fila-remove') ;
    }
    j-- ;
    $('#for').attr({"value" : j}) ;
}) ;

function obtenerEmpleado(id) {
        $('#nombre').attr({'value' : $('#'+id).find('#nombres').text()}) ;
        $('#horasExtras').attr({'value': $('#'+id).find('#he').text()}) ;
        $('#codigo').attr({'value' : id}) ;
        $('#'+id).addClass('mostrar') ;
}

//$('#form2').clone().appendTo('#'+i+'-cuenta') ;