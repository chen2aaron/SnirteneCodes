var contextPath = contextPath || "",
    Souche = Souche || {};
-1 != window.location.href.indexOf("souche.com") && (document.domain = "souche.com"),
    Souche.Util = function () {
        var e = {};
        return {
            mixin: function (e, t) {
                for (var a in t)e[a] = t[a]
            },
            appear: function (t, a, o, i) {
                e[t] = e[t] || [], e[t].push(a), o || (o = 0), e[t].distance = o, e[t].multi = i
            },
            init: function () {
                var t = function () {
                    var t = ($(window).width(), $(window).height()), a = $(window).scrollTop();
                    for (var o in e)if ($(o).length) {
                        {
                            var i = $(o).offset();
                            $(o).height()
                        }
                        if (i.top - a > 0 && i.top - a < t - e[o].distance) {
                            for (var n = 0; n < e[o].length; n++)e[o][n]();
                            e[o].multi || (e[o] = [])
                        }
                    }
                };
            $(document).ready(function () {
                setTimeout(function () {
                    t()
                }, 200)
            }), $(window).scroll(t)
            },
            actionList: function () {
            }
        }
    }(),
    Souche.Util.init(),
    Souche.Data = {DropdownzIndex: 1e3},
    Souche.UI = Souche.UI || {},
    Souche.UI.Select = function () {
        var e = function (e) {
            this.config = {
                eles: ["#J_buybrand", "#J_buyset", ""],
                type: "car-subdivision",
                defaultValues: []
            },
                Souche.Util.mixin(this.config, e), this.init()
        };
        return e.prototype = {
            init: function () {
                for (var e = this.config, t = 0; t < e.eles.length; t++)e.defaultValues[t] = e.defaultValues[t] || "", e.eles[t] = "#" + e.eles[t];
                $.ajax({
                    url: contextPath + "/pages/dicAction/loadRootLevel.json",
                    dataType: "json",
                    data: {type: e.type},
                    success: function (t) {
                        $(e.eles[0]).append($("<option value=''>-请选择-</option>"));
                        for (var a in t.items) {
                            var o = t.items[a];
                            $(e.eles[0]).append('<option value="' + o.code + '" ' + (e.defaultValues[0] == o.code ? "selected" : "") + ">" + o.name + "</option>")
                        }
                        e.defaultValues[0] && $(e.eles[0]).change()
                    },
                    error: function () {
                    },
                    failure: function () {
                    }
                });
                for (var t in e.eles)$(e.eles[t]).attr("data-index", t).change(function () {
                    var t = this.value;
                    if (null != t) {
                        var a = t.split("-")[0], o = 1 * $(this).attr("data-index");
                        $(Souche.UI.Select).trigger("change", {
                            id: this.id,
                            value: this.value,
                            text: this.options[this.selectedIndex].innerHTML
                        }), o >= e.eles.length - 1 || $.ajax("brand" == a ? {
                            url: contextPath + "/pages/dicAction/loadRootLevelForCar.json",
                            dataType: "json",
                            data: {type: e.type, code: t},
                            success: function (t) {
                                $(e.eles[1]).empty(), $(e.eles[1]).append($("<option value=''>-请选择-</option>"));
                                for (var a = 0; a < t.keys.length; a++) {
                                    var o = t.keys[a], i = $("<optgroup label='" + o + "' style='color:green;font-style: italic;background-color:#f5f5f5;'></optgroup>");
                                    $(e.eles[1]).append(i);
                                    for (var n = 0; n < t.codes[o].length; n++) {
                                        var s = t.codes[o][n];
                                        i.append($("<option style='background-color:#ffffff;color:#000000;font-style: normal;' value='" + s.code + "' " + (e.defaultValues[1] == s.code ? "selected" : "") + ">" + s.name + "</option>"))
                                    }
                                    $(e.eles[1]).append($(""))
                                }
                                e.defaultValues[1] && $(e.eles[1]).change()
                            }
                        } : {
                            url: contextPath + "/pages/dicAction/loadNextLevel.json",
                            dataType: "json",
                            data: {type: e.type, code: t},
                            success: function (t) {
                                $(e.eles[o + 1]).empty(), $(e.eles[o + 1]).append($("<option value=''>-请选择-</option>"));
                                for (var a in t.items) {
                                    var i = t.items[a];
                                    $(e.eles[o + 1]).append('<option value="' + i.code + '" ' + (e.defaultValues[o + 1] == i.code ? "selected" : "") + ">" + i.name + "</option>")
                                }
                                e.defaultValues[2] && $(e.eles[2]).change()
                            }
                        })
                    }
                })
            }
        }, {
            init: function (t) {
                return new e(t)
            }
        }
    }(),
    Souche.UI.NewSelect = function () {
        var e = function (e) {
            this.config = {
                eles: ["#J_buybrand", "#J_buyset", ""],
                type: "car-subdivision",
                defaultValues: []
            },
                Souche.Util.mixin(this.config, e), this.init()
        };
        return e.prototype = {
            init: function () {
                for (var e = this.config, t = 0; t < e.eles.length; t++)e.defaultValues[t] = e.defaultValues[t] || "", e.eles[t] = "#" + e.eles[t];
                if ("car-subdivision" == e.type || "area" == e.type) {
                    $.ajax({
                        url: contextPath + "/pages/dicAction/loadRootLevel.json",
                        dataType: "json",
                        data: {type: e.type},
                        success: function (t) {
                            if ($(".choose-box", e.eles[0]).html(""), "car-subdivision" == e.type) {
                                var a = {};
                                $(".brand-cata").html("");
                                for (var o in t.items) {
                                    var i = t.items[o].name.split(" ")[0],
                                        n = t.items[o].name.split(" ")[1];
                                    t.items[o].name = n, a[i] ? a[i].push(t.items[o]) : a[i] = [t.items[o]]
                                }
                                for (var o in a) {
                                    $(".brand-cata").append("<li><a>" + o + "</a></li>"),
                                        $(".choose-box", e.eles[0]).append("<div class=cont-tit data-name='" + o + "'>" + o + "</div>");
                                    for (var s in a[o]) {
                                        var c = a[o][s],
                                            l = $('<div class="choose-cont" data-code="' + c.code + '" data-name="' + c.name + '">' + c.name + "</option>");
                                        $(".choose-box", e.eles[0]).append(l),
                                            l.on("click", function (t) {
                                                e.eles.length > 2 && $(".choose-box", e.eles[2]).html('<div class="cont-default" data-code="" data-name="">请先选择车系</div>'),
                                                    t.stopPropagation(),
                                                    $(e.eles[0]).attr({
                                                        "data-code": $(this).attr("data-code"),
                                                        "data-name": $(this).attr("data-name")
                                                    }), $(e.eles[0]).trigger("change", {
                                                    code: $(this).attr("data-code"),
                                                    name: $(this).attr("data-name")
                                                }), $(".choose-cont", $(this).closest(".open-item")).removeClass("active"), $(this).addClass("active")
                                            }), e.defaultValues[0] && e.defaultValues[0] == c.code && l.trigger("click")
                                    }
                                }
                                $(".brand-cata a").on("click", function () {
                                    var e = $(this).html(), t = $("#choose-brand .choose-box .cont-tit[data-name=" + e.toUpperCase() + "]");
                                    t.length && t.parent().animate({scrollTop: t.parent().scrollTop() + (t.offset().top - t.parent().offset().top)})
                                })
                            } else for (var o in t.items) {
                                var c = t.items[o], l = $('<div class="choose-cont" data-code="' + c.code + '" data-name="' + c.name + '">' + c.name + "</option>");
                                $(".choose-box", e.eles[0]).append(l), l.on("click", function (t) {
                                    t.stopPropagation(), $(e.eles[0]).attr({
                                        "data-code": $(this).attr("data-code"),
                                        "data-name": $(this).attr("data-name")
                                    }), $(e.eles[0]).trigger("change", {
                                        code: $(this).attr("data-code"),
                                        name: $(this).attr("data-name")
                                    }), $(".choose-cont", $(this).closest(".open-item")).removeClass("active"), $(this).addClass("active")
                                }), e.defaultValues[0] && e.defaultValues[0] == c.code && l.trigger("click")
                            }
                        },
                        error: function () {
                        },
                        failure: function () {
                        }
                    });
                    for (var t in e.eles) $(e.eles[t]).attr("data-index", t).change(function (t, a) {
                        var o = a.code;
                        if (null != o) {
                            var i = o.split("-")[0],
                                n = 1 * $(this).attr("data-index");
                            return $(".choose-result", $(this)).val(a.code),
                                $(".choose-result-name", $(this)).val(a.name),
                                $(Souche.UI.NewSelect).trigger("change", {
                                id: this.id,
                                code: a.code,
                                name: a.name
                            }),
                                n >= e.eles.length - 1
                                    ? ($(e.eles[0]).closest(".select-open").addClass("hidden"),
                                        void $(".display-text", $(e.eles[0]).closest(".select-item")).html(function () {
                                            for (var t = [], a = 0; a < e.eles.length; a++)t.push($(e.eles[a]).attr("data-name"));
                                            return t.join(" ")
                                        }))
                                    : void
                                    $.ajax("brand" == i ? {
                                url: contextPath + "/pages/dicAction/loadRootLevelForCar.json",
                                dataType: "json",
                                data: {type: e.type, code: o},
                                success: function (t) {
                                    $(".choose-box", e.eles[1]).html("");
                                    for (var a = 0; a < t.keys.length; a++) {
                                        var o = t.keys[a];
                                        $(".choose-box", e.eles[1]).append("<div class=cont-tit>" + o + "</div>");
                                        for (var i = 0; i < t.codes[o].length; i++) {
                                            var n = t.codes[o][i], s = $('<div class="choose-cont" data-code="' + n.code + '" data-name="' + n.name + '">' + n.name + "</option>");
                                            $(".choose-box", e.eles[1]).append(s), s.on("click", function (t) {
                                                t.stopPropagation(), $(e.eles[1]).attr({
                                                    "data-code": $(this).attr("data-code"),
                                                    "data-name": $(this).attr("data-name")
                                                }), $(e.eles[1]).trigger("change", {
                                                    code: $(this).attr("data-code"),
                                                    name: $(this).attr("data-name")
                                                }), $(".choose-cont", $(this).closest(".open-item")).removeClass("active"), $(this).addClass("active")
                                            }), e.defaultValues[1] && e.defaultValues[1] == n.code && s.trigger("click")
                                        }
                                    }
                                }
                            } : {
                                url: contextPath + "/pages/dicAction/loadNextLevel.json",
                                dataType: "json",
                                data: {type: e.type, code: o},
                                success: function (t) {
                                    if ("car-subdivision" == e.type && 1 == n) {
                                        $(".choose-box", e.eles[n + 1]).html("");
                                        var a = {};
                                        for (var o in t.items) {
                                            var i = t.items[o].name.split(" ")[0];
                                            a[i] ? a[i].push(t.items[o]) : a[i] = [t.items[o]]
                                        }
                                        for (var o in a) {
                                            $(".choose-box", e.eles[n + 1]).append("<div class=cont-tit data-name='" + o + "'>" + o + "</div>");
                                            for (var s in a[o]) {
                                                var c = a[o][s], l = $('<div class="choose-cont" data-code="' + c.code + '" data-name="' + c.name + '">' + c.name + "</option>");
                                                $(".choose-box", e.eles[n + 1]).append(l), l.on("click", function (t) {
                                                    t.stopPropagation(), $(e.eles[n + 1]).attr({
                                                        "data-code": $(this).attr("data-code"),
                                                        "data-name": $(this).attr("data-name")
                                                    }), $(e.eles[n + 1]).trigger("change", {
                                                        code: $(this).attr("data-code"),
                                                        name: $(this).attr("data-name")
                                                    }), $(".choose-cont", $(this).closest(".open-item")).removeClass("active"), $(this).addClass("active")
                                                }), e.defaultValues[n + 1] && e.defaultValues[n + 1] == c.code && l.trigger("click")
                                            }
                                        }
                                    } else {
                                        $(".choose-box", e.eles[n + 1]).html("");
                                        for (var o in t.items) {
                                            var c = t.items[o], l = $('<div class="choose-cont" data-code="' + c.code + '" data-name="' + c.name + '">' + c.name + "</option>");
                                            $(".choose-box", e.eles[n + 1]).append(l), l.on("click", function (t) {
                                                t.stopPropagation(), $(e.eles[n + 1]).attr({
                                                    "data-code": $(this).attr("data-code"),
                                                    "data-name": $(this).attr("data-name")
                                                }), $(e.eles[n + 1]).trigger("change", {
                                                    code: $(this).attr("data-code"),
                                                    name: $(this).attr("data-name")
                                                }), $(".choose-cont", $(this).closest(".open-item")).removeClass("active"), $(this).addClass("active")
                                            }), e.defaultValues[n + 1] && e.defaultValues[n + 1] == c.code && l.trigger("click")
                                        }
                                    }
                                }
                            })
                        }
                    })
                } else {
                    $(".choose-cont").on("click", function (t) {
                        var a = $(this).attr("data-code"), o = $(this).html(), i = $(this).closest(".open-item").attr("data-index");
                        "time" == e.type && 0 == i && ($(".cont-default", e.eles[1]).addClass("hidden"), $(".cont-item", e.eles[1]).removeClass("hidden")), $(this).closest(".open-item").attr({
                            "data-code": a,
                            "data-name": o
                        }), $(".choose-cont", $(this).closest(".open-item")).removeClass("active"), $(this).addClass("active"), i >= e.eles.length - 1 && ($(this).closest(".select-open").addClass("hidden"), $(".display-text", $(e.eles[0]).closest(".select")).html(function () {
                            for (var t = [], a = 0; a < e.eles.length; a++)t.push($(e.eles[a]).attr("data-name"));
                            return t.join(" ")
                        })), $(".choose-result", $(this).closest(".open-item")).val(a), $(".choose-result-name", $(this).closest(".open-item")).val(o), t.stopPropagation()
                    });
                    for (var t in e.eles)$(e.eles[t]).attr("data-index", t), e.defaultValues[t] && $(".choose-cont[data-code=" + e.defaultValues[t] + "]", e.eles[t]).trigger("click")
                }
            }
        }, {
            init: function (t) {
                return new e(t)
            }
        }
    }(), Souche.Form = Souche.Form || {}, Souche.Form = function () {
    jQuery.validator && (jQuery.validator.addMethod("exactlength", function (e, t, a) {
        return this.optional(t) || e.length == a
    }, jQuery.format("请输入 {0} 字符.")), jQuery.validator.addMethod("vin", function (e, t) {
        return this.optional(t) || /^[A-Z0-9]{8}[0-9X][A-Z0-9]{2}[A-Z0-9]{6}$/.test(e.toUpperCase())
    }, jQuery.format("vin编码格式错误.")));
    var e = function (e) {
        this.config = {
            ele: "loginform", isAsync: !1, beforeSubmit: function () {
                return !0
            }, validateFail: function () {
            }, success: function () {
            }, error: function () {
            }
        }, Souche.Util.mixin(this.config, e)
    };
    return e.prototype = {
        submit: function () {
            var e = this.config;
            $("#" + e.ele).validate({
                messages: e.messages || {}, submitHandler: function (t) {
                    e.beforeSubmit() && (e.isAsync ? ($("*[type='submit']").attr("disabled", !0), $.ajax({
                        url: $(t).attr("action") || "",
                        type: $(t).attr("method") || "get",
                        dataType: "json",
                        data: $(t).serialize(),
                        success: function (t) {
                            $("*[type='submit']").attr("disabled", !1), t.errorMessage ? e.error(t.errorMessage) : e.success(t)
                        },
                        error: function () {
                            $("*[type='submit']").attr("disabled", !1), e.error()
                        }
                    })) : t.submit())
                }, errorPlacement: function (t, a) {
                    e.validateFail(t.html(), a)
                }
            })
        }
    }, {
        submit: function (t) {
            new e(t).submit()
        }
    }
}(), Souche.MiniLogin = Souche.MiniLogin || {}, Souche.MiniLogin = function () {
    var e = '<div class="mem">    <div class="mem-feed">       <div class="mem-head">        <div class="mem-close" click_type="minilogin-close"></div>        <div class="mem-title">登录</div>       </div>        <form  class="mem-form" id="loginform" action="/pages/evaluateAction/isNoRegisterLoginYzm.json" method="post" >          <input type="hidden" value="ajaxUserLogin" name="j_type" />          <input type="hidden" value="0" id="login_type" />          <input type="hidden" value="1421820928828" id="time" />          <input type="hidden" value="f5523598bc99432f686396d5cc90aa9b" id="token" />          <input type="hidden" value="" name="type" id="j_type" />          <input type="hidden" value="" name="userId" id="j_userId" />        <div class="mem-error novisible input-error-tip"><span class="error-icon"></span><span class="info">您输入的密码和账户名不匹配</span></div>        <div class="mem-controller clearfix" id="J-tel-controller">          <label for="mem-tel" class="mem-label">手机号：</label>          <input type="text" name="phone" id="mem-tel" class="mem-text-input" placeholder="请输入正确的手机号"/>          <div class="input-error-tip hidden"><span class="error-icon"></span>请输入正确的手机号</div>        </div>        <div class="mem-controller clearfix" id="J-pwd-controller">          <label for="mem-password" class="mem-label">验证码：</label>                              <input type="text" id="mem-password" name="yzm" class="mem-send member-psd" value="" placeholder="请查收短信" />          <button class="send" type="button" id="get-code">获取验证码</button>                </div>        <div class="submit-controller">          <input type="submit" class="mem-button" click_type="minilogin-yzm" id="login_button"  value="登 录"  />        </div>      </form>    </div>          </div>', t = null, a = null, o = !1, i = !0, n = !0, s = !1, c = function () {
    };
    return {
        callback: function () {
            this.close(), c()
        }, resizeTo: function () {
        }, close: function () {
            $(".result_p .warning ").addClass("hidden"), t && t.css({display: "none"}), a && a && a.css({display: "none"})
        }, toReg: function (e, a) {
            $(".mem-title").html("完善信息"), $(".other-login").addClass("hidden"), t.css({height: 370}), $("#j_type").val(e), $("#j_userId").val(a), $("#loginform").attr("action", contextPath + "/pages/evaluateAction/bindThirdAccount.json")
        }, _show: function () {
            var o = this;
            if (t)t.css({
                display: "block",
                width: 400,
                height: 450,
                left: $(window).width() / 2 - 200,
                top: $(window).height() / 2 - 225
            }), a.css({display: "block"}), $(".mem-title").html("登录"), $(".other-login").removeClass("hidden"), $("#loginform").attr("action", contextPath + "/pages/evaluateAction/isNoRegisterLoginYzm.json"); else {
                t = $(e), t.css({
                    display: "block",
                    width: 400,
                    height: 450,
                    left: $(window).width() / 2 - 200,
                    top: $(window).height() / 2 - 225
                }), a = $("<div id='minilayer'></div>"), a.css({
                    display: "block",
                    width: $(document.body).width(),
                    left: 0,
                    top: 0,
                    height: $(document.body).height(),
                    position: "absolute",
                    background: "#111",
                    zIndex: 1e8
                }).css("opacity", .7), $(document.body).append(a), $(document.body).append(t), $(".social-item a", t).on("click", function (e) {
                    e.preventDefault();
                    var t = $(this).attr("href"), a = window.open(t, "", "width=800,height=500");
                    a.focus()
                }), a.on("click", function () {
                    o.close()
                }), $(".mem-title").html("登录"), $(".other-login").removeClass("hidden"), $("#loginform").attr("action", contextPath + "/pages/evaluateAction/isNoRegisterLoginYzm.json");
                var i = 60, n = function () {
                    i > 0 ? ($("#get-code").html(i + "秒后可重发").attr("disabled", !0), i -= 1, setTimeout(function () {
                        n()
                    }, 1e3)) : $("#get-code").html("发送验证码").attr("disabled", !1)
                };
                $(".mem-close").click(function () {
                    Souche.MiniLogin.close(), $(Souche.MiniLogin).trigger("manualClose")
                });
                var s = /^1[34587][0-9]{9}$/;
                $("#get-code").on("click", function () {
                    return s.test($("#mem-tel").val()) ? ($(".mem-error").addClass("novisible"), $("#mem-tel").parent().find(".input-error-tip").addClass("hidden"), i = 60, n(), void $.ajax({
                        url: contextPath + "/pages/smsCaptchaAction/send.json",
                        data: {cellphone: $("#mem-tel").val(), token: Souche_token, time: Souche_time},
                        dataType: "json",
                        success: function (e) {
                            e.code && 401 == e.code ? window.parent.window.location.href = contextPath + "/pages/valid.html" : e.error && alert(e.error)
                        }
                    })) : ($(".mem-error").removeClass("novisible"), void $(".mem-error .info").html("请输入正确的手机号"))
                }), $("#loginform").on("submit", function (e) {
                    e.preventDefault(), $(".mem-error").addClass("novisible"), $.ajax({
                        url: this.action,
                        data: $("#loginform").serialize(),
                        dataType: "json",
                        success: function (e) {
                            e.msg ? ($(".mem-error").removeClass("novisible"), $(".mem-error .info").html(e.msg)) : (Souche.MiniLogin.close(), Souche.MiniLogin.callback())
                        }
                    })
                })
            }
        }, checkLogin: function (e, t, a, l, r) {
            c = e;
            var d = this;
            o = !!t, i = !a, n = !l, s = !!r, n ? o && i ? Souche.checkVerifyAndThirdLogin(function (e) {
                e ? d.callback && d.callback() : d._show()
            }) : o ? $.ajax({
                url: contextPath + "/pages/evaluateAction/isPhoneVerifyLogin.json",
                type: "post",
                dataType: "json",
                success: function (e) {
                    "true" == e.result ? d.callback && d.callback() : d._show()
                },
                error: function () {
                    d._show()
                }
            }) : i ? Souche.checkAllLogin(function (e) {
                e ? d.callback && d.callback() : d._show()
            }) : Souche.checkPhoneExist(function (e) {
                e ? d.callback && d.callback() : d._show()
            }) : d._show()
        }
    }
}(), Souche.checkVerifyAndThirdLogin = function (e) {
    $.ajax({
        url: contextPath + "/pages/evaluateAction/isVerifyAndThirdLogin.json",
        type: "post",
        dataType: "json",
        success: function (t) {
            e("true" == t.result ? !0 : !1)
        },
        error: function () {
            e(!1)
        }
    })
}, Souche.checkAllLogin = function (e) {
    $.ajax({
        url: contextPath + "/pages/evaluateAction/isLogin.json",
        type: "post",
        dataType: "json",
        success: function (t) {
            e("true" == t.result ? !0 : !1)
        },
        error: function () {
            e(!1)
        }
    })
}, Souche.checkPhoneExist = function (e) {
    $.ajax({
        url: contextPath + "/pages/evaluateAction/isPhoneLogin.json",
        type: "post",
        dataType: "json",
        success: function (t) {
            e("true" == t.result ? !0 : !1)
        },
        error: function () {
            e(!1)
        }
    })
}, Souche.PhoneRegister = function (e, t) {
    $.ajax({
        url: contextPath + "/pages/evaluateAction/noRegisterLogin.json",
        type: "post",
        dataType: "json",
        data: {phone: e},
        success: function (e) {
            t(e.errorMessage ? !1 : !0)
        },
        error: function () {
            t(!1)
        }
    })
}, Souche.AjaxManager = function () {
    var e = {}, t = function () {
        arguments[2];
        delete this.context.ajaxList[this.identify][this.option.url]
    }, a = function (e, a) {
        var o = this.predicate.call(e);
        if (e.context = {context: this, identify: o, option: e}, this.ajaxList[o]) {
            var i = this.ajaxList[o].lastTime, n = +new Date;
            if (n - i > this.delayTime) {
                window.clearTimeout(this.ajaxList[o].handle), this.ajaxList[o].lastTime = +new Date, this.ajaxList[o][e.url] && this.aborted && this.ajaxList[o][e.url].abort();
                var s = $.ajax(e);
                this.ajaxList[o][e.url] = s, s.done(t).then(a)
            } else {
                window.clearTimeout(this.ajaxList.handle);
                var c = this;
                this.ajaxList.handle = window.setTimeout(function () {
                    c.ajaxList[o].lastTime = +new Date, c.ajaxList[o][e.url] && c.aborted && c.ajaxList[o][e.url].abort();
                    var i = $.ajax(e);
                    c.ajaxList[o][e.url] = i, i.done(t).then(a)
                }, this.delayTime)
            }
        } else {
            this.ajaxList.handle = void 0, this.ajaxList[o] = this.ajaxList[o] || {}, this.ajaxList[o].lastTime = +new Date;
            var s = $.ajax(e);
            this.ajaxList[o][e.url] = s, s.done(t).then(a)
        }
    }, o = function (e) {
        if (!e.url)throw new Error("url underfind");
        a.apply(this, arguments)
    }, i = function (e) {
        e = e || {}, this.aborted = e.aborted || !1, this.delayTime = e.delayTime || 0, this.predicate = e.predicate || function () {
            return this.url
        }, this.ajaxList = {}
    };
    return e.init = function (e) {
        i.prototype.addAjax = o;
        var t = new i(e);
        return t
    }, e
}(), function () {
    function e(e) {
        return s.raw ? e : encodeURIComponent(e)
    }

    function t(e) {
        return s.raw ? e : decodeURIComponent(e)
    }

    function a(t) {
        return e(s.json ? JSON.stringify(t) : String(t))
    }

    function o(e) {
        0 === e.indexOf('"') && (e = e.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, "\\"));
        try {
            return e = decodeURIComponent(e.replace(n, " ")), s.json ? JSON.parse(e) : e
        } catch (t) {
        }
    }

    function i(e, t) {
        var a = s.raw ? e : o(e);
        return $.isFunction(t) ? t(a) : a
    }

    var n = /\+/g, s = $.cookie = function (o, n, c) {
        if (void 0 !== n && !$.isFunction(n)) {
            if (c = $.extend({}, s.defaults, c), "number" == typeof c.expires) {
                var l = c.expires, r = c.expires = new Date;
                r.setTime(+r + 864e5 * l)
            }
            return document.cookie = [e(o), "=", a(n), c.expires ? "; expires=" + c.expires.toUTCString() : "", c.path ? "; path=" + c.path : "", c.domain ? "; domain=" + c.domain : "", c.secure ? "; secure" : ""].join("")
        }
        for (var d = o ? void 0 : {}, u = document.cookie ? document.cookie.split("; ") : [], h = 0, p = u.length; p > h; h++) {
            var m = u[h].split("="), f = t(m.shift()), v = m.join("=");
            if (o && o === f) {
                d = i(v, n);
                break
            }
            o || void 0 === (v = i(v)) || (d[f] = v)
        }
        return d
    };
    s.defaults = {}, $.removeCookie = function (e, t) {
        return void 0 === $.cookie(e) ? !1 : ($.cookie(e, "", $.extend({}, t, {expires: -1})), !$.cookie(e))
    }
}();