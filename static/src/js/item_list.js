odoo.define('university_teacher.exam_list', function (require) {
    $(function () {
        $('.collapse').on('show.bs.collapse', function () {
            var toggle = $('[data-target="#' + this.id + '"]');
            if (toggle) {
                var parent = toggle.attr('data-parent');
                if (parent) {
                    $(parent).find('.collapse.in').collapse('hide');
                }
            }
        });
    })
})