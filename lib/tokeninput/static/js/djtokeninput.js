jQuery(function() {
  jQuery("input.tokeninput").each(function() {
    var field = jQuery(this);

    field.tokenInput(field.data("search-url"), {
      prePopulate: field.data("prepopulate"),
      preventDuplicates: true
    });
  });
});
