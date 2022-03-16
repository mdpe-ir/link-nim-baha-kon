(function ($) {
    "use strict";


    /*==================================================================
    [ Validate ]*/

    var links = $('.validate-input textarea[name="links"]');
    var outputs = $('.validate-input textarea[name="outputs"]');
    const siteUrl = 'https://www.digitalbam.ir/';

    $('.validate-form').on('submit', function () {
        var check = true;
        var loading = false;

        try {


            if ($(links).val().trim() == '') {
                showValidate(links);
                check = false;

            }

            if (check) {

                const value = $(links).val();
                let linkList = value.split(/\r?\n/);
                document.getElementById('outputs').value = "";
                document.getElementById("loading").removeAttribute("hide");
                document.getElementById("unloaidng").setAttribute("hide", "hide");
                document.getElementById("loadingIcon").removeAttribute("hide");
                document.getElementById("unloadingIcon").setAttribute("hide", "hide");
                loading = true;


                linksGenerator(linkList).then(r => {
                    loading = false;
                    document.getElementById("unloaidng").removeAttribute("hide");
                    document.getElementById("loading").setAttribute("hide", "hide");
                    document.getElementById("unloadingIcon").removeAttribute("hide");
                    document.getElementById("loadingIcon").setAttribute("hide", "hide");
                    var x = document.getElementById("snackbar");
                    x.className = "show";
                    setTimeout(function () {
                        x.className = x.className.replace("show", "");
                    }, 3000);
                }) ;




            }


        } catch (e) {
            console.log(e);
            return false;

        }

        return false;
    });


    $('.validate-form .input1').each(function () {
        $(this).focus(function () {
            hideValidate(this);


        });
    });

    async function linksGenerator(linkList){
        for (let i = 0; i < linkList.length; i++) {
            if (linkList[i].trim() != '') {
                linkList[i] = linkList[i].trim();
                let link = linkList[i];
                if (link.indexOf('http') === 0) {


                    await  $.post("https://www.digitalbam.ir/Home/DetectSearchPrase", {Phrase: encodeURIComponent(link)}, function (data) {


                        if (data === "downloadLink")
                            $.post("https://www.digitalbam.ir/DirectLinkDownloader/Download", {downloadUri: encodeURIComponent(link)}, function (data) {
                                // window.location.href = data.fileUrl;
                                document.getElementById('outputs').value += data.fileUrl + '\n\n';

                            });
                        // }
                    });


                }

            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
        $(thisAlert).focus();
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }


})(jQuery);