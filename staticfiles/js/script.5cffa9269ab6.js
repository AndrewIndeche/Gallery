function myFunction() {
    var copyText = document.getElementById("{{item.id}}image_link.url");

    copyText.select();
    copyText.setSelectionRange(0, 99999);

    document.execCommand("copy");
}

$(function() {
    $('button[data-toggle="tooltip"]').tooltip({
        animated: 'fade',
        placement: 'top',
        trigger: 'click'
    });
})
