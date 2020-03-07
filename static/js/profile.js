 $(document).ready(function(){
        $('#upload-img-btn').click(function(){
            $('#upload-img').click();
        });

        // ①为input设定change事件
        $('#upload-img').change(function () {
        //    ②如果value不为空，调用文件加载方法
            if($(this).val() != ""){
                fileLoad(this);
            }
        })

    });

    function change_password() {
        var password = $("#password").val()
        $.post("{% url 'user_profile:reset-password' %}",{"password":password,"csrfmiddlewaretoken":"{{ csrf_token }}"},function(result){
            alert("修改成功");
          });

    }

    function fileLoad(ele){
          //④创建一个formData对象
        var formData = new FormData();
        //⑤获取传入元素的val
        var name = $(ele).val();
          //⑥获取files
        var files = $(ele)[0].files[0];
        //⑦将name 和 files 添加到formData中，键值对形式
        formData.append("file", files);
        formData.append("name", name);
        formData.append("csrfmiddlewaretoken", "{{ csrf_token }}");
        $.ajax({
            url: "{% url 'user_profile:change-avatar' %}",
            type: 'POST',
            data: formData,
            processData: false,// ⑧告诉jQuery不要去处理发送的数据
            contentType: false, // ⑨告诉jQuery不要去设置Content-Type请求头
            beforeSend: function () {
               //⑩发送之前的动作
                //alert("我还没开始发送呢");
            },
            success: function (responseStr) {
               //11成功后的动作
               $("#avatar").attr("src", JSON.parse(responseStr)['avatar'] + "?a"+Date());
               alert("修改成功");
            }
            ,
            error : function (responseStr) {
                //12出错后的动作
                alert("出错啦");
            }
        });
    }