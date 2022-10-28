const url = 'https://fourtonfish.com/hellosalut/?lang=';
document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(function () {
    $.get(url + $('INPUT#language_code').val(), function (data, status) {
      if (status === 'success') {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
