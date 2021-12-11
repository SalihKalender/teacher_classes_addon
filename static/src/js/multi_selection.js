odoo.define('university_teacher.add_exam', function (require) {
    function createTable(students) {
        const myTableDiv = document.getElementById("results_table");
        myTableDiv.innerHTML = ''
        const table = document.createElement('TABLE');
        table.border = '1';
        table.className = 'table table-striped'

        const tableBody = document.createElement('TBODY');
        table.appendChild(tableBody);

        students.forEach((student, index) => {
            const tr = document.createElement('TR');
            tableBody.appendChild(tr);
            Object.entries(student).forEach((value, index) => {
                if (index !== 0) {      
                    if (index === 3) {
                        console.log(student.id)
                        const td = document.createElement('TD');
                        const point_input = document.createElement('input')
                        point_input.type = "text"
                        point_input.className = 'student_point form-control'
                        point_input.name = `student_${student.id}`
                        point_input.id = `student_${student.id}`
                        if (student.point) {
                            point_input.value = student.point
                        }
                        td.appendChild(point_input)
                        tr.appendChild(td)
                        $(point_input).on('change', function (e) {
                            student.point = e.target.value
                        })
                        return;
                    }
                    const td = document.createElement('TD');
                    td.width = '150';
                    td.appendChild(document.createTextNode(value[1]));
                    tr.appendChild(td);
                }
            })
        })
        myTableDiv.append(table)
    }

    let all_students = []
    const rpc = require('web.rpc')
    document.querySelector(".c-filter__toggle").addEventListener("click", function (e) {
        e.preventDefault()
        this.classList.toggle("c-filter__toggle--active");
        document.querySelector(".c-filter__ul").classList.toggle("c-filter__ul--active");
    });
    $('.classes_checkbox').click(async function (e) {
        const is_checked = e.target.checked
        const class_id = e.target.value
        const class_name = e.target.name.replace('class_', '')
        // console.log(class_id)
        if (is_checked) {
            let students = null
            try {
                students = await rpc.query({
                    model: 'student.student',
                    method: 'search_read',
                    kwargs: {
                        domain: [['class_room.id', '=', class_id]],
                        fields: ['id', 'name']
                    }
                })
            } catch (err) {
                return console.log(err)
            }
            students.forEach((student) => {
                student.class_room = class_name
                student.point = null
                let is_there = false
                all_students.forEach((all_student) => {
                    if (all_student.id === student.id) {
                        is_there = true
                    }
                })
                if (!is_there) {
                    all_students.push(student)
                }
            })
        } else {
            all_students = all_students.filter(student => student.class_room !== class_name)
        }
        createTable(all_students)
    })


})


