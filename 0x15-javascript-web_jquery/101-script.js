const $ = window.$;
window.onload = () => {
  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(() => {
    $('UL.my_list li:last-child').remove();
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list').children().remove();
  });
};