$(function () {
    $('#something').on('input', function () {
            var url = "{% url 'dash_township_detail_view' 123 %}";
            var opt = $('option[value="' + $(this).val() + '"]');
            if (opt.attr('id')!=null && opt.attr('id')!=undefined) {
            document.location.href = url.replace('123', opt.attr('id'))
            };
          });
        });