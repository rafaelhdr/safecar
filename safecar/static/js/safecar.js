$(document).ready(function(){
    $('.mark-status').click(function(){
        var data = {}
        data['action'] = $(this).attr('data-action');
        $.post("/api/car/mark-status", data)
        .done(function(response){
            window.location.reload();
        })
        .fail(function() {
            alert( "Houve alguma falha no sistema. Por favor, tente novamente. Se o erro persistir, por favor, entre em contato." );
        });
    });
});