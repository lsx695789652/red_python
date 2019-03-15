layui.use(['form', 'layer', 'jquery'], function () {
    var form = layui.form,
        layer = parent.layer === undefined ? layui.layer : top.layer
    $ = layui.jquery;

    //登录按钮
    form.on("submit(login)", function (data) {
        $(this).text("登录中...").attr("disabled", "disabled").addClass("layui-disabled");
        var param = data.field;
        if (param.length < 1) {
            layer.alert('输入用户名或密码', {icon: 5});
            return false
        }
        $.ajax({
            url: "/admin/login/",
            type: 'post',
            dataType: 'json',
            data: param,
            success: function (res) {
                if (res == 200) {
                    layer.alert('登录成功！', {icon: 1});
                    setTimeout(function () {
                        window.location.href = "/admin/index/";
                    }, 1000);
                } else {
                    layer.alert('用户名或密码错误！', {icon: 5});
                    $('.layui-btn').text("登录").removeAttr("disabled", "disabled").removeClass("layui-disabled");
                }
            },
            error: function () {
                layer.alert('操作失败！！！', {icon: 5});
                $('.layui-btn').text("登录").removeAttr("disabled", "disabled").removeClass("layui-disabled");
            }
        });
        return false;
    })

    //表单输入效果
    $(".loginBody .input-item").click(function (e) {
        e.stopPropagation();
        $(this).addClass("layui-input-focus").find(".layui-input").focus();
    })
    $(".loginBody .layui-form-item .layui-input").focus(function () {
        $(this).parent().addClass("layui-input-focus");
    })
    $(".loginBody .layui-form-item .layui-input").blur(function () {
        $(this).parent().removeClass("layui-input-focus");
        if ($(this).val() != '') {
            $(this).parent().addClass("layui-input-active");
        } else {
            $(this).parent().removeClass("layui-input-active");
        }
    })
})
