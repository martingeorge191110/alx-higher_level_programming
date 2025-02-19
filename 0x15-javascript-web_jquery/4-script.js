const $ = window.$;
$('div#toggle_header').on('click', () => {
  $('header').toggleClass('green red');
});
