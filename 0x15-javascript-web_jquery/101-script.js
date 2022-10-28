document.addEventListener('DOMContentLoaded', function () {
  const list = $('UL.my_list');
  const item = '<li>Item</li>';
  $('div#add_item').click(function () {
    list.append(item);
  });

  $('div#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  $('div#clear_list').click(function () {
    $('ul.my_list li').each(function () {
      $(this).remove();
    });
  });
});
