// add list element to existing ul element
$("div#add_item").on("click", function () {
  $("ul.my_list").append("<li>Item</li>");
});
