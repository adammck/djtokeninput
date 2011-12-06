jQuery(function() {
  jQuery("input.tokeninput").each(function() {
    var field = jQuery(this);

    field.tokenInput(
      field.data("search-url"),
      field.data("settings")
    );
  });
});
