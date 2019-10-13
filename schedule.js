
export const renderCourseCard = function(course){
    return(
        `<section>
            <div>
                <div class="box">
                    <p>${course.name}</p>
                    <p>${course.professor}</p>
                    <p>${course.time}</p>
                    <p>${course.rating}</p>
                </div>
            </div>
        </section>`
    );
}

export const loadCoursesIntoDOM = function() {
    const $root = $('#root');

    let finalCourses = [];

    for(let i = 0; i < courseData.length; i++) {
        finalCourses[i] = renderCourseCard(courseData[i]);
    }

    $root.append(finalCourses);
}

$(function() {
    loadCoursesIntoDOM(courseData);
});