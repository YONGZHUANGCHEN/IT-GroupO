 $(document).ready(function(){
        $('#upload-img-btn').click(function(){
            $('#upload-img').click();
        });

        // Set the change event for the input
        $('#upload-img').change(function () {
        //    If the value is not empty, call the file load method
            if($(this).val() != ""){
                fileLoad(this);
            }
        })

    });

    function change_password() {
        var password = $("#password").val()
        $.post("{% url 'user_profile:reset-password' %}",{"password":password,"csrfmiddlewaretoken":"{{ csrf_token }}"},function(result){
            alert("Modify the success");
          });

    }

    function fileLoad(ele){
          //Create a formData object
        var formData = new FormData();
        //gets the val of the passed element
        var name = $(ele).val();
          //get files
        var files = $(ele)[0].files[0];
        //Name and files will be added to the formData, key-value pairs form
        formData.append("file", files);
        formData.append("name", name);
        formData.append("csrfmiddlewaretoken", "{{ csrf_token }}");
        $.ajax({
            url: "{% url 'user_profile:change-avatar' %}",
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            beforeSend: function () {

            },
            success: function (responseStr) {

               $("#avatar").attr("src", JSON.parse(responseStr)['avatar'] + "?a"+Date());
               alert("Modify the success");
            }
            ,
            error : function (responseStr) {

                alert("Error !");
            }
        });
    }