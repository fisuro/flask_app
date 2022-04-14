$(document).ready(function() {    
    $('#subbutton').click(function(){
        $("#customers tbody").empty();
        $.ajax({
            type: 'GET',
            url : '/users',
            success: function(data){
                for(var i in data){
                    var markup = "<tr><td>" + data[i].id + "</td><td>" + data[i].name + "</td><td>" + data[i].surname + "</td><td>" + data[i].email +"</td><td> <button type='button' class='edit' id='edit" + data[i].id + "' name='edituj'>Edit</button> <button  type='button' class='delete' id='delete" + data[i].id + "' name='obrisi'>Delete</button></td></tr>";
                    $("#customers tbody").append(markup);    
                } 
                $(".delete").click(function(){
                    var buttonID = this.id;
                    var ret = buttonID.replace('delete', '');
                    function confirmAction() {
                        let confirmAction = confirm("Are you sure that you want to delete this user?");
                        if (confirmAction) {
                          alert("User is successfully deleted");
                          $.ajax({
                            type: 'DELETE',
                            url : '/users/'+ret,
                            success: function(request, message){
                                $('#subbutton').click();
                                }
                            })
                        } else {
                          alert("Action canceled");
                        }
                      }
                    confirmAction()
                    })

                $(".edit").click(function(){
                    var buttonID = this.id;
                    var ret = buttonID.replace('edit', '');
                    window.location.href = "/users/" + ret;
                })
            }
        })
    })
    $("#edituser").click(function(){
        var kita = {
            name : $('#fname').val(),
            surname: $('#lname').val()
        }
        function confirmAction() {
            $.ajax({
                type: 'PUT',
                url : window.location.pathname,
                dataType: 'json',
                contentType: 'application/json',
                data: JSON.stringify(kita),
                success: function(request, message){
                    alert(message)
                    window.location.href = "/";    
                }
            })
        }
        confirmAction();
    })


    $('#clearbtn').click(function(){
        $('#fname').val('');
        $('#lname').val('');
        $('#email').val('');
    })
    
    $('#aduser').click(function(){
        var kita = {
            name : $('#fname').val(),
            surname: $('#lname').val(),
            email: $('#email').val()
        }
        $.ajax({
            type: 'POST',
            url: '/users',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(kita),

            success: function(request, message){
                $('#subbutton').click();
                alert(message)
            },

            error: function(xhr, status, error) {
                alert(xhr.responseText)
            }
        })
    })
});