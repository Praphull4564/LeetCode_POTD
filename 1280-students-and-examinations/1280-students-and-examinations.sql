select s.student_id,s.student_name,s.subject_name,coalesce(e.attended_exams,0) as attended_exams from
(select * from Students join Subjects)s left join
(select *,count(*) as attended_exams from Examinations group by student_id,subject_name)e
on (s.student_id=e.student_id and s.subject_name=e.subject_name)
order by student_id,subject_name