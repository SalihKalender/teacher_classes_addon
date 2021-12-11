odoo.define('university_teacher.add_class', function (require) {
    let student_count = 0;
    $('#add_student_button').click(function () {
        student_count++;
        const students_row = document.querySelector('#students_row')
        const container = document.createElement('div')
        container.className = 'p-3 border-info student_input_container'
        const label = document.createElement('label')
        label.htmlFor = 'student_name'
        label.innerText = 'Student Name'
        container.appendChild(label)
        const input_div = document.createElement('div')
        input_div.className = 'col-sm- d-flex'
        const input = document.createElement('input')
        input.setAttribute('required', '')
        input.className = 'form-control'
        input.id = 'student_' + student_count
        input.name = 'student_' + student_count
        input_div.appendChild(input)
        const delete_button = document.createElement('button')
        delete_button.className = 'btn btn-danger ml-2 delete_button'
        delete_button.id = student_count.toString()
        delete_button.innerText = 'Delete'
        delete_button.type = 'button'
        input_div.appendChild(delete_button)
        container.appendChild(input_div)
        students_row.appendChild(container)
        if (student_count !== 0) {
            $('#student_count').text(student_count)
            $('#student_count_container').show()
        }
    })
    $(document).on('click', "button.delete_button", function (e) {      
        student_count--
        e.preventDefault()
        $(e.target).parents('.student_input_container').remove()
        $('#student_count').text(student_count)
        if(student_count === 0) {
            $('#student_count_container').hide()
        }
    });
})