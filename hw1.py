academic_hour_duration=40
break_duration=15
astronomic_hour_duration=60
course_academic_hours=64

course_astronomic_hours=(course_academic_hours*academic_hour_duration+((course_academic_hours/3)*break_duration))/astronomic_hour_duration

print(course_astronomic_hours)



