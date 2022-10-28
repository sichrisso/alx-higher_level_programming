document.addEventListener('DOMContentLoaded', function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
    if (status === 'success') {
      $('div#hello').text(data.hello);
    }
  });
});
