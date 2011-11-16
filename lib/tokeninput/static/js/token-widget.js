jQuery(function() {
  jQuery("input.token-input").each(function() {
    var field = jQuery(this);

    field.tokenInput(field.data("search-url"), {
      prePopulate: field.data("prepopulate")
    });
  });
});
