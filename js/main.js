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
                document.getElementById("loading").removeAttribute("hidden");
                document.getElementById("unloaidng").setAttribute("hidden", "hidden");
                document.getElementById("loadingIcon").removeAttribute("hidden");
                document.getElementById("unloadingIcon").setAttribute("hidden", "hidden");
                loading = true;


                linksGenerator(linkList).then(r => {
                    loading = false;
                    document.getElementById("unloaidng").removeAttribute("hidden");
                    document.getElementById("loading").setAttribute("hidden", "hidden");
                    document.getElementById("unloadingIcon").removeAttribute("hidden");
                    document.getElementById("loadingIcon").setAttribute("hidden", "hidden");
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